# playwright安装:

- [playwright安装:](#playwright安装)
  - [前言](#前言)
  - [为什么要学 Playwright ？](#为什么要学-playwright-)
    - [跨浏览器和平台](#跨浏览器和平台)
    - [稳定性](#稳定性)
    - [运行机制](#运行机制)
    - [完全隔离-快速执行](#完全隔离-快速执行)
    - [强大的工具](#强大的工具)
  - [环境准备](#环境准备)
    - [安装 playwright：](#安装-playwright)
    - [安装所需的浏览器 chromium,firefox 和 webkit：](#安装所需的浏览器-chromiumfirefox-和-webkit)
    - [简单使用](#简单使用)
    - [headless 模式](#headless-模式)
  - [关于页面操作的等待](#关于页面操作的等待)
  - [time.sleep() 的不再使用](#timesleep-的不再使用)
    - [wait\_for\_timeout 和 slow\_mo 的区别:](#wait_for_timeout-和-slow_mo-的区别)
    - [**什么时候用哪个？**](#什么时候用哪个)


## 前言

说到 web 自动化，大家最熟悉的就是 selenium 了，selenium 之后又出现了三个强势的框架Puppeteer、CyPress、TestCafe， 但这3个都需要掌握 JavaScript 语言，所以只是少部分人在用。

2020年微软开源一个 UI 自动化测试工具 Playwright , 支持 Node.js、Python、C# 和 Java 语言。


## 为什么要学 Playwright ？
selenium 在国内普及程度非常高，说到 web 自动化很多人第一个就会想到 selenium，它的出现确实是给整个行业带来了很多的影响。

支持多语言，开源的框架，可以兼容多种浏览器，上手非常容易。

那么现在微软推出的 Playwright 到底有没必要去学呢？先看下[官方介绍](https://playwright.dev/python/):

### 跨浏览器和平台

- 跨浏览器。Playwright 支持所有现代渲染引擎，包括 Chromium、WebKit 和 Firefox。
- 跨平台。在 Windows、Linux 和 macOS 上进行本地测试或在 CI 上进行无头或有头测试。
- 跨语言。在TypeScript、JavaScript、Python、.NET、Java中使用 Playwright API 。
- 测试移动网络。适用于 Android 和 Mobile Safari 的 Google Chrome 浏览器的本机移动仿真。相同的渲染引擎适用于您的桌面和云端。

### 稳定性

- 自动等待。Playwright 在执行动作之前等待元素可操作。它还具有一组丰富的内省事件。两者的结合消除了人为超时的需要——这是不稳定测试的主要原因。
- Web优先断言。Playwright 断言是专门为动态网络创建的。检查会自动重试，直到满足必要的条件。
- 追踪。配置测试重试策略，捕获执行跟踪、视频、屏幕截图以消除薄片。

### 运行机制

浏览器在不同进程中运行属于不同来源的 Web 内容。 Playwright 与现代浏览器架构保持一致，并在进程外运行测试。这使得 Playwright 摆脱了典型的进程内测试运行器的限制。

- 多重一切。测试跨越多个选项卡、多个来源和多个用户的场景。为不同的用户创建具有不同上下文的场景，并在您的服务器上运行它们，所有这些都在一次测试中完成。
- 可信事件。悬停元素，与动态控件交互，产生可信事件。Playwright 使用与真实用户无法区分的真实浏览器输入管道。
- 测试框架，穿透 Shadow DOM。Playwright 选择器穿透影子 DOM 并允许无缝地输入帧。

### 完全隔离-快速执行

- 浏览器上下文。Playwright 为每个测试创建一个浏览器上下文。浏览器上下文相当于一个全新的浏览器配置文件。这提供了零开销的完全测试隔离。创建一个新的浏览器上下文只需要几毫秒。
- 登录一次。保存上下文的身份验证状态并在所有测试中重用它。这绕过了每个测试中的重复登录操作，但提供了独立测试的完全隔离。

### 强大的工具

- 代码生成器。通过记录您的操作来生成测试。将它们保存为任何语言。
- 调试。检查页面、生成选择器、逐步执行测试、查看点击点、探索执行日志。
- 跟踪查看器。捕获所有信息以调查测试失败。Playwright 跟踪包含测试执行截屏、实时 DOM 快照、动作资源管理器、测试源等等。


## 环境准备

Playwright 是专门为满足端到端测试的需要而创建的。Playwright 支持所有现代渲染引擎，包括 Chromium、WebKit（Safari 的浏览器引擎）和 Firefox。
在 Windows、Linux 和 macOS 上进行本地测试或在 CI 上进行测试.

python 版本要求 python3.7+ 版本。

### 安装 playwright：

```bash
pip install playwright
```

### 安装所需的浏览器 chromium,firefox 和 webkit：

```bash
playwright install
```

仅需这一步即可安装所需的浏览器，并且不需要安装驱动包了（解决了selenium启动浏览器，总是要找对应驱动包的痛点）

如果安装报错，提示缺少Visual C++， 解决办法：

安装Microsoft Visual C++ Redistributable 2019

```txt
https://aka.ms/vs/16/release/VC_redist.x64.exe
```

直接点击就可以下载了，下载后直接安装即可。


### 简单使用

安装后，您可以在 Python 脚本中使用 Playwright，并启动 3 种浏览器中的任何一种（chromium,firefox和webkit）。

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    """
    使用 Playwright 异步 API 打开百度主页，并输出页面标题。

    主要功能包括：
    1. 启动浏览器。
    2. 打开一个新页面并访问百度主页。
    3. 获取并打印页面标题。
    4. 关闭浏览器。
    """
    # 使用 `async_playwright` 进行异步操作
    async with async_playwright() as p:
        # 启动 Chromium 浏览器
        # headless=False 表示启动有界面的浏览器（非无头模式）
        browser = await p.chromium.launch(headless=False)
        
        # 创建一个新的页面实例
        page = await browser.new_page()
        
        # 导航到百度主页
        await page.goto("https://www.baidu.com")
        
        # 获取页面标题并打印
        print(await page.title())
        
        # 关闭浏览器
        await browser.close()

# 运行异步函数 `main`
asyncio.run(main())
```

终端输出:

```txt
百度一下，你就知道
```

### headless 模式

默认情况下，Playwright 以无头模式运行浏览器。要查看浏览器 UI，请 `headless=False` 在启动浏览器时传递标志。

```python
# 不填写，或者设置 headless=False 表示无头浏览器模式。
browser = await p.chromium.launch(headless=False)
```


## 关于页面操作的等待

🌈Playwright 打开浏览器运行脚本的速度那就是一个字：快！

```python
chromium.launch(headless=False, slow_mo=500)
```

您还可以用来 `slow_mo`（单位是毫秒）减慢执行速度。它的作用范围是全局的，从启动浏览器到操作元素每个动作都会有等待间隔，方便在出现问题的时候看到页面操作情况。

```python
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

        # 在百度搜索框（id 为 "kw"）中输入 "Playwright"
        await page.fill('#kw', "Playwright")
        
        # 点击百度搜索按钮（id 为 "su"）
        await page.click('#su')
        
        # 关闭浏览器以释放资源
        await browser.close()

asyncio.run(main())
```

运行后会发现每个操作都会有间隔时间。


## time.sleep() 的不再使用

Playwright 在查找元素的时候具有自动等待功能，如果你在调试的时候需要使用等待，你应该使用 `page.wait_for_timeout(5000)` 代替 `time.sleep(5)` 并且最好不要等待超时。

这是因为playwright内部依赖于异步操作，并且在使用时 `time.sleep(5)` 无法正确处理它们。

```python
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
```

### wait_for_timeout 和 slow_mo 的区别:

`wait_for_timeout` 和 `slow_mo` 是 Playwright 中两种不同的等待机制，它们的作用和使用场景不同，以下是详细的区别和适用场景：

| 特性               | `wait_for_timeout`                            | `slow_mo`                              |
|--------------------|-----------------------------------------------|-----------------------------------------|
| **作用范围**        | 单独的等待时间，阻塞当前代码执行              | 全局范围，影响每一步操作之间的延迟      |
| **设置方式**        | 在代码中显式调用                              | 在启动浏览器时配置                      |
| **是否可控**        | 可单独控制具体等待时长                        | 每个操作之间自动应用固定的延迟          |
| **适用场景**        | 特定场景下需要明确等待，通常用于调试或加载检查 | 放慢所有操作的速度以便观察行为          |

### **什么时候用哪个？**

- **用 `wait_for_timeout`：**  
  当你知道需要等待一段时间才能继续操作，例如页面上某些动态内容加载完成。

- **用 `slow_mo`：**  
  当你想要调试整个操作流程，观察每一步是如何执行的，而不需要手动插入等待代码。

在实际场景中，建议优先使用 Playwright 的**条件等待**方法（如 `wait_for_selector` 或 `wait_for_event`），而不是依赖 `wait_for_timeout` 或 `slow_mo`，因为条件等待更加高效和可靠。

