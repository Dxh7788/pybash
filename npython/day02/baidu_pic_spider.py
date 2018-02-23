#! /user/bin/python # 第一行是特殊注释行，称之为组织行，用来告诉GNU/Linux系统应该使用哪个解释器来执行。
# Linux/Unix等要设置字符集，Windows不用设置
# -*- coding:utf-8 -*-
# Author:xiaohong.dong

import requests
import re
import random
url = ''

if __name__ == '__main__':
    url = ('http://image.baidu.com/search/index?tn=baiduimage'
           '&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1'
           '&fmq=1519364542656_R&pv=&ic=0&nc=1&z=&se=1&showtab=0'
           '&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=冲田杏梨')

    html = requests.get(url)
    print('解析冲田杏梨的图片....')
    try:
        for addr in re.findall('"objURL":"(.*?)"', html.text, re.S):
            pics = requests.get(addr)
            fb = open('E:\\data2\\img\\' + (str(random.randrange(0, 1000, 4))) + '.jpg', "wb")
            fb.write(pics.content)
            fb.close()
    except Exception as e:
        print(e)
