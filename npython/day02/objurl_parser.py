#! /user/bin/python # 第一行是特殊注释行，称之为组织行，用来告诉GNU/Linux系统应该使用哪个解释器来执行。
# Linux/Unix等要设置字符集，Windows不用设置
# -*- coding:utf-8 -*-
# Author:xiaohong.dong

copyright()
license()
credits()
abs()  # 求绝对值
divmod()  # 求模
input()  # 控制台输入值
open()  # 内置函数,打开文件.
staticmethod()  # python staticmethod 返回函数的静态方法
all()  # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False。
enumerate()  # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
int()  # int() 函数用于将一个字符串或数字转换为整型
ord()  # ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，
# 返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常
str()  # str() 函数将对象转化为适于人阅读的形式
any()  # any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True
eval()  # eval() 函数用来执行一个字符串表达式，并返回表达式的值
isinstance()  # isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
pow()  # pow() 方法返回 xy（x的y次方） 的值
sum()  # sum() 方法对系列进行求和计算
issubclass()  # issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类
print()  # print() 方法用于打印输出，最常见的一个函数
super()
bin()  # bin() 返回一个整数 int 或者长整数 long int 的二进制表示
iter()  # iter() 函数用来生成迭代器
property()  # property() 函数的作用是在新式类中返回属性值
tuple()  # Python 元组 tuple() 函数将列表转换为元组
bool()  # bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。bool 是 int 的子类
filter()  # filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中
len()  # Python len() 方法返回对象（字符、列表、元组等）长度或项目个数
range()  # python range() 函数可创建一个整数列表，一般用在 for 循环中
type()  # type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象
bytearray()  # bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256
float()  # float() 函数用于将整数和字符串转换成浮点数
list()  # list() 方法用于将元组转换为列表
input()  # python input()用来获取控制台的输入。input() 将所有输入作为字符串看待，返回字符串类型
callable()  # callable()函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；但如果返回False，调用对象object绝对不会成功
format()  # 新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。基本语法是通过 {} 和 : 来代替以前的 %
locals()  # locals() 函数会以字典类型返回当前位置的全部局部变量
chr()  # chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
frozenset()  # frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素
vars()  # vars() 函数返回对象object的属性和属性值的字典对象
classmethod()  # classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的
# cls 参数，可以来调用类的属性，类的方法，实例化对象等。
getattr()  # getattr() 函数用于返回一个对象属性值
map()  # map() 会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
repr()  # repr() 函数将对象转化为供解释器读取的形式
globals()  # globals() 函数会以字典类型返回当前位置的全部全局变量
max()
reversed()
zip()  # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表
compile()  # compile() 函数将一个字符串编译为字节代码
hasattr()  # hasattr() 函数用于判断对象是否包含对应的属性
memoryview()  # memoryview() 函数返回给定参数的内存查看对象(Momory view)。
# 所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问
round()  # round() 方法返回浮点数x的四舍五入值
__import__()  # __import__() 函数用于动态加载类和函数。如果一个模块经常变化就可以使用 __import__() 来动态载入
complex()
hash()
min()  # min() 方法返回给定参数的最小值，参数可以为序列
set()
delattr()  # delattr 函数用于删除属性。
help()  # help() 函数用于查看函数或模块用途的详细说明。
next()  # next() 返回迭代器的下一个项目
setattr()
dict()
hex()  # hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
object()
slice()  # slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
dir()
id()  # id() 函数用于获取对象的内存地址
oct()  # oct() 函数将一个整数转换成8进制字符串
sorted()  # sorted() 函数对所有可迭代的对象进行排序操作。
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
