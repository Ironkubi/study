# mock

## mock介绍

py3已将mock集成到unittest库中。简单理解：模拟接口返回参数；

## mock类

```.bash
class Mock(spec=None,side_effect=None,return_value=DEFFAULT,name=None) 

secp：定义mock对象的属性值，可以是列表，字符串，甚至一个对象或者实例 
side_effect：可以用来抛出异常或者动态改变返回值，它必须是一个iterator（列表），它会覆盖return_value
return_value：定义mock方法的返回值，它可以是一个值，可以是一个对象（如果存在side_effect参数那这个就没有用，也就是不能同时用）
name：作为mock对象的一个标识，在print时可以看到
```

## mock实际使用

### 1.未开发完成的功能如何测试？

```.bash
 1 def add(self, a, b):
 2     """两个数相加"""
 3     pass
 4 
 5 
 6 class TestSub(unittest.TestCase):
 7     """测试两个数相加用例"""
 8 
 9     def test_sub(self):
10         # 创建一个mock对象 return_value代表mock一个数据
11         mock_add = mock.Mock(return_value=15)
12         # 将mock对象赋予给被测函数
13         add = mock_add
14         # 调用被测函数
15         result = add(5, 5)
16         # 断言实际结果和预期结果
17         self.assertEqual(result, 15)

```

### 2.完成开发的功能如何测试？

```.bash
class SubClass(object):
    def add(self, a, b):
        """两个数相加"""
        return a + b


class TestSub(unittest.TestCase):
    """测试两个数相加用例"""


    def test_add2(self):
        # 初始化被测函数类实例
        sub = SubClass()
        # 创建一个mock对象 return_value代表mock一个数据
        # 传递side_effect关键字参数, 会覆盖return_value参数值, 使用真实的add方法测试
        sub.add = Mock(return_value=15, side_effect=sub.add)
        # 调用被测函数
        result = sub.add(5, 5)
        # 断言实际结果和预期结果
        self.assertEqual(result, 10)
```

### 3.存在依赖关系的功能如何测试？

```.bash
 1 # 支付类
 2 class Payment:
 3 
 4     def requestOutofSystem(self, card_num, amount):
 5         '''
 6         请求第三方外部支付接口，并返回响应码
 7         :param card_num: 卡号
 8         :param amount: 支付金额
 9         :return: 返回状态码，200 代表支付成功，500 代表支付异常失败
10         '''
11         # 第三方支付接口请求地址(故意写错)
12         url = "http://third.payment.pay/"
13         # 请求参数
14         data = {"card_num": card_num, "amount": amount}
15         response = requests.post(url, data=data)
16         # 返回状态码
17         return response.status_code
18 
19     def doPay(self, user_id, card_num, amount):
20         '''
21         支付
22         :param userId: 用户ID
23         :param card_num: 卡号
24         :param amount: 支付金额
25         :return:
26         '''
27         try:
28             # 调用第三方支付接口请求进行真实扣款
29             resp = self.requestOutofSystem(card_num, amount)
30             print('调用第三方支付接口返回结果：', resp)
31         except TimeoutError:
32             # 如果超时就重新调用一次
33             print('重试一次')
34             resp = self.requestOutofSystem(card_num, amount)
35 
36         if resp == 200:
37             # 返回第三方支付成功，则进行系统里面的扣款并记录支付记录等操作
38             print("{0}支付{1}成功！！！进行扣款并记录支付记录".format(user_id, amount))
39             return 'success'
40 
41         elif resp == 500:
42             # 返回第三方支付失败，则不进行扣款
43             print("{0}支付{1}失败！！不进行扣款！！！".format(user_id, amount))
44             return 'fail'
45 
46 # 单元测试类
47 class payTest(unittest.TestCase):
48 
49     def test_pay_success(self):
50         pay = Payment()
51         # 模拟第三方支付接口返回200
52         pay.requestOutofSystem = mock.Mock(return_value=200)
53         resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
54         self.assertEqual('success', resp)
55 
56     def test_pay_fail(self):
57         pay = Payment()
58         # 模拟第三方支付接口返回500
59         pay.requestOutofSystem = mock.Mock(return_value=500)
60         resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
61         self.assertEqual('fail', resp)
62 
63     def test_pay_time_success(self):
64         pay = Payment()
65         # 模拟第三方支付接口首次支付超时,重试第二次成功
66         pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 200])
67         resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
68         self.assertEqual('success', resp)
69 
70     def test_pay_time_fail(self):
71         pay = Payment()
72         # 模拟第三方支付接口首次支付超时,重试第二次失败
73         pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 500])
74         resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
75         self.assertEqual('fail', resp)


```


## mock装饰器

1.@patch('module名字.方法名') 

2.@patch.object(类名, '方法名') 
```.bash
 1 # 装饰类演示
 2 from mock import Mock, patch
 3 
 4 
 5 # 单独的相乘函数
 6 def multiple(a, b):
 7     return a * b
 8 
 9 
10 # 单独的捕获Exception函数
11 def is_error():
12     try:
13         os.mkdir("11")
14         return False
15     except Exception as e:
16         return True
17 
18 
19 # 计算类,包含add方法
20 class calculator(object):
21     def add(self, a, b):
22         return a + b
23 
24 
25 # 装饰类演示 - 单元测试类
26 class TestProducer(unittest.TestCase):
27 
28     # case执行前
29     def setUp(self):
30         self.calculator = calculator()
31 
32     # mock一个函数,注意也要指定module
33     @patch('mock_learn.multiple')
34     def test_multiple(self, mock_multiple):
35         mock_multiple.return_value = 3
36         self.assertEqual(multiple(8, 14), 3)
37 
38     # mock一个类对象的方法
39     @patch.object(calculator, 'add')
40     def test_add(self, mock_add):
41         mock_add.return_value = 3
42         self.assertEqual(self.calculator.add(8, 14), 3)
43 
44     # mock调用方法返回多个不同的值
45     @patch.object(calculator, 'add')
46     def test_effect(self, mock_add):
47         mock_add.side_effect = [1, 2, 3]
48         self.assertEqual(self.calculator.add(8, 14), 1)
49         self.assertEqual(self.calculator.add(8, 14), 2)
50         self.assertEqual(self.calculator.add(8, 14), 3)
51 
52     # mock的函数抛出Exception
53     @patch('os.mkdir')
54     def test_exception(self, mkdir):
55         mkdir.side_effect = Exception
56         self.assertEqual(is_error(), True)
57 
58     # mock多个函数,注意函数调用顺序
59     @patch.object(calculator, 'add')
60     @patch('mock_learn.multiple')
61     def test_more(self, mock_multiple, mock_add):
62         mock_add.return_value = 1
63         mock_multiple.return_value = 4
64         self.assertEqual(self.calculator.add(3, 3), 1)
65         self.assertEqual(multiple(3, 3), 4)

```