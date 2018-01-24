print("hello,world")
word = '单引号字符串'
sentence = "双引号字符串"
brBlock = '''这是一个字符串块:
             我换行了'''
if True:
    print(word)
if not False:
    print(sentence)
print(brBlock)
print("hello,world")
print("this"" is"" a" " string")

dataIn = input("\n\n按下 enter 键后退出。")
print(dataIn)

#缩进相同的一组语句构成一个代码块，我们称之代码组。
#像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
#我们将首行及后面的代码组称为一个子句(clause)。
#如下实例：
expression = True

if expression:
    print("1")
elif expression:
    print("2")
else:
    print("3")