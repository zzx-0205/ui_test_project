"""结算页 - POM 页面对象"""
from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_btn = page.locator("[data-test='checkout']")
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_btn = page.locator("[data-test='continue']")
        self.finish_btn = page.locator("[data-test='finish']")
        self.complete_header = page.locator(".complete-header")
        self.thank_you_text = page.locator(".complete-text")

    def click_checkout(self):
        """点击 Checkout 按钮"""
        self.checkout_btn.click()

    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str):
        """填写收货人信息"""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_btn.click()

    def click_finish(self):
        """点击 Finish 完成下单"""
        self.finish_btn.click()

    def is_order_successful(self) -> bool:
        """判断下单是否成功"""
        return self.complete_header.is_visible() and "Thank you" in self.complete_header.text_content()