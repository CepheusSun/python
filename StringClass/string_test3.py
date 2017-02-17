# -- coding: UTF-8 --

from __future__ import print_function, division

"""
题目内容：
依次判断一系列给定的字符串是否为合法的 Python 标识符。

输入格式:
一系列字符串，每个字符串占一行。

输出格式：
判断每行字符串是否为合法的 Python 标示符，如果合法则输出 True，否则输出 False。

输入样例：
abc
_def
21gh

输出样例：
True
True
False

"""

import re


def is_illegal(string):
    print(string)
    re_ = re.compile(r'^[a-zA-Z_][\w_]*')
    for x in string.split():
        print(True if re_.findall(x) else False)


def main():
    tmp = ''
    while True:
        _ = raw_input()
        if _:
            tmp += _ + '\n'
        else:
            break
    is_illegal(tmp)


if __name__ == '__main__':
    main()
