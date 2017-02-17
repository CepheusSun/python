# -- coding: UTF-8 --

from __future__ import print_function, division


known = {0: 0, 1: 1}


def fib(n):
    if n in known:
        return known[n]

    res = fib(n - 1) + fib(n - 2)
    known[n] = res
    return res


def output(n):
    if n < 0:
        print('error')
    else:
        i = 0
        res = 0
        while fib(i) < n:
            if fib(i) % 2 == 0:
                res += fib(i)
            i += 1
        return res


def main():
    n = int(raw_input())
    print(output(n))


if __name__ == '__main__':
    main()
