class MyAnnotation:
    """
    算法!

    文档字符串的规范:一行以句号, 问号或惊叹号结尾的概述(或者该文档字符串单纯只有一行). 接着是一个空行. 接着是文档字符串剩下的部分,
    它应该与文档字符串的第一行的第一个引号对齐
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def annotation(self):
        """
        函数注解

        这个是为了方便对函数的注释规范有一个了解而做的样例。
        :return:
        """
        print(self.__doc__)


myAnnotation = MyAnnotation("ddd", 12)
print(myAnnotation.annotation())
print(myAnnotation.annotation.__doc__)
