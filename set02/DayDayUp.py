# -*- coding:utf-8 -*-
# Time:2020/3/16 21:32
# Author: 御承扬
# e-mail:2923616405@qq.com
# project: Python大数据
# File: DayDayUp
# PyCharm


def func1():
    day_factor = 0.005
    up = pow(1 + day_factor, 365)
    down = pow(1 - day_factor, 365)
    print("向上：{:.2f}，向下：{:.2f}".format(up, down))


if __name__ == "__main__":
    dayUp = pow(1.001, 365)
    dayDown = pow(0.999, 365)
    print("向上：{:.2f}，向下：{:.2f}".format(dayUp, dayDown))
    print("权重为：0.005时：")
    func1()
