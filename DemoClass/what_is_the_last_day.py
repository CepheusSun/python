# -- coding: UTF-8 --

from __future__ import print_function, division


def count_day_of_month(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 29
    else:
        return 28


def total_count_of_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 366
    else:
        return 365


def counter(year, month):
    total_count = 2
    for y in range(1800, year):
        total_count += total_count_of_year(y)
    for m in range(1, month + 1):
        total_count += count_day_of_month(year, m)
    res = total_count % 7
    print(res)


def main():
    year = int(raw_input())
    month = int(raw_input())
    counter(year, month)


if __name__ == '__main__':
    main()
