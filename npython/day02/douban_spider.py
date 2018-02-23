#! /user/bin/python # 第一行是特殊注释行，称之为组织行，用来告诉GNU/Linux系统应该使用哪个解释器来执行。
# Linux/Unix等要设置字符集，Windows不用设置
# -*- coding:utf-8 -*-
# Author:xiaohong.dong
import requests
from bs4 import BeautifulSoup
import re

print('开始抓取豆瓣top250影评....')
for page in range(10):
    url = 'https://movie.douban.com/top250?start='+str(page*25)+'&filter='
    print('正在爬取第'+str(page+1)+'页...')

    # 获取源代码
    html = requests.get(url)
    # 解析源代码
    print('解析数据....')
    try:
        soup = BeautifulSoup(html.text, 'html.parser')
        soup = str(soup)  # 将网页文本转换成字符串
        title = re.compile(r'<span class="title">(.*)</span>')  # 该函数根据包含的正则表达式创建模式对象
        names = re.findall(title, soup)
        for name in names:
            if name.find('/') == -1:  # 剔除英文名称(英文名特征是含有反斜杠)
                print(name)
    except Exception as e:
        print(e)

    print('\n\n电影影评抓取成功...')
