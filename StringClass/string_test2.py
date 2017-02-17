# -- coding: UTF-8 --

from __future__ import print_function, division

"""
题目内容：
依次计算一系列给定字符串的字母值，字母值为字符串中每个字母对应的编号值（A对应1，B对应2，以此类推，不区分大小写字母，非字母字符对应的值为0）的总和。例如，Colin 的字母值为 3 + 15 + 12 + 9 + 14 = 53

输入格式:
一系列字符串，每个字符串占一行。

输出格式：
计算并输出每行字符串的字母值。

输入样例：
Colin
ABC

输出样例：
53
6

"""


def count_of_letter(letter):
    return ord(letter) - 64


def add(num0, num1):
    return num0 + num1


def process(string):
    string = string.upper()
    t = list(string)
    new_t = map(count_of_letter, t)
    print(reduce(add, new_t))


def main():
    t = []
    while True:
        _ = raw_input()
        if _:
            t.append(_)
        else:
            break
    for _ in t:
        process(_)


if __name__ == '__main__':
    main()
