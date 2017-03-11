# -- coding: UTF-8 --

from __future__ import print_function, division


def is_pal(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_pal(s[1:-1])


def max_pal(n):
    max_num, max_a, max_b = 0, 0, 0
    for a in range(10 ** (n - 1), 10 ** n):
        for b in range(a, 10 ** n):
            if is_pal(str(a*b)):
                if a * b > max_num:
                    max_num, max_a, max_b = a * b, a, b
    return max_num


def main():
    print(max_pal(int(raw_input())))


if __name__ == '__main__':
    main()
