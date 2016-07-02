#!/usr/bin/env python
# encoding: utf-8

"""
@author: wangweikang
@software: PyCharm Community Edition
@file: easyMath.py
@time: 16/7/2 下午10:15
"""

from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MAXTRIES = 2


def doprob():
    op = choice('+-')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    opps = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if opps == MAXTRIES:
                print 'answer\n %s %d' % (pr, ans)
            else:
                print 'incorrect... try angin'
                opps += 1
        except (KeyboardInterrupt, \
                EOFError, ValueError):
            print 'invalid input... try again'


def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
        main()
