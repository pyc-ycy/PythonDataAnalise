# -*- coding:utf-8 -*-
# Time : 2019/11/23 下午 9:37 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  Python大数据
# File : test.py 
# @software: PyCharm


def test(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    a = int(10)
    b = int(15)
    d = "a"
    e = "4"
    c = test(a, b)
    print(c)
