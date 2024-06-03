import asyncio
from playwright.async_api import async_playwright

async def scrape_weibo_hot_search():
    async with async_playwright() as p:
        # 启动Chromium浏览器
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        # 访问微博热搜页面
        page = await context.new_page()
        await page.goto("https://weibo.com/")

        # 等待热搜元素加载
        await page.wait_for_selector('div.wbpro-side-bottom')

        # 获取热搜列表
        hot_search_div = await page.query_selector('div.wbpro-side-bottom')
        hot_search_items = await hot_search_div.query_selector_all('li')

        # 输出热搜内容
        for index, item in enumerate(hot_search_items, start=1):
            title = await item.inner_text()
            print(f"{index}. {title}")

        # 关闭浏览器
        await browser.close()

# 运行爬取任务
asyncio.run(scrape_weibo_hot_search())
