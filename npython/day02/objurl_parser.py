#! /user/bin/python # 第一行是特殊注释行，称之为组织行，用来告诉GNU/Linux系统应该使用哪个解释器来执行。
# Linux/Unix等要设置字符集，Windows不用设置
# -*- coding:utf-8 -*-
# Author:xiaohong.dong

copyright()
license()
credits()
abs()
divmod()
input()
open()
staticmethod()
all()
enumerate()
int()
ord()
str()
any()
eval()
isinstance()
pow()
sum()
issubclass()
print()
super()
bin()
iter()
property()
tuple()
bool()
filter()
len()
range()
type()
bytearray()
float()
list()
input()
callable()
format()
locals()
chr()
frozenset()
vars()
classmethod()
getattr()
map()
repr()
globals()
max()
reversed()
zip()
compile()
hasattr()
memoryview()
round()
__import__()
complex()
hash()
min()
set()
delattr()
help()
next()
setattr()
dict()
hex()
object()
slice()
dir()
id()
oct()
sorted()
# intern()，已经转移到sys模块
# coerce(),Python3中已经被移除corece内置函数和__coerce__方法的支持
# buffer(),Python2的内函数buffer在Python3中被memoryview类替换，
# 它们并不是完全兼容，所以2to3并没有改变这个函数，除非你明确指定缓冲存储修改器（buffer fixer）

# apply(),apply 是 pandas 库的一个很重要的函数
# xrange(),python3　里，range()返回迭代器，xrange()不再存在
# cmp(),python 3.4.3 的版本中已经没有cmp函数，被operator模块代替，在交互模式下使用时，需要导入模块
# long(),在Python 3里，由于长整型已经不存在了，自然原来的long()函数也没有了。为了强制转换一个变量到整型，可以使用int()函数
# reload(),Python 3.0把reload内置函数移到了imp标准库模块中
# reduce()，在python3里，reduce()函数已经从全局名字空间移除，现在被放置在fucntools模块里
# unicode(),python２有两个全局函数可以把对象强制转换成字符串:unicode()把对象转换成unicode字符串，还有str()把对象转换为非Unicode字符串。
# Python3只有一种字符串类型，unicode字符串，所以str()函数即可完成所有的功能
# unichr(),在python3.0只用chr()就可以了。在python2.6用chr()和unichr()
# basestring(),python3舍弃了该函数，所以该函数不能在python3中使用
# execfile()python3 删去了 execfile()，代替方法如下：
'''
with open('test1.py','r') as f:
    exec(f.read())
'''
