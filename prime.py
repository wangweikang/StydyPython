#!/usr/bin/env python
# encoding: utf-8

# 题 2
# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用

"""
@author: wangweikang
@software: PyCharm Community Edition
@file: prime.py
@time: 16/5/25 下午11:37
"""


def prime_numbers():
    for x in range(3, 100):
        n = 0
        for y in range(2, int(x / 2) + 1):
            if x % y == 0:
                break
            else:
                n += 1
        if n == int(x / 2) - 1:
            print(x)

prime_numbers()