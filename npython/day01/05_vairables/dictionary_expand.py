"""
    1.Dictionary的方法
    2len(dict):长度
    3.d[key]:返回字典d中键为key的元素。如果key不在映射中，则引发一个KeyError
    4.d[key] = value,设置d[key]的值为value
    5.del d[key] 从d中删除d[key] 。如果key不在映射中，则抛出KeyError。
    6.key in d 如果d有一个键key，则返回True，否则返回False。
    7.key not in d.相当于not key in d。
    8.iter(d).返回字典的键上的一个迭代器。这是iterkeys()的快捷方式
    9.clear()从字典中移除所有项。
    10.copy()返回字典的一个浅拷贝。
    11.fromkeys(seq[, value])与键从seq和值将设置为值创建一个新的字典。
    12.fromkeys()是一个类方法，返回一个新字典。value默认为None。
    13.get(key[, default])如果key在字典中，则返回key对应的值，否则返回default。如果没有预置default的值，则它默认为None，所以此方法永远不会引发KeyError。
    14.has_key(key)测试key是否在字典中存在。has_key()已经被key in d弃用。
    15.items()返回该dictionary的(key, value)对的列表。
    如果items()、keys()、values()、iteritems()、iterkeys()和itervalues()调用过程中没有对字典进行修改，则列表将完全一致。
    这允许使用zip()创建(value, key)对：pairs = zip(d.values(), d.keys())。iterkeys()和itervalues()
    方法具有同样的关系：pairs = zip(d.itervalues(), d.iterkeys())提供相同的pairs值。另一种创建相同列表的方式是pairs = [(v, k) for （k, v） in d.iteritems()]
    16.iteritems()返回字典的(key, value)对上的一个迭代器。请参阅dict.items()注释。
    使用iteritems()过程中添加或删除字典中的项可能引发RuntimeError或遍历所有条目失败.
    17.iterkeys()返回字典的键上的一个迭代器。请参阅dict.items()注释。
    使用iterkeys()过程中添加或删除字典中的项可能引发RuntimeError或遍历所有条目失败.
    18.itervalues()在字典的值返回一个迭代器。请参阅dict.items()注释。
    使用itervalues()过程中添加或删除字典中的项可能引发RuntimeError或遍历所有条目失败.
    19.keys()返回的字典的键列表的副本。请参阅dict.items()注释。
    20.pop(key[, default])如果key在字典中，删除它并返回其值，否则返回default。如果没有给出default且key不是在字典中，则引发一个KeyError。
    21.popitem()从字典中移除并返回任意一个(key, value)对。
    22.popitem()对于破坏性地遍历一个字典很有用，正如在集合算法中经常用到的一样。如果字典为空，调用popitem()将引发一个KeyError。
    23.setdefault(key[, default])如果key在字典中，返回其值。如果不在，则插入值为default的key并返回default。default默认为None。
    24.update([other])依据other更新词典的键/值对，覆盖现有的键。返回None。
    25.update()接受另一个字典对象或可迭代的键/值对（如元组或其它长度为2的可迭代对象）。如果指定的是关键字参数，那么字典使用这些键/值对更新：d.update(red=1, blue=2)。
        2.4版中的更改：允许参数是可迭代的键/值对，并允许关键字参数。
    26.values()返回字典的值的列表的副本。请参阅dict.items()注释。
    27.viewitems()返回字典项(key, value)对的一个新视图。有关详细信息，请参阅以下文档的视图对象。
    28.viewkeys()返回字典的键的新的视图。有关详细信息，请参阅以下文档的视图对象。
    29.viewvalues()返回字典的值的新的视图。有关详细信息，请参阅以下文档的视图对象。
"""
pass
# Dictionary,字典
dicts = {}
dicts['one'] = 'This is one'
dicts[2] = 'This is 2'

# dictionary的遍历
for k in dicts:
    print("dictionary 的 key是: ", k, "dictionary 的 值是: ", dicts[k])
# dictionary的大小
print(dicts.__len__())
# dictionary值
print(dicts.items())
# dictionary的values和keys对应,以及items对应
print(dicts.values(), dicts.keys(), dicts.items())
