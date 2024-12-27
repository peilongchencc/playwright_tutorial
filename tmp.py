import asyncio
from playwright.async_api import async_playwright

async def main():
    """
    使用 Playwright 异步 API 打开百度主页，并输出页面标题。
    
    功能描述：
    1. 启动一个 Chromium 浏览器实例。
    2. 创建一个新页面并导航到百度主页。
    3. 获取并打印页面标题。
    4. 在百度搜索框中输入 "Playwright"，然后点击搜索按钮。
    5. 最后关闭浏览器。

    注意事项：
    - 浏览器以有界面模式运行 (headless=False)。
    - slow_mo=100 用于延迟操作，便于观察浏览器行为。
    - 使用wait_for_timeout(5000)等待页面加载，确保页面完全加载。
    """
    # 使用 `async_playwright` 进行异步操作
    async with async_playwright() as p:
        # 启动 Chromium 浏览器
        # 参数 `headless=False` 启动有界面模式（即显示浏览器窗口）
        # 参数 `slow_mo=100` 使每个操作间隔 100 毫秒，方便观察
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        
        # 创建一个新的浏览器页面实例
        page = await browser.new_page()
        
        # 导航到百度主页，通过 URL 进行访问
        await page.goto("https://www.baidu.com")
        
        # 获取当前页面的标题，并打印到控制台
        print(await page.title())

        # 暂停 5 秒，模拟短暂等待以确保页面完全加载
        await page.wait_for_timeout(5000)
        
        # 在百度搜索框（id 为 "kw"）中输入 "Playwright"
        await page.fill('#kw', "Playwright")
        
        # 点击百度搜索按钮（id 为 "su"）
        await page.click('#su')
        
        # 关闭浏览器以释放资源
        await browser.close()

# 运行异步主函数 `main`
# 使用 asyncio 的 `run` 方法启动异步事件循环
asyncio.run(main())