"""
Description: 测试使用python运行pytest示例。
Notes: 
访问 "https://playwright.dev/" 需要开启代理，否则会提示 "playwright._impl._errors.TimeoutError: Page.goto: Timeout 30000ms exceeded."。
"""
import sys
import os

# 获取当前脚本的绝对路径
current_script_path = os.path.abspath(__file__)
# 获取当前脚本的父目录的父目录
parent_directory_of_the_parent_directory = os.path.dirname(os.path.dirname(current_script_path))
# 将这个目录添加到 sys.path
sys.path.append(parent_directory_of_the_parent_directory)

from dotenv import load_dotenv

load_dotenv('env_config/.env.local')

# 设置代理环境变量
os.environ['http_proxy'] = os.getenv("HTTP_PROXY")
os.environ['https_proxy'] = os.getenv("HTTPS_PROXY")

import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield
    
    print("after the test runs")

def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/")
    
if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "Getting_Started/test_example_fixtures.py"])
