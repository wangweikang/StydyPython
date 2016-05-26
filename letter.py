#!/usr/bin/env python
# encoding: utf-8

# 题 4
# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形式

"""
@author: wangweikang
@software: PyCharm Community Edition
@file: letter.py
@time: 16/5/25 下午11:38
"""


def cap_string(str_='xiao jing mo meng meng da'):
    srlist = [x[0].upper() + x[1:] + ' ' for x in str_.split(' ')]
    print(''.join(srlist))


cap_string()
