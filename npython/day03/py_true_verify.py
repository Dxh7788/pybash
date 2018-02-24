#!/usr/bin/python


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
