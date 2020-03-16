# -*- coding:utf-8 -*-
# Time:2020/3/1 15:35
# Author: 御承扬
# e-mail:2923616405@qq.com
# project: Python大数据
# File: nothing
# PyCharm

from turtle import *


def draw1():
    pensize(2)
    circle(10)
    circle(40)
    circle(80)
    circle(160)


def draw2():
    color('red', 'red')
    begin_fill()
    for i in range(5):
        fd(200)
        rt(144)
    end_fill()
    done()

def draw3():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()


if __name__ == "__main__":
    print("Hello world")
    draw3()

