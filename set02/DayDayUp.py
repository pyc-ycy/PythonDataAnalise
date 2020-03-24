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


def dayUp(df) -> float:
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup


if __name__ == "__main__":
    day_Up = pow(1.001, 365)
    dayDown = pow(0.999, 365)
    print("向上：{:.2f}，向下：{:.2f}".format(day_Up, dayDown))
    print("权重为：0.005时：")
    func1()
    dayFactor = 0.01
    while dayUp(dayFactor) <= 37.78:
        dayFactor += 0.001
    print("工作日的努力参数：{:.5f}".format(dayFactor))
    print("{:.5f}".format(pow(1 + dayFactor, 365)))
    t = "t"
    print("%s" % (t * 4))
