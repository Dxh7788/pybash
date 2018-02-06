# -*- coding:utf-8 -*-
# author:xd.d

import urllib.request


def savefile(data):
    path = "E:\\pyh\\spider\\douban_01.out"
    f = open(path, 'wb')
    f.write(data)
    f.close()

# 网址


url = "https://www.douban.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/59.0.3071.86 Safari/537.36'}
req = urllib.request.Request(url, headers)
resp = urllib.request.urlopen(req)
data = resp.read()

# 结果保存到文件
# savefile(data)
data = data.decode('utf-8')
print(data)

# 打印爬去网页的各类信息
print(type(data))
print(resp.geturl())
print(resp.info())
print(resp.getcode())
