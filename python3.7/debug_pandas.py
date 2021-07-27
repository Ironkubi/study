# -*-coding:utf-8 -*-
# File : debug_pandas.py
# @Time : 2021/5/26 18:20
# @Author : Sf
# version : python 3.7.8

"""
一、 创建数据
import pandas as pd
import numpy as np

# 一、 创建数据
ipl_data = {'国家': ['中国', '美国', '韩国', '韩国', '日本','日本', '中国', '中国'],
         '职业': ['老师', '商人', '运动员', '运动员', '医生', '老师','律师','客服'],
         '年龄': [28, 27, 29, 30, 27, 35,28 ,28],
         '体重': [54, 60, 70, 65, 55, 50, 52, 47],
         '身高': [165, 170, 168, 168, 180, 175, 172, 160],
         '性别':['男', '男', '女', '男', '女', '男', '男', '女']}
df = pd.DataFrame(ipl_data)
print(df)
   体重  国家  年龄 性别   职业   身高
0  54  中国  28  男   老师  165
1  60  美国  27  男   商人  170
2  70  韩国  29  女  运动员  168
3  65  韩国  30  男  运动员  168
4  55  日本  27  女   医生  180
5  50  日本  35  男   老师  175
6  52  中国  28  男   律师  172
7  47  中国  28  女   客服  160
二、读取数据
filepath = 'dataset.csv'
df = pd.read_csv(filepath)
# pd.read_excel(filepath
# pd.read_json(filepath)
三、保存数据
filepath = 'dataset.csv'
df.to_csv(filepath)
# df.to_excel(filepath)
四、查看数据
1. 查看头部数据
print(df.head(3))  # 查看头3行数据
print(df.tail(3)) # 查看后3行数据
   体重  国家  年龄 性别   职业   身高
0  54  中国  28  男   老师  165
1  60  美国  27  男   商人  170
2  70  韩国  29  女  运动员  168

   体重  国家  年龄 性别  职业   身高
5  50  日本  35  男  老师  175
6  52  中国  28  男  律师  172
2. 格式查看
print(df.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8 entries, 0 to 7
Data columns (total 6 columns):
体重    8 non-null int64
国家    8 non-null object
年龄    8 non-null int64
性别    8 non-null object
职业    8 non-null object
身高    8 non-null int64
dtypes: int64(3), object(3)
memory usage: 464.0+ bytes
None
3. 查看统计信息(这个操作只针对数值型的列)
print(df.describe())
              体重         年龄          身高
count   8.000000   8.000000    8.000000
mean   56.625000  29.000000  169.750000
std     7.818248   2.618615    6.112049
min    47.000000  27.000000  160.000000
25%    51.500000  27.750000  167.250000
50%    54.500000  28.000000  169.000000
75%    61.250000  29.250000  172.750000
max    70.000000  35.000000  180.000000
五、基本处理
1. 增
df['爱好'] = ['运动', '看书', '旅行', '旅行', '拍照', '唱歌', '画画', '唱歌']
print(df)
   体重  国家  年龄 性别   职业   身高  爱好
0  54  中国  28  男   老师  165  运动
1  60  美国  27  男   商人  170  看书
2  70  韩国  29  女  运动员  168  旅行
3  65  韩国  30  男  运动员  168  旅行
4  55  日本  27  女   医生  180  拍照
5  50  日本  35  男   老师  175  唱歌
6  52  中国  28  男   律师  172  画画
7  47  中国  28  女   客服  160  唱歌
2. 删
df.drop(['身高', '体重'], axis=1, inplace=True)
print(df)
   国家  年龄 性别   职业
0  中国  28  男   老师
1  美国  27  男   商人
2  韩国  29  女  运动员
3  韩国  30  男  运动员
4  日本  27  女   医生
5  日本  35  男   老师
6  中国  28  男   律师
7  中国  28  女   客服
3. 选
df1 = df[['国家', '年龄']]
print(df1)
   国家  年龄
0  中国  28
1  美国  27
2  韩国  29
3  韩国  30
4  日本  27
5  日本  35
6  中国  28
7  中国  28
4. 改
# ACCESSOR,可以将它理解为一种属性接口，通过它可以获得额外的方法
print(pd.Series._accessors)
print([i for i in dir(pd.Series.str) if not i.startswith('_')])
df['国家'].str.replace('美', '英')
print(df)
{'str', 'cat', 'dt'}
['capitalize', 'cat', 'center', 'contains', 'count', 'decode', 'encode', 'endswith', 'extract', 'extractall', 'find', 'findall', 'get', 'get_dummies', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace', 'istitle', 'isupper', 'join', 'len', 'ljust', 'lower', 'lstrip', 'match', 'normalize', 'pad', 'partition', 'repeat', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'slice', 'slice_replace', 'split', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'wrap', 'zfill']
   体重  国家  年龄 性别   职业   身高
0  54  中国  28  男   老师  165
1  60  英国  27  男   商人  170
2  70  韩国  29  女  运动员  168
3  65  韩国  30  男  运动员  168
4  55  日本  27  女   医生  180
5  50  日本  35  男   老师  175
6  52  中国  28  男   律师  172
7  47  中国  28  女   客服  160
5. 单(多)列运算
df['年龄'] = df['年龄'] + 10
df['年龄乘体重'] = df['年龄'] * df['体重']
df['年龄乘以2'] = df['年龄'].map(lambda x: x*2)
df['col3'] = df.apply(lambda x: x['col1'] + 2 * x['col2'], axis=1) 
print(df)
   体重  国家  年龄 性别   职业   身高  年龄乘体重
0  54  中国  38  男   老师  165   2052
1  60  美国  37  男   商人  170   2220
2  70  韩国  39  女  运动员  168   2730
3  65  韩国  40  男  运动员  168   2600
4  55  日本  37  女   医生  180   2035
5  50  日本  45  男   老师  175   2250
6  52  中国  38  男   律师  172   1976
7  47  中国  38  女   客服  160   1786
六、重复数据
6.2 判断某列是否重复
flag = df['国家'].duplicated()
df['is_repeat'] = flag
print(df[['国家', 'is_repeat']])
   国家  is_repeat
0  中国      False
1  美国      False
2  韩国      False
3  韩国       True
4  日本      False
5  日本       True
6  中国       True
7  中国       True
6.3 判断dataframe数据整行是否重复
flag = df.duplicated()
df['is_repeat'] = flag
print(df)
   体重  国家  年龄 性别   职业   身高  is_repeat
0  54  中国  28  男   老师  165      False
1  60  美国  27  男   商人  170      False
2  70  韩国  29  女  运动员  168      False
3  65  韩国  30  男  运动员  168      False
4  55  日本  27  女   医生  180      False
5  50  日本  35  男   老师  175      False
6  52  中国  28  男   律师  172      False
7  47  中国  28  女   客服  160      False
6.4 判断dataframe数据多列数据是否重复(多列组合查)
flag = df.duplicated(subset = ['国家', '性别'])
df['is_repeat'] = flag
print(df)
   体重  国家  年龄 性别   职业   身高  is_repeat
0  54  中国  28  男   老师  165      False
1  60  美国  27  男   商人  170      False
2  70  韩国  29  女  运动员  168      False
3  65  韩国  30  男  运动员  168      False
4  55  日本  27  女   医生  180      False
5  50  日本  35  男   老师  175      False
6  52  中国  28  男   律师  172       True
7  47  中国  28  女   客服  160      False
6.5 去重

# DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)

df.drop_duplicates(subset = ['国家', '性别'], keep='last', inplace=True)
print(df)
# drop_duplicats参数说明：
#   参数subset
#     subset用来指定特定的列，默认所有列
#   参数keep
#     keep可以为first和last，表示是选择最前一项还是最后一项保留，默认first
#   参数inplace
#     inplace是直接在原来数据上修改还是保留一个副本，默认为False
根据['国家', '性别']进行去重，行索引为0的数据被删除了，保留了行索引为7的数据

   体重  国家  年龄 性别   职业   身高
1  60  美国  27  男   商人  170
2  70  韩国  29  女  运动员  168
3  65  韩国  30  男  运动员  168
4  55  日本  27  女   医生  180
5  50  日本  35  男   老师  175
6  52  中国  28  男   律师  172
7  47  中国  28  女   客服  160
"""""

