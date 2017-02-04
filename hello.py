# -- coding: UTF-8 --


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
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

print is_abecedarian('abcb')


def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

print is_abecedarian('abcb')


def is_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i + 1] < word[i]:
            return False
        i += 1
    return True

print is_abecedarian('abc')
