# Locators(定位器):
- [Locators(定位器):](#locators定位器)
  - [Introduction(介绍):](#introduction介绍)
    - [Quick Guide(快速指南):](#quick-guide快速指南)

## Introduction(介绍):

Locators are the central piece of Playwright's auto-waiting and retry-ability.<br>

定位器是 Playwright 自动等待和重试功能的核心。<br>

In a nutshell, locators represent a way to find element(s) on the page at any moment.<br>

简而言之，定位器代表了一种随时在页面上找到元素的方法。<br>

### Quick Guide(快速指南):

These are the recommended built in locators. / 以下是推荐的内置定位器。<br>

| Method                   | Description                                                                            | 中文解释                                      |
|--------------------------|----------------------------------------------------------------------------------------|-------------------------------------------|
| page.get_by_role()       | to locate by explicit and implicit accessibility attributes.                           | 通过显式和隐式的可访问性属性进行定位。                    |
| page.get_by_text()       | to locate by text content.                                                             | 通过文本内容进行定位。                                 |
| page.get_by_label()      | to locate a form control by associated label's text.                                   | 通过相关标签的文本定位表单控件。                           |
| page.get_by_placeholder()| to locate an input by placeholder.                                                     | 通过占位符定位输入框。                               |
| page.get_by_alt_text()   | to locate an element, usually image, by its text alternative.                          | 通过文本替代（通常是图片）定位元素。                        |
| page.get_by_title()      | to locate an element by its title attribute.                                           | 通过标题属性定位元素。                               |
| page.get_by_test_id()    | to locate an element based on its data-testid attribute (other attributes can be configured). | 通过 data-testid 属性定位元素（可以配置其他属性）。      |
