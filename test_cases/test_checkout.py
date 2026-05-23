"""核心测试用例：登录参数化 + 完整下单流程"""
import json
import os
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def load_user_data():
    """从 JSON 文件加载参数化测试数据"""
    json_path = os.path.join(
        os.path.dirname(__file__), "..", "test_data", "users.json"
    )
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


class TestLogin:
    """登录功能测试"""

    @pytest.mark.parametrize("user", load_user_data())
    def test_login(self, page, user):
        """参数化测试：验证不同账号的登录表现"""
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(user["username"], user["password"])

        if user["should_succeed"]:
            inventory_page = InventoryPage(page)
            assert inventory_page.is_loaded(), (
                f"【{user['description']}】登录后应跳转到商品页"
            )
        else:
            error_text = login_page.get_error_text().lower()
            assert any(keyword in error_text for keyword in ["locked out", "required"]), (
                f"【{user['description']}】错误提示不匹配，实际：{error_text}"
            )


class TestCheckout:
    """下单流程测试"""

    def test_add_to_cart(self, logged_in_page):
        """测试添加商品到购物车"""
        inventory_page = InventoryPage(logged_in_page)
        assert inventory_page.is_loaded(), "商品页加载失败"

        inventory_page.add_first_item_to_cart()
        count = inventory_page.get_cart_count()
        assert count == "1", f"购物车角标应为 1，实际为 {count}"

    def test_complete_checkout(self, logged_in_page):
        """完整下单流程：加购 → 结账 → 填写信息 → 完成"""
        inventory_page = InventoryPage(logged_in_page)
        checkout_page = CheckoutPage(logged_in_page)

        # 1. 确保在商品页
        assert inventory_page.is_loaded(), "商品页加载失败"

        # 2. 添加商品 → 进入购物车
        inventory_page.add_first_item_to_cart()
        inventory_page.go_to_cart()

        # 3. 点击 Checkout
        checkout_page.click_checkout()

        # 4. 填写收货信息
        checkout_page.fill_shipping_info("张", "三", "100000")

        # 5. 点击 Finish
        checkout_page.click_finish()

        # 6. 断言下单成功
        assert checkout_page.is_order_successful(), "下单后应显示 Thank you 成功页面"