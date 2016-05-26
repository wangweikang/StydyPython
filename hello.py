#!/usr/bin/env python
# encoding: utf-8

# 题 3
# 给定一个只包含字母的字符串，返回单个字母出现的次数
# 考察字典的概念和使用
# 返回值为包含元组的列表，格式如下（对列表中元组的顺序不做要求）
# 参数 "hello"
# 返回值 [('h', 1), ('e', 1), ('l', 2), ('o', 1)]

"""
@author: wangweikang
@software: PyCharm Community Edition
@file: hello.py
@time: 16/5/25 下午11:38
"""


def letter_count(str1='hello'):
    d = dict()
    for x in str1:
        try:
            d[x] += 1
        except KeyError:
            d[x] = 1
    lst = [(k, v) for k, v in d.items()]
    print(lst)


letter_count()
