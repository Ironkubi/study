<!--
 * @Descripttion: 
 * @Author: zlj
 * @Date: 2020-04-08 10:36:14
-->
# selenium使用

## 行为链

有时候页面操作可能需要很多步，可以使用鼠标的行为链来完成
```bash
from selenium.webdriver import ActionChains
 input_tag = driver.find_element_by_id('kw')
 submit_tag = driver.find_element_by_id('su')

actions= ActionChains(driver)
action.move_to_element(input_tag).perform()  #移动元素
action.send_keys_to_element(input_tag,'onion')
action.move_to_element(submit_tag)
action.click(submit_tag)
action.perform()


action.click_and_hold(element).perform() 点击但不松开鼠标
action.context_click(element).perform() 右键点击
action.double_click(element).perform()  双击 
action.click_and_hold(login_btn).perform() 长按
```

### 将 ac1 拖拽到 ac2 位置

```bash
ac1 = driver.find_element_by_xpath('elementD')
ac2 = driver.find_element_by_xpath('elementE')
ActionChains(driver).drag_and_drop(ac1, ac2).perform()
```

## cookie 操作

```bash
1. 获取所有的cookie
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])

2.删除cookie
# By name
driver.delete_cookie("CookieName")

# all
driver.delete_all_cookies()

3.根据cookie的key 获取value

value =driver.get_cookie(key)
```

