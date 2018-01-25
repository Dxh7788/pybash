# python循环的spider学习
# 循环语句需要使用冒号


def __for__circle__letter__():
    for letter in "book":
        print("current letter", letter)


__for__circle__letter__()

ls = ["da", "ds", "dd", "df"]


def __for__circle__list__():
    for ele in ls:
        print("current element in list ls ", ele)


__for__circle__list__()

letter = "abcde"


def __for__circle__by__index():
    for index in range(len(letter)):
        print("current index is ", index, ",current letter is ", letter[index])


__for__circle__by__index()


# for...else...
def __for__circle__else__():
    for index in range(len(letter)):
        for index2 in range(0,index):
           print("current index is ", index, ",current letter is ", letter[index])
    else:
        print("else")


__for__circle__else__()
# while...else...
count = 0


def __while__circle__else__():
    while(count<9):

        count = count+1

        if(count<7):
            count = count+1
            print("the count value is ", count)
    else:
        print("while's else logical")


__while__circle__else__

