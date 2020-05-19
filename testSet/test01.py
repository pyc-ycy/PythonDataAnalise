# -*- coding:utf-8 -*-
# Time:2020/4/21 17:50
# Author: 御承扬
# e-mail:2923616405@qq.com
# project: Python大数据
# File: test01
# PyCharm

def aFunc(a: int, b: int) -> str:
    c = a + b
    return "a+b=" + str(c)


if __name__ == "__main__":
    a = 23
    b = 32
    c = aFunc(a, b)
    print(c)
