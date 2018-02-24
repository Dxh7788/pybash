#!/usr/bin/python

# not比非布尔操作符的优先级低，因此not a == b解释为not (a == b)，a == not b是一个语法错误


class Truer(object):

    def __init__(self):
        print('init print ....')

    def __len__(self):
        return 0


truer = Truer()
if truer:
    print('true')
if not truer:
    print('false')
