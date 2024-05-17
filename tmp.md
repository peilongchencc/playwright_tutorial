我终端输入`pytest`运行下列代码后报错:

```python
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

终端显示:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/playwright_tutorial# pytest
================================================================= test session starts ==================================================================
platform linux -- Python 3.11.7, pytest-7.4.0, pluggy-1.0.0
rootdir: /data/playwright_tutorial
plugins: base-url-2.1.0, anyio-4.2.0, playwright-0.5.0
collected 2 items                                                                                                                                      

test_example.py 
FF                                                                                                                               [100%]

======================================================================= FAILURES =======================================================================
_______________________________________________________________ test_has_title[chromium] _______________________________________________________________

page = <Page url='https://playwright.dev/'>

    def test_has_title(page: Page):
>       page.goto("https://playwright.dev/")

test_example.py:5: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/root/anaconda3/lib/python3.11/site-packages/playwright/sync_api/_generated.py:8667: in goto
    self._sync(
/root/anaconda3/lib/python3.11/site-packages/playwright/_impl/_page.py:500: in goto
    return await self._main_frame.goto(**locals_to_params(locals()))
/root/anaconda3/lib/python3.11/site-packages/playwright/_impl/_frame.py:145: in goto
    await self._channel.send("goto", locals_to_params(locals()))
/root/anaconda3/lib/python3.11/site-packages/playwright/_impl/_connection.py:59: in send
    return await self._connection.wrap_api_call(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <playwright._impl._connection.Connection object at 0x7fcaa3b82750>, cb = <function Channel.send.<locals>.<lambda> at 0x7fcaa31a39c0>
is_internal = False

    async def wrap_api_call(
        self, cb: Callable[[], Any], is_internal: bool = False
    ) -> Any:
        if self._api_zone.get():
            return await cb()
        task = asyncio.current_task(self._loop)
        st: List[inspect.FrameInfo] = getattr(task, "__pw_stack__", inspect.stack())
        parsed_st = _extract_stack_trace_information_from_stack(st, is_internal)
        self._api_zone.set(parsed_st)
        try:
            return await cb()
        except Exception as error:
>           raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E           playwright._impl._errors.TimeoutError: Page.goto: Timeout 30000ms exceeded.
E           Call log:
E           navigating to "https://playwright.dev/", waiting until "load"

/root/anaconda3/lib/python3.11/site-packages/playwright/_impl/_connection.py:513: TimeoutError
___________________________________________________________ test_get_started_link[chromium] ____________________________________________________________

page = <Page url='https://playwright.dev/'>

    def test_get_started_link(page: Page):
>       page.goto("https://playwright.dev/")

test_example.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/root/anaconda3/lib/python3.11/site-packages/playwright/sync_api/_generated.py:8667: in goto
    self._sync(
/root/anaconda3/lib/python3.11/site-packages/playwright/_impl/_page.py:500: in goto
    return await self._main_frame.goto(**locals_to_params(locals()))
/root/anaconda3/lib/python3.11/site-packages/playwright/_impl/_frame.py:145: in goto
    await self._channel.send("goto", locals_to_params(locals()))
/root/anaconda3/lib/python3.11/site-packages/playwright/_impl/_connection.py:59: in send
    return await self._connection.wrap_api_call(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <playwright._impl._connection.Connection object at 0x7fcaa3b82750>, cb = <function Channel.send.<locals>.<lambda> at 0x7fcaa2f08900>
is_internal = False

    async def wrap_api_call(
        self, cb: Callable[[], Any], is_internal: bool = False
    ) -> Any:
        if self._api_zone.get():
            return await cb()
        task = asyncio.current_task(self._loop)
        st: List[inspect.FrameInfo] = getattr(task, "__pw_stack__", inspect.stack())
        parsed_st = _extract_stack_trace_information_from_stack(st, is_internal)
        self._api_zone.set(parsed_st)
        try:
            return await cb()
        except Exception as error:
>           raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E           playwright._impl._errors.TimeoutError: Page.goto: Timeout 30000ms exceeded.
E           Call log:
E           navigating to "https://playwright.dev/", waiting until "load"

/root/anaconda3/lib/python3.11/site-packages/playwright/_impl/_connection.py:513: TimeoutError
=============================================================== short test summary info ================================================================
FAILED test_example.py::test_has_title[chromium] - playwright._impl._errors.TimeoutError: Page.goto: Timeout 30000ms exceeded.
FAILED test_example.py::test_get_started_link[chromium] - playwright._impl._errors.TimeoutError: Page.goto: Timeout 30000ms exceeded.
============================================================= 2 failed in 60.97s (0:01:00) =============================================================
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/playwright_tutorial# 
```