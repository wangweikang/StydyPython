#!/usr/bin/env python
# encoding: utf-8

"""
@author: wangweikang
@software: PyCharm Community Edition
@file: pie.py
@time: 16/4/4 下午2:21
"""

from __future__ import print_function, division

import math
import turtle

def draw_pie(t, n, r):
    polypie(t, n, r)
    t.pu()
    t.fd(r * 2 + 10)
    t.pd()

def polypie(t, n, r):
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle / 2)
        t.lt(angle)

def isosceles(t, r, angle):

    y = r * math.sin(angle * math.pi / 180)
    t.rt(angle)
    t.fd(r)
    t.lt(90 + angle)
    t.fd(2 * y)
    t.lt(90 + angle)
    t.fd(r)
    t.lt(180 - angle)

bob2 = turtle.Turtle()
bob2.pu()
bob2.bk(130)
bob2.pd()

draw_pie(bob2, 5, 60)
draw_pie(bob2, 6, 60)
draw_pie(bob2, 7, 60)
draw_pie(bob2, 8, 60)

bob2.hideturtle()
turtle.mainloop()