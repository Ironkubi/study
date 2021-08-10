  ## Appium 
    
   > 1、列出手机装的所有app的包名：   
     adb shell pm list packages  

   > 列出系统应用的所有包名：   
     adb shell pm list packages -s  

   > 列出除了系统应用的第三方应用包名：  
     adb shell pm list packages -3                 
     aapt dump badging xxx.apk(安装包名称)  
  
   > appium中的定位表达式，继承了selenium中的八大定位表达式  
     通过resrouce-id来定位  
     find_element_by_id("com.taobao.taobao:id/textview_goods_title")  
     通过ClassName定位(class)  
     find_element_by_class_name("android.widget.CheckBox")  
     通过AccessibilityId定位(content-desc)  
     find_element_by_accessibility_id("勾选宝贝")  
     