#! /user/bin/python # 第一行是特殊注释行，称之为组织行，用来告诉GNU/Linux系统应该使用哪个解释器来执行。
# Linux/Unix等要设置字符集，Windows不用设置
# -*- coding:utf-8 -*-
# Author:xiaohong.dong


class Ko:

    @staticmethod
    def kl():
        print('静态函数被调用....')

    @classmethod
    def kc(cls):
        print('类的函数被调用....')


Ko.kl()
Ko.kc()
