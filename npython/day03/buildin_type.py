#! /user/bin/python
# 内置类型
import sys
"""
    5.1 真值的测试
    5.2 布尔操作- and，not，or
        not比非布尔操作符的优先级低，因此not a == b解释为not (a == b)，a == not b是一个语法错误
    5.3 比较操作
        <,<=,>,>=,==,!=,is,is not。 !=也可以写为<>,向后兼容
        所有对象都支持比较操作。它们都具有相同的优先级（高于布尔操作）。比较可以任意链接；例如，x < y < = z相当于x < y and y < = z，只是y只计算一次（但这两种情况在x < y为假时都不会计算z）
        类的非同一个实例比较时通常不相等，除非该类定义__eq__()或__cmp__()方法
    5.4  数值类型int float long complex
        
"""
print(sys.float_info)
print(sys.int_info)

print(3/2.0)
