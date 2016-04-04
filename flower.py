#!/usr/bin/env python
# encoding: utf-8

"""
@author: wangweikang
@software: PyCharm Community Edition
@file: flower.py
@time: 16/4/4 下午2:05
"""

from __future__ import print_function, division
import turtle
from mypolygon import arc


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)


def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


bob1 = turtle.Turtle()

move(bob1, -100)
flower(bob1, 7, 40.0, 60.0)

move(bob1, 100)
flower(bob1, 20, 140.0, 20.0)

bob1.hideturtle()
turtle.mainloop()
