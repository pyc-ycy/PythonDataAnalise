# -*- coding:utf-8 -*-
# Time:2020/3/24 21:38
# Author: 御承扬
# e-mail:2923616405@qq.com
# project: Python大数据
# File: strOpt
# PyCharm

"""
    字符串处理函数：
    len() 求字符串长度
    str() 将任意类型 x 所对应的字符串形式
    hex() 或 oct() 生成十六进制或八进制字符串
    chr(u) 和 ord(x) 前者用于将 Unicode 编码转成单字符，后者用于将单字符转为 Unicode（Python 默认编码 Unicode）

"""


def WeekNamePrintV1():
    week_str = "星期一星期二星期三星期四星期五星期六星期日"
    week_id = eval(input("请输入星期数字(1-7):"))
    pos = (week_id - 1) * 3
    print(week_str[pos:pos + 3])


def WeekNamePrintV2():
    week_str = "一二三四五六日"
    week_id = eval(input("请输入星期数字(1-7):"))
    print("星期" + week_str[week_id - 1])


def funStr():
    s1 = "1 + 1 = 2" + chr(10004)
    s2 = "这个字符♉的Unicode值是：" + str(ord("♉"))
    print("%s\n%s" % (s1, s2))
    for i in range(12):
        print(chr(9800 + i), end=" ")


if __name__ == "__main__":
    WeekNamePrintV1()
    WeekNamePrintV2()
    funStr()
