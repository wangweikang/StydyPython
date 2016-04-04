#!/usr/bin/env python
# encoding: utf-8

"""
@author: wangweikang
@software: PyCharm Community Edition
@file: mypolygon.py
@time: 16/4/4 下午12:15
"""
import turtle

import math

bob = turtle.Turtle()
print (bob)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

for i in range(4):
    bob.fd(100)
    bob.lt(90)


# encapsulation 封装
def qeuare(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


qeuare(bob)


# 增加一个型参 泛化 generalization
# 边长不同的正方形
def qeuare(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


qeuare(bob, 100)


# 任意边长的多边形
def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


polygon(bob, 7, 70)  # 或者为避免忘记给他参数加上名称polygon(bob, n=7, length=70)


# 画50边形

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)


circle(bob, 100)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


arc(bob, 60, 275)

