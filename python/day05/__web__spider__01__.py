# -*- coding:utf-8 -*-
import urllib.request


page = 1
url = 'http://www.douban.com/'

# 请求
request = urllib.request.Request(url)
# 爬取结果
response = urllib.request.urlopen(request)
data = response.read()
print(data)

# 打印爬去网页的各类信息
print(type(data))
print(response.geturl())
print(response.info())
print(response.getcode())
