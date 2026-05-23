"""pytest 全局 fixture 与 Hooks"""
import os
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def browser():
    """启动本地 Edge 浏览器（Windows 自带，无需下载）"""
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """每个测试用例独立的页面（隔离上下文）"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def logged_in_page(page):
    """已登录的页面，给需要登录态的用例直接使用"""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    return page


# ========== 失败自动截图 ==========
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """测试失败时自动截图"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page") or item.funcargs.get("logged_in_page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = __import__("time").strftime("%Y%m%d_%H%M%S")
            filename = f"screenshots/{item.name}_{timestamp}.png"
            page.screenshot(path=filename)
            print(f"\n📸 失败截图已保存：{filename}")