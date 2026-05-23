# UI 自动化测试框架 (Playwright + Pytest)

基于 **Python + Playwright + Pytest** 的 UI 自动化测试项目，以 [Saucedemo](https://www.saucedemo.com) 电商网站为被测应用，实现**登录验证**与**完整下单流程**的自动化测试。

## 🛠 技术栈
- Python 3.8+
- Playwright（微软出品，现代 UI 自动化框架）
- Pytest（fixture、parametrize）
- POM 页面对象模式
- JSON 数据驱动

## 📂 项目结构
├── config/          # 配置文件
├── pages/           # POM 页面对象
├── test_data/       # JSON 参数化测试数据
├── test_cases/      # 测试用例
│   ├── conftest.py  # fixture + 失败截图
│   └── test_checkout.py
└── screenshots/     # 失败截图目录

## 🚀 快速开始
1. 安装依赖：`pip install -r requirements.txt`
2. 安装浏览器：`playwright install chromium`
3. 运行测试：`pytest -v`

## 📝 测试覆盖
- 登录参数化（标准用户 / 被锁用户 / 空用户名）
- 添加商品到购物车
- 完整下单流程（加购 → 结账 → 填写信息 → 完成）

## 💡 设计亮点
- POM 分层，页面元素与测试逻辑解耦
- JSON 外部数据驱动，易于扩展测试场景
- 失败自动截图，便于快速定位问题
- Session 级浏览器复用，fixture 管理页面隔离
## 🪄 作者
周子旋-UI 自动化测试实习项目