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
    常用的字符串处理方法：
    str.lower() 与 str.upper() 前者用于将字符串中的大写字母转为小写字母，后者相反
    str.split(sep=None) 根据分隔符将字符串划分成字串，返回一个子字符串构成的列表
    str.count(sub) 统计字串在字符串中出现的次数
    str.replace(old, new) 将指定的字串进行替代
    str.center(width[,fillchar]) 字符串根据宽度进行居中，不足长的用填充字符填充
    str.strip(chars) 去掉字符串中的字串
    str.join(iter) 在 iter 变量除最后元素外每个元素后增加一个 str
    .format 格式化：
    "{:格式控制标记}：字符串".format(数据)
    {} 里从左到右依次为
    : 引导符号，填充字符控制，对齐方式控制，输出宽度控制，千位分隔符控制，小数点精度控制，
    数据类型（b, c, d, o, x, X 表示整数，e E f % 表示浮点数类型
    {0:=^20}   0 表示 format 中的第一个参数 = 表示填充字符，^ 表示居中对齐，20 表示输出宽度
    > 表示右对齐，< 表示左对齐
     "{0:#^20,.4f}".format(142.369875)
    '######142.3699######'
    "{0:#^20,.4f}".format(1234567.2365478)
    '###1,234,567.2365###'
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
