# 页面操作Action

## 最常用的Action

| Action                       | Description                     |
|------------------------------|----------------------------------|
| locator.check()              | 选中输入复选框                    |
| locator.click()              | 点击元素                         |
| locator.uncheck()            | 取消选中输入复选框                |
| locator.hover()              | 将鼠标悬停在元素上               |
| locator.fill()               | 填写表单字段，输入文本           |
| locator.focus()              | 聚焦到元素                      |
| locator.press()              | 按单个按键                      |
| locator.set_input_files()    | 选择文件上传                    |
| locator.select_option()      | 在下拉列表中选择选项             |


| Assertion                           | Description            |
|-------------------------------------|------------------------|
| expect(locator).to_be_checked()     | 复选框已选中            |
| expect(locator).to_be_enabled()     | 控件已启用              |
| expect(locator).to_be_visible()     | 元素可见                |
| expect(locator).to_contain_text()   | 元素包含文本            |
| expect(locator).to_have_attribute() | 元素具有属性            |
| expect(locator).to_have_count()     | 元素列表具有给定长度    |
| expect(locator).to_have_text()      | 元素匹配文本            |
| expect(locator).to_have_value()     | 输入元素具有值          |
| expect(page).to_have_title()        | 页面具有标题            |
| expect(page).to_have_url()          | 页面具有URL             |
