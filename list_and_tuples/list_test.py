# -- coding: UTF-8 --

from __future__ import print_function, division


"""
内建数据结构，用来存储一系列元素


时间复杂度
    量化一个算法的运行时间为输入长度的函数
    不需要显式的计算这些常数

    O表示,只保留高阶项
    线性查找的时间复杂度为O(n)


    O 能告诉我们什么
    如果算法A的复杂度为O(n)，算法B的复杂度为O(n2),对于较大输入，A 总是比B快

    二分查找 输入的应该是有序的列表


    排序
    选择排序



"""


def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst.insert(i, lst.pop(min_index))


def prime(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    res = [2]
    for i in range(3, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res.append(i)
    return res


def bi_search(lst, item):
    if len(lst) == 0:
        return -1
    i = len(lst) // 2
    if lst[i] == item:
        return item
    if lst[i] > item:
        return bi_search(lst[:i], item)
    else:
        return bi_search(lst[i + 1:], item)


def main():
    # n = int(raw_input())
    # lst = []
    # while True:
    #     _ = raw_input()
    #     if _:
    #         lst.append(_)
    #     else:
    #         break
    # list2 = prime(n)
    # for i in lst:
    #     res = bi_search(list2, float(i))
    #     if res > 0:
    #         res = list2.index(res)
    #     print(res)
    list1 = [1, 2, 3]
    list2 = list1
    list3 = list2
    list1.remove(1)
    print(list3[1])


def func(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] < lst[j]:
                lst.insert(i, lst.pop(j))
            else:
                pass
    else:
        return lst
    return -1




if __name__ == '__main__':
    lst1 = [6, 2, 4, 1, 5, 9]
    lst2 = func(lst1)
    lst2[3:-2] = []
    print(lst1)
    main()
