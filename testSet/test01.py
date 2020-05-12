# -*- coding:utf-8 -*-
# Time:2020/4/21 17:50
# Author: 御承扬
# e-mail:2923616405@qq.com
# project: Python大数据
# File: test01
# PyCharm

def leiChen(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result


if __name__ == "__main__":
    n = int(input())
    sumNum = 0
    for i in range(1,n+1):
        sumNum = sumNum + leiChen(i)
    print(sumNum)
