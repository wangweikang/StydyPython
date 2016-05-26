#!/usr/bin/env python
# encoding: utf-8

# 题 5
# 写一个 Queue 类，它有两个方法，用法如下

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)

# print(q.dequeue()) # 1
# print(q.dequeue()) # 2
# print(q.dequeue()) # 3

"""
@author: wangweikang
@software: PyCharm Community Edition
@file: que.py
@time: 16/5/25 下午11:39
"""


class Node(object):
    def __init__(self, val, p=0):
        self.data = val
        self.next = p


class Queue(object):
    """docstring for Queue"""

    def __init__(self, node=Node(0)):
        self.head = node
        self.head.next = None

    def enqueue(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        return data


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  # 1
print(q.dequeue())  # 2
print(q.dequeue())  # 3
