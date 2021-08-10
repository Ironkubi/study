<!--
 * @Descripttion: 
 * @Author: zlj
 * @Date: 2020-08-27 10:23:41
-->
# alert窗口

## 警告框
```.bash
# 警告框
alert1 = driver.find_element_by_id("bu1")

# 先点击，得先弹出警告框
alert1.click()

# 切换至警告框
alert1 = driver.switch_to.alert

# 获取alert窗口的值
print(alert1.text)

# 点击 确定
alert1.accept()

```
## 确认框
```.bash
alert2 = driver.find_element_by_id("bu2")
alert2.click()

# 切换至对话框
alert2_ = driver.switch_to.alert

# 获取窗口值
print(alert2_.text)

# 点击 取消
alert2_.dismiss()
# 点击 确认
# alert2_.accept()
```
## 对话框
```.bash
alert3 = driver.find_element_by_id("bu3")
alert3.click()

# 切换至对话框
alert3_ = driver.switch_to.alert

# 获取窗口值
print(alert3_.text)

# 输入值到对话框中
alert3_.send_keys("输入对话框")

# 点击 确认
alert2_.accept()
```
