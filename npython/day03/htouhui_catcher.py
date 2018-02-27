#! /user/bin/python
# Author xiohn.dg

import requests
import re
url = 'https://www.htouhui.com/'
regex = r'https://www.htouhui.com/'
# 抓取页面数据
res_data = requests.get(url)
html = res_data.text
html = str(html)
pattern = re.compile(regex, re.S)
contents = re.findall(pattern, html)
print(contents)
print(''.join(contents))


