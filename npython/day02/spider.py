#! /user/bin/python # 第一行是特殊注释行，称之为组织行，用来告诉GNU/Linux系统应该使用哪个解释器来执行。
# Linux/Unix等要设置字符集，Windows不用设置
# -*- coding:utf-8 -*-
# FileName:spider.py
# Author:xiaohong.dong

# python中称之为导入模块,java中叫导包

from urllib import request  # 导入网页操作的模块
url = "http://youku.com"
resource = request.urlopen(url)  # 用模块打开一个网页获取一个网页对象
html = resource.read()  # read将网页对象转换成字符串

fn = open('youku.html', 'w+b')  # 创建一个文件,w代表写，r代表读，b代表二进制
fn.write(html)  # 写入匹配到的字符串
fn.close()  # 写完后关闭文件
print('执行完毕')

# python的主方法
if __name__ == '__main__':

    print(html)
    # 通过URL获取网站的源代码
    # 将获取的源代码下载到本地的文件中
