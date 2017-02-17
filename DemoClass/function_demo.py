# -- coding: UTF-8 --

# from __future__ import print_function, division


def foo():
    m = 1
    def bar():
         n = 2
         return m + n
    m = bar()
    # print(m)


def fib(n):
    f1, f2 = 0, 1
    while f2 < n:
        print f2,
        f1, f2 = f2, f1 + f2


def gcd(m, n):
    r = m % n
    if r == 0:
        return n
    else:
        r = m % n
    return gcd(n, r)


def main():
    # foo()
    print gcd(15, 36)


if __name__ == '__main__':
    main()
