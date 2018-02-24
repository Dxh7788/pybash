#! /user/bin/python
# Author:xiaohong.dong
# Date: 2018-02-24 13:44:00

truer = 'this is a testify Sentence'
# 查找函数find(self, sub, start, end),从[start,end]处查找子字符串sub在str中出现的首次索引值
print(truer.find('is'))
# 标题函数str.title(),首字母变成大写
print(truer.title())
# count(self, x, start, end) 从str的[start, end]区间查找子字符串x出现的次数
print(truer.count('is'))
# join(self, iterable[str]) 将iterable[str]的元素拼接成一个连续字符串
# join相当于循环读取序列类型中的值然后拼接到一起,只有str的序列类型才支持
# Return a string which is the concatenation of the strings in the iterable.  The separator between elements is S
pl = ['a', 'b', 'c', 'd']
pt = ('a', 'b', 'c', 'v')
pm = {'a': '1', 'b': '2'}
print(''.join(pl))
print(''.join(pt))
print(''.join(pm))
# Return the lowest index in S where substring sub is found,
# such that sub is contained within S[start:end].
# Optional arguments start and end are interpreted as in slice notation
# str中的子字符串的最小索引,这个方法和find()一样,它们的区别是find()如果失败会返回-1,而index()会抛出ValueError异常
print(truer.index('is', 3, truer.__len__()))
# capitalize()首字母大写,其他单词的首字母全部小写.
print(truer.capitalize())
# encode(self, encode, error)字符编码转换,error默认是strict.
# 也可以是ignore和replace,ignore是如果转码失败则不展示,replace是如果转码失败则展示乱码
print('中文'.encode('gbk'))
print('中文'.encode('gb2312'))
print('中文'.encode('utf-8'))
# S.decode(self, encode, error),error默认是strict,也可以是ignore和replace,ignore是如果转码失败则不展示,replace是如果转码失败则展示乱码
print(b'\xd6\xd0\xce\xc4'.decode('gbk'))
print(b'\xd6\xd0\xce\xc4'.decode('utf-8', 'replace'))
# S.endswith(self, suffix, start=None, end=None),判断S是否以suffix结束.开始位置为start,结束位置为end
print(truer.endswith('ce'))
# S.expandtabs(self,tabsize=8),替换制表符为空格或多个空格
print("\t1\t2\t3\t4".expandtabs())
# S.format(self, *args, **kwargs)
print('I\'m {0},He\'s {1},She\'s {2}'.format(0, 1, 2))
# S.format_map(self,map)暂留 TODO
# print('{0}'.format_map(map(lambda x: x**2, [1, 2])))
# S.isalnum(self)是否是数字
print('1'.isalnum())
# S.isalpha(self),S中是否全部是字符
print('ab'.isalpha())
# S.isdecimal(self)如果S中只有十进制字符，则返回True，否则返回False。十进制字符包括数字字符和所有可用于构成十进制基数数字的字符，例如U+0660表示阿拉伯-印度文数字的零
print(truer.isdecimal())
# S.isdigit(self)是否全部是数字
print('1232'.isdigit())
# S.isidentifier(self)是否是有效的标识符(变量名).'*a'不是有效的标识符,而ab是有效的标识符.
print('*a'.isidentifier())
print('ab'.isidentifier())
# S.islower()是否全部小写
print('Ab'.islower())
print('ab'.islower())
# S.isnumberic(self),如果S中只有数值字符则返回True，否则返回False。数值字符包括数字字符和具有数值属性的Unicode，例如U+2155表示分数五分之一
# S.isdigit(self),比isnumberic能用的范围要广
print(truer.isnumeric())
# S.isprintable()是否是可打印字符,以正则表达式中的打印和非打印为依据
print('\n'.isprintable())
print(truer.isprintable())
# S.isspace(self),是否全部空白且至少一个字符
print('\t'.isspace())
print('a b'.isspace())
print(''.isspace())
# S.istitle(self)是否是titlecase字符串
print(truer.title().istitle())
print(truer.istitle())
# S.isupper(self)是否全部大写且至少一个字符串
print(truer.isupper())
# S.ljust(self),左调整
print(truer.ljust(50, ' '))
# S.lower(self),全部变小写
print(truer.lower())
# S.lstrip(self, chars=None),把字符串左边的chars拿掉
print(truer.lstrip())
# S.maketrans(self, *args, **kwargs),暂留 TODO
# print(truer.maketrans())
# S.partition(self, sep),拆分函数,在分隔符首次出现位置拆分字符串，并返回包含分隔符之前部分、分隔符本身和分隔符之后部分的3元组。
# 如果找不到分隔符，返回包含字符串本身，跟着两个空字符串的 3 元组
print(truer.partition('\t'))
print(truer.partition(' '))
# S.center(self, width, fillchar =None),居中
print(truer.center(50, ' '))
# S.rjust(),右对齐
print(truer.rjust(50, ' '))
# S.rstrip(self, chars=None),把字符串右边的在chars中的字符拿掉
print(truer.rstrip('cne'))
# 不赘述
print(truer.replace('is', 'Is', 1))
# S.rfind(self, sub, start=None, end=None),sub出现的最大索引值,没有lfind()因为find()默认从左开始.
print(truer.rfind('is'))
# S.rindex(self, sub, start=None, end=None),sub出现的最大索引值,没有lindex()因为index()默认从左开始.
print(truer.rindex('is'))
# 从右切分
print(truer.rpartition('is'))
# S.split(self, sub, maxsplit=-1),切分字符串,
# 如果sep未指定或者为None，则采用一种不同的分隔算法：连续的空格被视为一个单一的分隔符，结果的开始或结尾将不包含空字符串即使该字符串有前导或尾随空白。
# 因此，使用None分隔一个空字符串或只包含空白的字符串返回[]。
# 例如，' 1  2   3  '.split()返回['1', '2', '3']，' 1  2   3  '.split (None, 1）返回['1', '2    3   ']。
print(truer.split(' '))
# S.rsplit(self, sub, maxsplit=-1),从右切分字符串
print(truer.rsplit(' '))
# S.swapcase(self)大写变小写,小写变大写
print(truer.swapcase())
# 待处理 TODO
# print(truer.translate())
# S.splitlines(self, keepends=None)返回字符串中行组成的列表，在行的边界截断。此方法使用通用换行符方法分隔行。
# 换行符不包含在结果列表中，除非给定keepends给定且为真,相当于split('\n')
print(' ab\n c\n de \nfg\n kl'.splitlines())
print(' ab\n c\n de \nfg\n kl'.split('\n'))
print(' ab\n c\n de \nfg\n kl'.splitlines(True))
# S.upper(self),转大写
print(truer.upper())
# 在数值字符串的左边填充零至长度为width。符号前缀将正确处理。如果width小于或等于len(s)则返回原始字符串
print('120'.zfill(10))


class A(object):

    def abk(self):
        print('a')


if '__name__' == '__main__':
    a = A()
    print(a.__module__)



