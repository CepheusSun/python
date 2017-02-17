# -- coding: UTF-8 --

from __future__ import print_function, division


def hanoi(n, a, b, c):
    if n == 1:
        print('Move', n, 'from', a, 'to', c)
    else:
        hanoi(n - 1, a, c, b)
        print('Move', n, 'from', a, 'to', c)
        hanoi(n - 1, b, a, c)


def main():
    num = int(raw_input())
    hanoi(num, 'A', 'B', 'C')


if __name__ == '__main__':
    main()
