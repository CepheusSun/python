# -- coding: UTF-8 --
from __future__ import print_function, division

import bisect
# coding=utf8

# pi = 3.14
# radius = float(raw_input("radius:"))
# area = pi * radius ** 2
# print area


#  input = raw_input()
# print input * 3


# weight = float(raw_input('weight:'))
# height = float(raw_input('height:'))
# bmi = weight / height ** 2
#
# print format(bmi, '.2f')



# userInput = int(raw_input())
#
# hour = userInput / 60 ** 2
# minites = userInput / 60 - hour * 60
# seconds = userInput % 60
#
# print hour, minites, seconds
#
# import math
#
# a = float(raw_input())
# b = float(raw_input())
# c = float(raw_input())
#
# C = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
#
# print format(C * 180 / math.pi, '.1f')

#
# i = 0
# i = (i + 1000) * (1 + 0.047)
# i = (i + 1000) * (1 + 0.047)
# i = (i + 1000) * (1 + 0.047)
# i = (i + 1000) * (1 + 0.047)
# i = (i + 1000) * (1 + 0.047)
# i = (i + 1000) * (1 + 0.047)
# i = (i + 1000) * (1 + 0.047)
# i = (i + 1000) * (1 + 0.047)
# i = (i + 1000) * (1 + 0.047)
# i = (i + 1000) * (1 + 0.047)
#
# print i


# points = int(raw_input("领先的分数："))
# is_in_control = raw_input("是否领先队控球(Y／N：)")
# last_seconds = int(raw_input("比赛剩余秒数："))
#
# points -= 3
#
# if is_in_control == 'Y':
#     points += 0.5
# else:
#     points -= 0.5
#
# if points < 0:
#     points = 0
#
#
# points = points ** 2
#
# if points > last_seconds:
#     print "safe"
# else:
#     print  "unsafe"
#

#
# n = 5
# while n > 0:
#     n -= 1
#     if n < 3:
#         break
# else:
#     print n
#
# print n
#
# e = 1
# factorial = 1
# for i in range(1, 10):
#     factorial *= i
#     e += 1.0 / factorial
#
# print e
#
#
#
#
# pi = 0;
#
# for i in range(1,1000000):
#     pi += (-1.0)**(i + 1) / (2 * i - 1)
#
# pi *= 4;
#
# print  pi
#
#
# count = 0
# for i in range(100 ,1000):
#     if not i % 17:
#         count += 1
#
# print count


#
# n = 6
#
# while n !=  1 :
#     if n % 2 == 0 :
#         n /= 2
#     else:
#         n = 3 * n + 1
#     print n,



# for i in range(1 ,10):
#     for j in range(1 ,10):
#         if i >= j:
#             print format(i * j, '3'),
#     print




# while True:
#     for x in range(6):
#         y = 2 * x + 1
#         if  y > 9:
#             break


# import math
#
# n = int(raw_input())
# sum = 0
#
# def is_prime(num):
#     if num <= 1:
#         return False
#
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# for i in range(n):
#     if  is_prime(i):
#         sum += i
# print sum

# def is_runniam(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         return True
#     return False
#
# def days_per_month(month,year):
#     if month == 0:
#         year -= 1
#         month = 12
#     if month == 1 \
#             or month == 3 \
#             or month == 5 \
#             or month == 7 \
#             or month == 8 \
#             or month == 10 \
#             or month == 12:
#         return 31
#     elif month == 2:
#         if is_runniam(year):
#             return 29
#         return 28
#     else:
#         return 30
#
# last_day = 6
# count = 0
# for year in range(1990, 2001):
#     for month in range(1, 13):
#
#         total_days = days_per_month(month - 1,year) + last_day
#         if last_day == 0 and days_per_month(month -1 ,year) == 28:
#             count += 1
#             last_day = 0
#         elif total_days == 35:
#             count += 1
#             last_day = 0
#         else:
#             if total_days > 35:
#                 last_day = total_days - 35
#             else:
#                 last_day = total_days - 28
# print count
#
# import calendar
# count = 0
# for year in range(1901,2001):
#     for month in range(1,13):
#             if calendar.monthcalendar(year,month)[0].index(1) == 6:
#                 count += 1
# print count










#
# 题目内容：
# 数字197可以被称为循环素数，因为197的三个数位循环移位后的数字：197,971,719均为素数。100以内这样的数字包括13个
# ，2,3,5,7,11,13,17,31,37,71,73,79,97。要求任意正整数n以内一共有多少个这样的循环素数。
#
# 输入格式:
# 一个正整数n。
#
# 输出格式：
# n以内循环素数的数目。
#
# 输入样例：
# 100
#
# 输出样例：
# 13



import math


#
# def shift_number(number):
#     if number < 10:
#         return number
#     temp = number / 10
#     shifter = number % 10
#     shift_one = shifter * 10 + temp
#     return shift_one
#
#
#
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2 , int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# def is_shift_prime(number):
#     if number < 10 and is_prime(number):
#         return True
#
#     real_number = number
#     if is_prime(real_number):
#
#         for i in range(len(list(str(number))) - 1):
#             number = shift_number(number)
#             if is_prime(number):
#                 return True
#     return False
#
#
# def counter(number):
#     count = 0
#     for i in range(1, number+1):
#         if is_shift_prime(i):
#             count += 1
#     return count
#
# n = int(raw_input())
# print counter(n)


# 字符串
# fruit = 'banana'
# letter = fruit[1]
# print letter
# print len(fruit)
# print fruit[-1]


# 遍历字符串

# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print letter
#     index += 1


# for char in fruit:
#     print char


# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
#
# for letter in prefixes:
#     print letter + suffix



# 字符串切片

# s = 'Monty Python'
# print s[0:5]
# print s[6:12]

#  [n:m]操作符返回从第n个到第m个字符串的部分字符串
#  包括第一个，但是不包括最后一个。

# 如果你省略第一个索引，切片起始与0，如果省略最后一个起始于结尾。
# 如果n>m结果是空字符串


# greeting = 'Hello World'
# new_greeting = 'J' + greeting[1:]
# print new_greeting


# searching 搜索
#
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


# print find('hello', 'm')

# 循环和计数
#
# word = 'banana'
# count = 0
# for letter in word:
#     if letter == "a":
#         count += 1
# print count




# 字符串相关方法
#
# word = 'banana'
# new_word = word.upper()
# # print new_word
# index = word.find('a')
# print index
# print word.find('an', 3, 5)
#  参数： 需要查找的字符(串)，从第n个开始查找，查找终点


# in 运算符

# print 'a' in 'banana'


# 字符串比较
#
# if word == 'banana':
#     print 'equal'

# > < 运算符，相当于 ASCII 排序


###############################
#
#
#           案例分析
#
#
###############################


# 读取单词列表
# fin = open('words.txt')
# print fin

#  readline， 其从文件中读取字符直到到达新行并 将结果作为字符串返回:
# print fin.readline()


# line = fin.readline()
# word = line.strip()
# print word

# for line in fin:
#     word = line.strip()
#     print word
#
#
#
# line = fin.readline()
# line = fin.readline()
# print line


# 搜索
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True


# 只要有一个字符在 forbidden 中，都返回真。
# 模糊查找
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True


# 只有 word 中所有的字符都能在 available 中找到，才为真。
# 这个方法可以用来排除非法字符
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True


# word 是否含有 required 中的所有字符
# 验证一个字符必须含有某些字符串
def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


# print has_no_e("hello")
# print avoids('hello', 'm')
# print uses_only('hello', 'hello')
# print uses_all('Hello', 'ol')

# 字符串是否递增
#
# def is_abecedarian(word):
#     previous = word[0]
#     for c in word:
#         if c < previous:
#             return False
#         previous = c
#     return True
#
# print is_abecedarian('abcb')
#
#
# def is_abecedarian(word):
#     if len(word) <= 1:
#         return True
#     if word[0] > word[1]:
#         return False
#     return is_abecedarian(word[1:])
#
# print is_abecedarian('abcb')
#
#
# def is_abecedarian(word):
#     i = 0
#     while i < len(word)-1:
#         if word[i + 1] < word[i]:
#             return False
#         i += 1
#     return True
#
# print is_abecedarian('abc')



# list 列表

# a = 10
# b = 'str'
# lists = [a, b]
# a = 9
# print lists

# 列表方法

# t = ['a', 'b', 'c']
# t.append('d')
# print t
#
# t2 = ['e' ,'f']
# t.extend(t2)
# print t
# t.sort()
# print t



########
# map, filter, reduce 映射，过滤，削减
########


def add_all(t):
    total = 0
    for x in t:
        total += x
    return total


t = [1, 2, 3]


# print add_all(t)
# print sum(t)
#
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res


# print only_upper('asdF')


# pop 方法  改变列表并返回被删除的元素。如果不提供索引，删除并返回最后一个元素。
# del 运算符 如果不需要被删除的值，使用这个
# remove 方法 删除不知道索引的元素, 只删除第一个
# 以上方法运算符都可以使用切片

# t = ['a', 'b', 'c']
# del t[1]
# print t.pop(1)
# print t

# t = ['a', 'b', 'c', 'a']
# t.remove('a')
# print t

# 使用 list 函数将 str 转成 list
# s = 'spam'
# t = list(s)
# print t

# 使用split 方法将字符串分成单词
# s = 'pinging for the fjords'
# t = s.split()
# print t
# # 分隔符
# s = 'spam-spam-spsm'
# delimiter = '-'
# s.split(delimiter)
# print s.split(delimiter)
#
# # join 方法 和 split 相反。他接受一个字符串的列表，并将元素串联起来。
# t = ['pinging', 'for', 'the', 'fjords']
# delimiter = ' '
# print delimiter.join(t)

# a = [12, 14, 15]
# b = a
# b[0] = 19
# print a
#
#
# c = 'aaaa'
# d = c
# d = 'bb'
# print c

# def delete_head(t):
#     del t[0]
#
# letters = ['a', 'b', 'c']
# delete_head(letters)
# print letters
#
#
# def bad_delet_head(t):
#     return t[1:]
#
# print bad_delet_head(letters)
#
#
# def nested_sum(t):
#     sum = 0
#     for t1 in t:
#         for num in t1:
#             sum += num
#     return sum
#
#
# def nested_sum_2(t):
#     res = 0
#     for t1 in t:
#         res += sum(t1)
#     return res
#
#
# t = [[1, 2], [3],[4, 5, 6]]
# print nested_sum(t)
# print nested_sum_2(t)

#
# def custom(t):
#     res = []
#     for i in range(len(t)):
#         res.append(sum(t[:i+1]))
#     return res
#
# t = [1, 2, 3]
# print custom(t)


# def middle(t):
#     del t[len(t) -1]
#     del t[0]
#     return t
#
# t = [1, 2, 3, 4]
# print middle(t)


# def chop(t):
#     del t[len(t) -1]
#     del t[0]
#
# t = [1, 2, 3, 4]
# chop(t)
# print t

#
# def is_sorted(t):
#     temp = sorted(t)
#     if temp == t:
#         return True
#     return False
#
# print is_sorted([1, 2, 2])
# print is_sorted(['b', 'a'])

#
# def is_anagram(word,word2):
#     list1 = list(word)
#     list2 = list(word2)
#     if len(list1) != len(list2):
#         return False
#
#     for letter in list1:
#         if letter in list2:
#             list2.remove(letter)
#         else:
#             return False
#     return True
#
#
# print is_anagram('asd','dss')


# def has_duplicates(t):
#     for i in range(len(t)):
#         if t[i] in t[i+1:]:
#             return True
#     return False
#
# print has_duplicates(['a','b','c','a'])

#
# fin = open('words.txt')
# list = []

# for line in fin:
#     word = line
#     list.append(word)
# print list

# for line in fin:
#     word = line
#     list = list + [word]
#
# print list


def make_word_list():
    """
    reads lines from a file and build a list using append.
    :return: list of strings
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """check weather a word is in a list using bisection search.
    Precondition: the words in the list are sorted

    :param word_list: list of strings
    :param word: string
    """
    if len(word_list) == 0:
        return False

    # 结果四舍五入
    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i + 1:], word)


def in_bisect_cheat(word_list, word):
    """checks weather a word is in a list using bisection search.
    Precondition: the words in the list are sorted

    :param word_list: list of strings
    :param word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


def reverse_pair(word_list, word):
    """ find the shift word of a word

    :param word_list: list of strings
    :param word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)


def interlock(word_list, word):
    """check whether a word contains two interleaved words.

    :param word_list: list of strings
    :param word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds)


def interlock_general(word_list, word, n=3):
    """check wheather a word contains n interleaved words.

    :param word_list: list of strings
    :param word: string
    :param n: number if interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True


if __name__ == '__main__':
    word_list = make_word_list()
    #
    # for word in ['aa', 'alien', 'allen', 'zymurgy']:
    #     print(word, 'in list', in_bisect(word_list, word))
    #
    # for word in ['aa', 'alien', 'allen', 'zymurgy']:
    #     print(word, 'in list', in_bisect_cheat(word_list, word))

    # for word in word_list:
    #     if reverse_pair(word_list, word):
    #         print(word, word[::-1])

    # for word in word_list:
    #     if interlock(word_list, word):
    #         print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])

            