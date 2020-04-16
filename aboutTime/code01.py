# -*- coding:utf-8 -*-
# Time:2020/4/16 21:29
# Author: 御承扬
# e-mail:2923616405@qq.com
# project: Python大数据
# File: code01
# PyCharm

# Use time library
import time


if __name__ == "__main__":
    print(time.time())
    print(time.gmtime())
    t = time.gmtime()
    print(time.strftime("%Y-%m-%d,%B %A %H:%M:%S", t))
    tmpStr = time.strftime("%Y-%m-%d %H:%M:%S", t)
    tmpStr2 = time.strptime(tmpStr, "%Y-%m-%d %H:%M:%S")
    print(tmpStr2)