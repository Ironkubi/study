# 自动化测试框架unittest与pytest的区别？
  
 **一、用例编写规则(用例管理)**
   
   > 1、unittest提供了test cases、test suites、test fixtures、test runner相关的类,让测试更加明确、方便、可控。使用unittest编写用例,必须遵守以下规则:  
    （1）测试文件必须先import unittest  
    （2）测试类必须继承unittest.TestCase  
    （3）测试方法必须以“test_”开头  
    （4）测试类必须要有unittest.main()方法  

   > 2、pytest是python的第三方测试框架,是基于unittest的扩展框架,比unittest更简洁,更高效。使用pytest编写用例,必须遵守以下规则:  
    （1）测试文件名必须以“test_”开头或者"_test"结尾(如:test_ab.py)   
    （2）测试方法必须以“test_”开头。  
    （3）测试类命名以"Test"开头。  

   > 总结:
    pytest可以执行unittest风格的测试用例,无须修改unittest用例的任何代码,有较好的兼容性。 pytest插件丰富,比如flask插件,可用于用例出错重跑;还有xdist插件,可用于设备并行执行。  


 **二、用例前置和后置**
  
   > 1、unittest提供了setUp/tearDown，每个用例运行前、结束后运行一次。setUpClass和tearDownClass，用例执行前、结束后，只运行一次。  
   
   > 2、pytest提供了模块级、函数级、类极、方法级的setup/teardown，比unittest的setup/tearDown更灵活      
    1) 模块级（setup_module/teardown_module）开始于模块始末，全局的     
    2) 函数级（setup_function/teardown_function）只对函数用例生效（不在类中）   
    3) 类级（setup_class/teardown_class）只在类中前后运行一次(在类中)    
    4) 方法级（setup_method/teardown_method）开始于方法始末(在类中)   
    5) 类里面的（setup/teardown）运行在调用方法的前后  

   > 3、pytest还可以在函数前加@pytest.fixture()装饰器，在测试用例中装在fixture函数。fixture的使用范围可以是function,module,class,session。  
    firture相对于setup和teardown来说有以下几点优势：  
    1) 命名方式灵活，不局限于setup和teardown这几个命名    
    2) conftest.py 配置里可以实现数据共享，不需要import就能自动找到一些配置，可供多个py文件调用   
    3) scope="module" 可以实现多个.py跨文件共享前置  
    4) scope="session" 以实现多个.py跨文件使用一个session来完成多个用例  
    5) 用yield来唤醒teardown的执行  
    
 **三、断言**
  
   > 1.unittest提供了assertEqual、assertIn、assertTrue、assertFalse。  
   > 2.pytest直接使用assert 表达式。  

 **四、报告**
  
   > 1.unittest使用HTMLTestRunnerNew库。   
   > 2.pytest有pytest-HTML、allure插件。  

 **五、失败重跑**
  
   > 1、unittest无此功能。  
   > 2、pytest支持用例执行失败重跑，pytest-rerunfailures插件。  

 **六、参数化**
  
   > 1、unittest需依赖ddt库；  
   > 2、pytest直接使用@pytest.mark.parametrize装饰器。  

 **七、用例分类执行**
  
   > 1、unittest默认执行全部用例，也可以通过加载testsuit，执行部分用例；  
   > 2、pytest可以通过@pytest.mark来标记类和方法，pytest.main加入参数("-m")可以只运行标记的类和方法   
