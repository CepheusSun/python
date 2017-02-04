# -- coding: UTF-8 --
from __future__ import print_function, division

from pronounce import read_dictionary

eng2sp = dict()

eng2sp['one'] = 'uno'


"""
    对于字典来说，python 使用了一种叫做哈希表的算法，这就有一种很厉害的特性：
    in 运算符在对字典来使用对时候无论字典规模有多大，无论里面的项与多少个，花费的时间基本上是一样的。


    字典是用哈希表(散列表)来实现的，这意味着所有的键必须是散列的。

    hash 是一个函数，接受任意一种值，然后返回一个整数。
    字典用这些整数来存储和查找键值对，这些整数也叫做哈希值。

    如果键不可修改，系统工作正常。但如果键可以修改，比如是列表。就悲剧了。
    比如说：
        在创建一个键值对的时候，python计算键的哈希值，然后存在相应的未知。如果你修改了键，然后再计算哈希值，
        就不会指向同一个位置。这时候一个键就可以有两个指向了，或者就找不到某个键了。这就是为什么键必须是散列的，
        而像列表这样的可变类型就不行。

    因为字典是可以修改的，所以不能用来做键，只能用来做键值。
"""


"""
    字典有一个方法，get，接受一个键和一个默认值。如果这个键在字典中存在，get 就会返回对应的值，如果不存在返回默认值
"""

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] =1
        else:
            d[c] += 1
    return d


def print_hist(h):

    keys = h.keys()
    keys.sort()
    for c in keys:
        print(c, h[c])


def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res


verbose = True
"""
    全局变量。在函数内部对全局变量重新赋值并不会改变这个变量
    因为：
        函数中创建的是一个新的局部变量，函数结束之后，局部变量就释放了，并不会影响全局变量。

    如果要在函数内重新赋值，必须在使用这个全局变量之前用 global 关键字声明这个全局变量

        global verbose = False

    如果全局变量指向的是一个可修改的值，你可以无需声明该变量就直接修改。

    所以
        你可以在全局的列表或者字段里添加、删除、或者替换元素，但是如果要重新给这个变量赋值，就必须要声明
"""


def example():
    if verbose:
        print('Running example')


def make_word_dict():
    """read 'words.txt ' and create word list from it

    """
    word_dict = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_dict[word] = ''
    return word_dict


def homephones(a, b, phonetic):
    if a not in phonetic or b not in phonetic:
        return False
    return phonetic[a] == phonetic[b]


def check_word(word, word_dict, phonetic):
    word1 = word[1:]
    if word1 not in word_dict:
        return False
    if not homephones(word, word1, phonetic):
        return False

    word2 = word[0] + word[2:]
    if word2 not in word_dict:
        return False
    if not homephones(word, word2, phonetic):
        return False

    return True


if __name__ == '__main__':
    # print eng2sp
    # print len(eng2sp)
    # print 'one' in eng2sp
    # print eng2sp.values()
    # h = histogram('hello')
    # print(invert_dict(h))
    # print(fibonacci(100))
    # print(make_word_dict())

    phonetic = read_dictionary()
    word_dic = make_word_dict()
    for word in word_dic:
        if check_word(word, word_dic, phonetic):
            print(word, word[1:], word[0] + word[2:])