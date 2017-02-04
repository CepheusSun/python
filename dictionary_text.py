# -- coding: UTF-8 --

eng2sp = dict()

eng2sp['one'] = 'uno'


"""
    对于字典来说，python 使用了一种叫做哈希表的算法，这就有一种很厉害的特性：
    in 运算符在对字典来使用对时候无论字典规模有多大，无论里面的项与多少个，花费的时间基本上是一样的。

"""


"""
    字典有一个方法，get，接受一个键和一个默认值。如果这个键在字典中存在，get 就会返回对应的值，如果不存在返回默认值
"""

if __name__ == '__main__':
    print eng2sp
    print len(eng2sp)
    print 'one' in eng2sp
    print eng2sp.values()