# 类名的规范是驼峰标识,单行注释要用一个#来表示,类名前要空两行,空行不能多也不能少
# python的函数与函数之间要有一个空行,这是默认的规范.
# python使用self来表示当前实例,其他语言常用this,比如C++或者Java
# python中如果使用__开头并且以__结尾,比如__init__那么该方法属于预先定义的方法,自定义的方法不使用此类命名方式
# python的函数必须要有一个参数,如果没有自定义参数,应当使用self作为参数,如sanhello(self);如果有自定义参数,可不加self参数
# python的函数命名不能使用驼峰标识,而是全部使用小写格式
"""
python类的声明:
    python类的声明方式参照其他语言的命名方式.
    类中可以声明成员变量和成员函数.
    除类名能用驼峰命名外,函数参数以及函数名都要规范使用小写命名.
    函数参数之间应当在参数头加一个空格
"""

__all__ = ["DemoClass"]


class DemoClass:
    empCount = 0
    name = ""
    salary = 0.00
    # 声明函数,函数前要空一行

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.empCount += 1

    def say_hello(self):
        print(self.name)

    def book(self):
        print()


class DemoClassB:
    empCount = 0

    def __int__(self, empcount):
        self.empCount = empcount