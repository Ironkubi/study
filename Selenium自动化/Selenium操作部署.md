  ## Selenium
   > 显式等待和隐式等待:  
     显式等待就是有条件的等待   
     隐式等待就是无条件的等待   
     显式等待：  

   > 设置等待时间    
      WebDriverWait(driver, 3, 0.5) #传入三个参数，第一个是浏览器驱动，第二个是等待多少秒，第三个是每隔多少秒监控一次  
      原理：指定一个等待条件，和一个最长等待时间，程序会判断在等待时间内条件是否满足，如果满足则返回，如果不满足会继续等待，超过时间就会抛出异常  
   
   > 隐式等待：  
      browser.implicitly_wait(10) #直接等待10秒钟   
      当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0    
   
   > 分布式运行  
   java -Dwebdriver.chrome.driver="chromedriver.exe" -jar selenium-server-standalone-3.9.1.jar -role node -hub "http://10.224.70.158:8888/grid/register/" -port 5558 -browser "browserName=chrome,maxInstances=2,version=65,platform=WINDOWS"  
   java -Dwebdriver.firefox.driver="geckodriver.exe" -jar selenium-server-standalone-3.9.1.jar -role node -hub "http://10.224.70.158:8888/grid/register" -port 5558  -browser "browserName=firefox,maxInstances=2,version=56,platform=WINDOWS"  

