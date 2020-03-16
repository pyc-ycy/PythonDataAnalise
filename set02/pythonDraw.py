# -*- coding:utf-8 -*-
# Time:2020/3/15 21:22
# Author: 御承扬
# e-mail:2923616405@qq.com
# project: Python大数据
# File: pythonDraw
# PyCharm

import turtle as tl  # 引入绘图库 turtle
# 绘制蟒蛇
# 控制窗体大小
# setup 函数的参数从左到右分别是：窗体长度，窗体高度，窗体左上角横坐标，纵坐标
# goto 函数可以用绝对坐标控制海龟去到某一位置
# 使用海龟坐标，则可以用 fd(),bk() 等函数控制海龟运动方向。
tl.setup(950,350,100,100)
# penup 函数用于抬起画笔，此函数之后画笔的任何操作不会在画布上留下痕迹
tl.penup()
# fd=forward，向前前进，负数表示后退，效果等同于 bk 函数
# tl.fd(-350)
tl.bk(350)
# pendown 放下画笔，此函数之后的画笔操作会在画布上留下痕迹。
tl.pendown()
# pensize 设置画笔大小
tl.pensize(25)
# pencolor 设置画笔颜色，参数要用颜色名字符串或rgb值,rgb元组
tl.pencolor("purple")
# seth() 函数用于设置角度，正值为绝对角度坐标顺时针，负数为逆时针
# left 和 right 用海龟角度来改变方向
tl.seth(-40)
# 控制蟒蛇的节数
# circle 函数用于画弧，第一参数设置半径，第二个参数设置弧度大小，默认360°
# 圆心默认在海龟左侧 r 距离的位置上
for i in range(6):
    tl.circle(40,80)
    tl.circle(-40,80)
tl.circle(40,80/2)
tl.fd(10)
tl.circle(16,180)
tl.fd(40*2/3)
tl.done()