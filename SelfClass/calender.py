# -- coding: UTF-8 --
"""
题目内容：
一个斐波那契数列的前10项为：1, 2, 3, 5, 8, 13, 21, 34, 55, 89，对于一个最大项的值不超过n的斐波那契数列，求值为偶数的项的和。

输入格式:
一个正整数n，如100。

输出格式：
值为偶数的项的和，如 2 + 8 + 34 = 44。

输入样例：
100

输出样例：
44
"""


def is_even_number(n):
    """computes whether the number is an even number if so return True

    :param n:Int
    :return:
    """
    return not n % 2


def main():
    pass


def answer_the_question(n):
    if n < 1:
        print('输入错误')
        return

    first_number = 1



if __name__ == '__main__':
    main()
