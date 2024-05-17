# playwright_tutorial

本章介绍playwright框架的使用，笔者使用的系统为 ubuntu 20.04。<br>

- [playwright\_tutorial](#playwright_tutorial)
  - [System requirements:](#system-requirements)
  - [Installation](#installation)
    - [Introduction](#introduction)
    - [Installing Playwright Pytest(安装 Playwright Pytest):](#installing-playwright-pytest安装-playwright-pytest)
    - [Add Example Test(添加示例测试):](#add-example-test添加示例测试)
    - [`test_` 前缀补充:](#test_-前缀补充)
    - [Running the Example Test(运行示例测试):](#running-the-example-test运行示例测试)
    - [Updating Playwright(更新 Playwright):](#updating-playwright更新-playwright)


## System requirements:

- Python 3.8 or higher.

- Windows 10+, Windows Server 2016+ or Windows Subsystem for Linux (WSL).

- MacOS 12 Monterey, MacOS 13 Ventura, or MacOS 14 Sonoma.

- Debian 11, Debian 12, Ubuntu 20.04 or Ubuntu 22.04.


## Installation

### Introduction

Playwright was created specifically to accommodate the needs of end-to-end testing.<br>

Playwright 专门为满足端到端测试的需求而创建。<br>

Playwright supports all modern rendering engines including Chromium, WebKit, and Firefox.<br>

Playwright 支持所有现代渲染引擎，包括 Chromium、WebKit 和 Firefox。<br>

Test on Windows, Linux, and macOS, locally or on CI, headless or headed with native mobile emulation.<br>

在 Windows、Linux 和 macOS 上进行测试，可以本地或在 CI 上进行，无头或有头模式下使用原生移动仿真。<br>

The Playwright library can be used as a general purpose browser automation tool, providing a powerful set of APIs to automate web applications, **for both `sync` and `async` Python** 🔥.<br>

Playwright 库可以用作通用浏览器自动化工具，提供一套强大的 API 来自动化网络应用，支持同步和异步的 Python。<br>

This introduction describes the Playwright Pytest plugin, which is the recommended way to write end-to-end tests.<br>

本介绍描述了 Playwright Pytest 插件，这是编写端到端测试的推荐方式。<br>

**You will learn(你将学到)** :<br>

- How to install Playwright Pytest / 如何安装 Playwright Pytest

- How to run the example test / 如何运行示例测试

### Installing Playwright Pytest(安装 Playwright Pytest):

Playwright recommends using the official **[Playwright Pytest plugin](https://playwright.dev/python/docs/test-runners)** to write end-to-end tests.<br>

Playwright 推荐使用官方的 Playwright Pytest 插件来编写端到端测试。<br>

It provides context isolation, running it on multiple browser configurations out of the box.<br>

它提供上下文隔离，开箱即用地在多个浏览器配置上运行。<br>

Get started by installing Playwright and running the example test to see it in action.<br>

通过安装 Playwright 并运行示例测试开始，看看它的实际效果。<br>

Install the Pytest plugin(安装 Pytest 插件):<br>

```bash
pip install pytest-playwright
```

Install the required browsers(安装需要的浏览器):<br>

```bash
playwright install
```

playwright不需要像selenium一样下载ChromeDriver。<br>

Playwright 的一个显著优势是它自带了所有支持的浏览器（如 Chromium、Firefox 和 WebKit）的驱动程序。<br>

当你使用 `playwright install` 命令时，它会自动下载所需的浏览器二进制文件和相应的驱动。这一点与 Selenium 不同，在使用 Selenium 时，你需要根据浏览器版本手动下载对应的 WebDriver（如 ChromeDriver 或 GeckoDriver）。<br>

这种自包含的设计简化了 Playwright 的设置过程，让用户可以更轻松地开始自动化测试，无需担心驱动程序与浏览器版本之间的兼容性问题。<br>

终端运行`playwright install`后显示如下:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/playwright_tutorial# playwright install
Downloading Chromium 124.0.6367.29 (playwright build v1112) from https://playwright.azureedge.net/builds/chromium/1112/chromium-linux.zip
155.3 MiB [====================] 100% 0.0s
Chromium 124.0.6367.29 (playwright build v1112) downloaded to /root/.cache/ms-playwright/chromium-1112
Downloading FFMPEG playwright build v1009 from https://playwright.azureedge.net/builds/ffmpeg/1009/ffmpeg-linux.zip
2.6 MiB [====================] 100% 0.0s
FFMPEG playwright build v1009 downloaded to /root/.cache/ms-playwright/ffmpeg-1009
Downloading Firefox 124.0 (playwright build v1447) from https://playwright.azureedge.net/builds/firefox/1447/firefox-ubuntu-22.04.zip
85.4 MiB [====================] 100% 0.0s
Firefox 124.0 (playwright build v1447) downloaded to /root/.cache/ms-playwright/firefox-1447
Downloading Webkit 17.4 (playwright build v1992) from https://playwright.azureedge.net/builds/webkit/1992/webkit-ubuntu-22.04.zip
86.5 MiB [====================] 100% 0.0s
Webkit 17.4 (playwright build v1992) downloaded to /root/.cache/ms-playwright/webkit-1992
Playwright Host validation warning: 
╔══════════════════════════════════════════════════════╗
║ Host system is missing dependencies to run browsers. ║
║ Missing libraries:                                   ║
║     libgstcodecparsers-1.0.so.0                      ║
║     libflite.so.1                                    ║
║     libflite_usenglish.so.1                          ║
║     libflite_cmu_grapheme_lang.so.1                  ║
║     libflite_cmu_grapheme_lex.so.1                   ║
║     libflite_cmu_indic_lang.so.1                     ║
║     libflite_cmu_indic_lex.so.1                      ║
║     libflite_cmulex.so.1                             ║
║     libflite_cmu_time_awb.so.1                       ║
║     libflite_cmu_us_awb.so.1                         ║
║     libflite_cmu_us_kal16.so.1                       ║
║     libflite_cmu_us_kal.so.1                         ║
║     libflite_cmu_us_rms.so.1                         ║
║     libflite_cmu_us_slt.so.1                         ║
║     libx264.so                                       ║
╚══════════════════════════════════════════════════════╝
    at validateDependenciesLinux (/root/anaconda3/lib/python3.11/site-packages/playwright/driver/package/lib/server/registry/dependencies.js:216:9)
    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
    at async Registry._validateHostRequirements (/root/anaconda3/lib/python3.11/site-packages/playwright/driver/package/lib/server/registry/index.js:587:43)
    at async Registry._validateHostRequirementsForExecutableIfNeeded (/root/anaconda3/lib/python3.11/site-packages/playwright/driver/package/lib/server/registry/index.js:685:7)
    at async Registry.validateHostRequirementsForExecutablesIfNeeded (/root/anaconda3/lib/python3.11/site-packages/playwright/driver/package/lib/server/registry/index.js:674:43)
    at async t.<anonymous> (/root/anaconda3/lib/python3.11/site-packages/playwright/driver/package/lib/cli/program.js:119:7)
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/playwright_tutorial# 
```

### Add Example Test(添加示例测试):

Create a file that follows the `test_` prefix convention, such as `test_example.py`, inside the current working directory or in a sub-directory with the code below.<br>

在当前工作目录或子目录中创建一个遵循 `test_` 前缀约定的文件，例如 `test_example.py`，并使用下面的代码。<br>

🚨Make sure your test name also follows the `test_` prefix convention.<br>

🚨确保你的测试名称也遵循 `test_` 前缀约定。<br>

```python
# test_example.py
# 需要开启代理才能访问 "https://playwright.dev/"。
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
```

这段代码属于“使用 Playwright 与 Pytest”的类型。这里有几个明显的迹象说明了这一点：<br>

1. **函数命名**：函数名以 `test_` 开头，这是 Pytest 用于识别测试用例的常用命名约定。
2. **导入的库**：虽然代码中没有直接导入 `pytest`，但使用了 `expect` 来自 `playwright.sync_api`，这通常与测试断言相关联，用于验证测试预期。
3. **测试函数参数**：函数 `test_has_title` 和 `test_get_started_link` 接受 `page: Page` 参数。这种参数传递通常是在使用 Pytest 时，结合 fixture 使用的方式，fixture 用于设置和传递测试环境或对象。
4. **测试断言**：使用了 `expect` 函数来进行断言检查，如页面标题是否包含特定内容，以及页面元素的可见性。这是测试框架中常见的做法，用于校验页面达到了预期的状态。

总的来说，这段代码显示了典型的测试结构，使用 Pytest 运行 Playwright 测试的标准方式。代码的目的是验证页面在特定操作后的状态，符合自动化测试脚本的特点。<br>

### `test_` 前缀补充:

Playwright 本身并不要求文件必须以 `test_` 前缀开头。你可以给文件命名为任何合法的名称。<br>

然而，如果你使用 Playwright 集成了测试框架，如 Pytest，文件名以 `test_` 开头的约定可能会用到。<br>

这是因为 Pytest 会自动发现并运行所有以 `test_` 开头的 Python 文件中定义的测试。<br>

如果你仅仅是在使用 Playwright 进行浏览器自动化而不是进行系统测试，那么文件名没有特定的要求。但如果你打算构建自动化测试套件并使用 Pytest 这样的测试运行器，遵循这种命名约定将有助于 Pytest 识别和执行测试。<br>

总结来说：<br>

- **仅使用 Playwright**：文件名可以是任何有效的 Python 文件名。

- **使用 Playwright 与 Pytest**：建议使用 `test_` 前缀以便 Pytest 自动识别和运行测试。

### Running the Example Test(运行示例测试):

By default tests will be run on chromium.<br>

默认情况下，测试将在 Chromium 上运行。<br>

This can be configured via the [CLI options](https://playwright.dev/python/docs/running-tests).<br>

这可以通过 CLI 选项进行配置。<br>

Tests are run in headless mode meaning no browser UI will open up when running the tests.<br>

测试在无头模式下运行，这意味着在运行测试时不会打开浏览器 UI。<br>

Results of the tests and test logs will be shown in the terminal.<br>

测试结果和测试日志将显示在终端中。<br>

```bash
pytest
```

上述代码会运行`test_example.py`，终端显示如下:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/playwright_tutorial# pytest
================================================================= test session starts ==================================================================
platform linux -- Python 3.11.7, pytest-7.4.0, pluggy-1.0.0
rootdir: /data/playwright_tutorial
plugins: base-url-2.1.0, anyio-4.2.0, playwright-0.5.0
collected 2 items                                                                                                                                      

test_example.py ..                                                                                                                               [100%]

================================================================== 2 passed in 5.13s ===================================================================
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/playwright_tutorial# 
```

### Updating Playwright(更新 Playwright):

To update Playwright to the latest version run the following command:<br>

要将 Playwright 更新到最新版本，请运行以下命令：<br>

```bash
pip install pytest-playwright playwright -U
```
