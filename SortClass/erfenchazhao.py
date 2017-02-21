# -- coding: UTF-8 --
# @Date    : 2017-02-21
# @Author  : CepheusSun
# @Version : python 2.7


def in_bisect(word_list, word):
    """check weather a word is in a list using bisection search.
    Precondition: the words in the list are sorted

    :param word_list: list of strings
    :param word: string
    """
    if len(word_list) == 0:
        return False

    # 结果四舍五入
    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i + 1:], word)


def main():
    array = ['1', 'asf', 'sf2', 'df1', '2das', '5asdfd', '0sadf',
            '2ge', 'efc2', '1eds', '2ef', '2apple', 'apple', 'orange']
    print(in_bisect(array, '1'))
    print(in_bisect(array, '111'))


if __name__ == '__main__':
    main()
