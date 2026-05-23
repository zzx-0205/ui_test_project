"""商品列表页 - POM 页面对象"""
from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.first_add_to_cart_btn = page.locator("button[id^='add-to-cart']").first
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def is_loaded(self) -> bool:
        """判断页面是否加载成功"""
        return self.title.is_visible()

    def add_first_item_to_cart(self):
        """添加第一个商品到购物车"""
        self.first_add_to_cart_btn.click()

    def get_cart_count(self) -> str:
        """获取购物车角标数量"""
        return self.cart_badge.text_content()

    def go_to_cart(self):
        """进入购物车"""
        self.cart_icon.click()