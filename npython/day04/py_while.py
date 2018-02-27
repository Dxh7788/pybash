#! /user/bin/python
# Author xiohn.dg
message = input('请输入控制命令:')
while message != 'quit':
    message = input('请输入命令')
    print('We will add'+message+' this material in pizza')

age = input('Please tell me your age!')
while age != 'quit':
    age_num = int(age)
    if age_num < 3:
        print('You are free to play movie')
    if 3 <= age_num <= 12:
        print('Your price is $10.')
    if age_num > 12:
        print('your price is $15'.capitalize())
    age = input('Please tell me your age!')