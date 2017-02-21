# -- coding: UTF-8 --
# @Date    : 2017-02-21
# @Author  : CepheusSun
# @Version : python 2.7


class Tree(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def post_visit(tree):
    """递归后序遍历"""
    if tree:
        post_visit(tree.left)
        post_visit(tree.right)
        print(tree.data)


def pre_visit(tree):
    """递归先序遍历"""
    if tree:
        print(tree.data)
        pre_visit(tree.left)
        pre_visit(tree.right)


def in_visit(tree):
    """递归中序遍历"""
    if tree:
        in_visit(tree.left)
        print (tree.data)
        in_visit(tree.right)


def pre_stack(tree):
    """堆栈先序遍历"""
    if tree:
        my_stack = []
        node = tree
        while node or my_stack:
            while node:
                print(node.data)
                my_stack.append(node)
                node = node.left
            node = my_stack.pop()
            node = node.right


def in_stack(tree):
    """堆栈中序遍历"""
    if tree:
        my_stack = []
        node = tree
        while node or my_stack:
            while node:
                my_stack.append(node)
                node = node.left
            node = my_stack.pop()
            print(node.data)
            node = node.right


def post_stack(tree):
    if tree:
        my_stack1 = []
        my_stack2 = []
        node = tree
        my_stack1.append(node)
        while my_stack1:
            node = my_stack1.pop()
            if node.left:
                my_stack1.append(node.left)
            if node.right:
                my_stack1.append(node.right)
            my_stack2.append(node)
        while my_stack2:
            print my_stack2.pop().data


def main():
    node1 = Tree(1, 0, 0)
    node2 = Tree(2, 0, 0)
    node3 = Tree(3, node1, node2)
    node4 = Tree(4, 0, 0)
    node5 = Tree(5, node4, node3)
    print("the post_visit is ...")
    post_visit(node5)
    post_stack(node5)
    print("the pre_visit is ...")
    pre_visit(node5)
    pre_stack(node5)
    print("the in_visit is ...")
    in_visit(node5)
    in_stack(node5)


if __name__ == '__main__':
    main()
