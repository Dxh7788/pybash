#! /user/bin/python
# Author xiohn.dg

inu = input('请输入您的年龄:\n')
# 校验数据是否正确,测试跳过
# 格式转换
print(type(inu))
inu_int = int(inu)
print(type(inu_int))
print('您的年龄是:' + str(inu_int) + '岁.')

print(str(inu))
print(int(inu))
print(float(inu))
print(map(inu, inu))
print(tuple(inu))
print(list(inu))
print(dict([inu, inu]))

car = input('What car do you want to buy?\n')
print('Let me see if I can find you a '+car)

num_str = input('How many people to have dinner?\n')
num = int(num_str)
if num > 8:
    print('There have no empty table')
else:
    print('There have empty table')

odd_str = input('Please input a number?\n')
number = int(odd_str)
if number % 10 == 0:
    print('can be divided by 10')
else:
    print('cann\' be divided by 10')