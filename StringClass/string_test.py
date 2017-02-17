# -- coding: UTF-8 --

"""
题目内容：
“Pig Latin”是一个英语儿童文字改写游戏，整个游戏遵从下述规则：

(1). 元音字母是‘a’、‘e’、‘i’、‘o’、‘u’。字母‘y’在不是第一个字母的情况下，也被视作元音字母。其他字母均为辅音字母。例如，单词“yearly”有三个元音字母（分别为‘e’、‘a’和最后一个‘y’）和三个辅音字母（第一个‘y’、‘r’和‘l’）。

(2). 如果英文单词以元音字母开始，则在单词末尾加入“hay”后得到“Pig Latin”对应单词。例如，“ask”变为“askhay”，“use”变为“usehay”。

(3). 如果英文单词以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“quiet”变为“ietquay”，“quay”变为“ayquay”。

(4). 如果英文单词以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“tomato”变为“omatotay”， “school” 变为“oolschay”，“you” 变为“ouyay”，“my” 变为“ymay ”，“ssssh” 变为“sssshay”。

(5). 如果英文单词中有大写字母，必须所有字母均转换为小写。

输入格式:
一系列单词，单词之间使用空格分隔。

输出格式：
按照以上规则转化每个单词，单词之间使用空格分隔。

输入样例：
Welcome to the Python world Are you ready

输出样例：
elcomeway otay ethay ythonpay orldway arehay ouyay eadyray

"""
# from __future__ import print_function, division


def transfer_string_to_list(string):
    t = string.split()
    return t


def is_start_with_vowel(string):
    """判断一个字符串是不是元音开头

    :param string: Str
    """
    if string[0] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return True
    return False


def start_with_qu(string):
    """判断一个字符串是否含有'qu'

    :type string: Str
    """
    if len(string) < 2:
        return False
    bool1 = string[0] == 'Q' or string[0] == 'q'
    bool2 = string[1] == 'U' or string[1] == 'u'
    return bool1 and bool2


def is_consonants(char, is_first_letter=False):
    if is_first_letter:
        if char not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            return True
    elif char not in ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'):
        return True
    return False


def remove_and_find_all_consonants_at_the_begining(string):
    res = ''
    new = string
    for i in range(len(string)):
        if is_consonants(string[i], i == 0):
            res += string[i]
            new = new.replace(string[i], '')
        else:
            break
    return [new, res]


def process(string):
    t = transfer_string_to_list(string)
    for i in range(len(t)):
        t[i] = t[i].lower()
        if is_start_with_vowel(t[i]):
            temp = t[i]
            t[i] = temp + 'hay'
        if start_with_qu(t[i]):
            temp = t[i].replace('qu', '')
            t[i] = temp + 'quay'
        if not is_start_with_vowel(t[i]):
            temp = remove_and_find_all_consonants_at_the_begining(t[i])
            t[i] = temp[0] + temp[1] + 'ay'

    delimiter = ' '
    print(delimiter.join(t))


def main():
    string = raw_input()
    process(string)


if __name__ == '__main__':
    main()
