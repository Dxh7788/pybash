#! /user/bin/python
# Author:xiaohong.dong
# Date: 2018-02-24 16:08:00
a = bytearray('aaaaa', 'utf-8')
m = memoryview(a)
print(m.tobytes())

