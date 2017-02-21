# -- coding: UTF-8 --
# @Date    : 2017-02-21
# @Author  : CepheusSun
# @Version : python 2.7


def quick_sort(array, first_index, last_index):
    """快速排序"""
    if first_index < last_index:
        div_index = partition(array, first_index, last_index)
        quick_sort(array, first_index, div_index)
        quick_sort(array, div_index + 1, last_index)
    else:
        return


def partition(array, first_index, last_index):
    i = first_index - 1
    for j in range(first_index, last_index):
        if array[j] <= array[last_index]:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[last_index] = array[last_index], array[i + 1]
    return i


def merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


def merge_sort(array):
    """并归排序"""
    if len(array) <= 1:
        return array
    num = len(array) / 2
    left = merge_sort(array[:num])
    right = merge_sort(array[num:])
    return merge(left, right)


def main():
    array = [1, 4, 7, 5, 4, 9, 5, 8, 76, 5, 567, 54, 6, 54, 5, 5, 4, 0]
    print("initial array : \n", array)
    print("merge sort result: \n", merge_sort(array))
    quick_sort(array, 0, len(array) - 1)
    print("result array :\n", array)


if __name__ == '__main__':
    main()
