#!/usr/bin/env python
# encoding: utf-8

# 题 1
# 检查密码规则合法性
# 考察基本编码能力和字符串处理
# 参考 python 文档的字符串库

# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10
"""
@author: wangweikang
@software: PyCharm Community Edition
@file: pwd.py
@time: 16/5/25 下午11:36
"""


def valid_password(pwd=''):

    if not pwd[0].isalpha():
        return False
    for x in pwd:
        print(x)
        if not (x.isalpha() or x.isdigit() or x == '_'):
            return False
    if (pwd[0] == '_') or (pwd[-1] == '_'):
        return False

    if len(pwd) < 2 or len(pwd) > 10:
        return False

    return True


p = 'a22_d'
valid_password(p)
print(valid_password(p))

