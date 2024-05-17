"""
Description: playwright初始测试示例。
Notes: 
访问 "https://playwright.dev/" 需要开启代理，否则会提示 "playwright._impl._errors.TimeoutError: Page.goto: Timeout 30000ms exceeded."。
"""
import os
from dotenv import load_dotenv

load_dotenv('env_config/.env.local')

# 设置代理环境变量
os.environ['http_proxy'] = os.getenv("HTTP_PROXY")
os.environ['https_proxy'] = os.getenv("HTTPS_PROXY")

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()