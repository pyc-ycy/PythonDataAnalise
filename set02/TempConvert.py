# -*- coding:utf-8 -*-
# Time:2020/3/15 21:14
# Author: 御承扬
# e-mail:2923616405@qq.com
# project: Python大数据
# File: TempConvert
# PyCharm

TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print("转换后的温度是：{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("转换后的温度时：{:.2f}F".format(F))
else:
    print("输入格式错误！")
