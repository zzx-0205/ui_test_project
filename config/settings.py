"""全局配置"""
BASE_URL = "https://www.saucedemo.com"
TIMEOUT = 10000  # Playwright 超时，单位毫秒

# Saucedemo 内置测试账号
USERS = {
    "standard_user": "secret_sauce",
    "locked_out_user": "secret_sauce",
    "problem_user": "secret_sauce",
}