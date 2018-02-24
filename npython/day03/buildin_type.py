#! /user/bin/python
# 内置类型
import sys
import math
"""
    5.1 真值的测试
    5.2 布尔操作- and，not，or
        not比非布尔操作符的优先级低，因此not a == b解释为not (a == b)，a == not b是一个语法错误
    5.3 比较操作
        <,<=,>,>=,==,!=,is,is not。 !=也可以写为<>,向后兼容
        所有对象都支持比较操作。它们都具有相同的优先级（高于布尔操作）。比较可以任意链接；例如，x < y < = z相当于x < y and y < = z，只是y只计算一次（但这两种情况在x < y为假时都不会计算z）
        类的非同一个实例比较时通常不相等，除非该类定义__eq__()或__cmp__()方法
    5.4  数值类型int float long complex
        浮点数还接受可带有可选前缀 "+"或"-"的字符串"nan"和"inf"来表示非数字（NaN)）和正/负无穷
    5.4.1 整数类型的位操作
        左移n等同于乘以pow(2, n)。如果结果超过普通整数的范围则返回一个长整数
        右移n位等同于除以pow(2, n)。
    5.4.2 整数类型的其它方法
        bit_length() 返回以二进制表示一个整数必须的位数，不包括符号和前导零
    5.4.3 浮点数的其它方法
        as_integer_ratio() 返回一对整数，它们的比例准确地等于浮点数的原始值，且分母为正数。无穷引发ValueError，NaNs引发OverflowError 
        is_integer() 如果浮点数实例仅有整数，则返回True，否则返回False
            >>> (-2.0).is_integer()
            True
            >>> (3.2).is_integer()
            False
        hex() 返回浮点数的十六进制字符串表示形式。对于有限的浮点数，这种表示形式总是包括一个前导的0x和尾部p及指数
        fromhex(s) 类方法，返回十六进制字符串s表示的浮点数。字符串s可以有前导和尾随空白    
    5.5 迭代器类型
        Python支持容器上迭代的概念。这种实现使用两种截然不同的方法；它们都用于允许用户定义的类支持迭代
        container.__iter__()
            返回迭代器对象。该对象必须支持如下所述的迭代器协议。如果一个容器支持不同类型的迭代，可以提供额外的方法来为这些迭代类型要求特定的迭代器。
            (对象支持多种迭代形式的一个示例是支持广度和深度优先遍历的树结构)。此方法对应于Python/C API中Python对象的类型结构的tp_iter 部分
        迭代器对象本身需要支持以下两种方法，它们组合在一起形成迭代器协议：
        iterator.__iter__()
        返回迭代器对象本身。这允许容器和迭代器都可以在for和in语句中使用。此方法对应于Python/C API中Python对象的类型结构的tp_iter slot。
        iterator.next()
        从容器中返回下一个元素。如果没有元素，引发StopIteration异常。此方法对应于Python/C API中Python对象的类型结构的tp_iternext slot。
        Python定义了几个迭代器对象以支持在通用和特定的序列类型、字典以及其他更多特殊形式上的迭代。相比迭代器协议的实现，具体的类型并不重要。
        该协议的意图是一旦迭代器的next()方法引发StopIteration，后续调用将继续这样的行为。不遵守此性质的实现被认为是有问题的。
        (此约束在Python 2.3中添加；在Python 2.2中,有多个迭代器违背了此规则)。    
    5.5.1 生成器类型
        Python的生成器提供一种方便的方法来实现迭代器协议。如果容器对象的__iter__()方法实现为一个生成器，它将自动返回一个提供__iter__()和next()方法的迭代器对象（从技术上讲，是生成器对象）。生成器的更多信息可以在yield表达式的文档中找到
    5.6 序列类型 — str, unicode, list, tuple, bytearray, buffer, xrange
        
"""
print(sys.float_info)
print(sys.int_info)

print(3/2.0)
print(3//2)
print(3+2)
print(3-2)
print(-3)
print(3 % 2)
print(3*2)
print(3**2)
print(pow(3, 2))
c = complex(3, -2)
print(c)
print(c.conjugate())
print(math.floor(4/3))
print(math.ceil(4/3))
print(round(4/3, 5))
print(math.nan)
print(math.inf)
if 3 < -math.inf:
    print(1)
if 3 is not math.nan:
    print(2)

print(int(13).bit_length())
print(float(1.5).as_integer_ratio())
print(float(1.5).hex())
print(float.fromhex('0x1.8000000000000p+0'))
print(u'123')
print(bytearray(20))

ui = 'I was a soldier'
print(ui.center(6, 'b'))
