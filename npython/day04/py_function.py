#! /user/bin/python
# Author:xo.h_dong

"""
    8.1.2 实参和形参
        注意:  大家有时候会形参、实参部分,因此如果你看到有人将函数定义中的变量称为实参或将函数调用中的变量称为形参,不要大惊小怪
    8.2 传递实参
        8.2.1  位置实参
        位置实参的顺序很重要,不按顺序会产生难以控制的结果.
        8.2.2  关键字实参
        def pu(jk_name, jk_desc):
            print(jk_name+jk_desc)
        # 关键字实参
        pu('12', '32')
        pu(jk_name='32', jk_desc='12')
        pu(jk_desc='32', jk_name='12')
        8.2.3  默认值
        使用默认值时,在形参列表中必须先列出没有默认值的形参,再列出有默认值的实参.这让python依然能够正确解读位置实参.
        8.2.4  等效的函数调用
        多种传递参数方式混合使用.
    8.3  返回值
        8.3.1  返回简单值
        8.3.2  让实参变成可选的

"""


def pu(jk_name, jk_desc):
    print(jk_name+jk_desc)

# 关键字实参

pu('12', '32')
pu(jk_name='32', jk_desc='12')
pu(jk_desc='32', jk_name='12')

# 默认值


def pu0(jk_name, jk_desc='dog'):
    print(jk_name+jk_desc)

pu0('123')


def pu0(jk_name, jk_desc, jk_title=''):
    print(jk_name+jk_title+jk_desc)






