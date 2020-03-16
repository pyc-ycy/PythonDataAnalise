# -*- coding:utf-8 -*-
# Time:2020/3/15 21:28
# Author: 御承扬
# e-mail:2923616405@qq.com
# project: Python大数据
# File: DataType
# PyCharm

import math

if __name__ == "__main__":
    num = 8
    f = 0.1 + 0.2
    print("num 的二进制表示：{:b}".format(num))
    print("{:.16f}".format(f))
    # round 用于四舍五入，第二个参数用于小数截取位数
    # 不确定尾数一般发生在 10^-16 左右，round 十分有效
    t = round(0.1 + 0.2, 1) == 0.3
    print(t)
    # 科学计数法 4.3e-3=0.0043
    y = 0.43e-2
    print(y)
    # 复数类型
    fs = 12.3 + 12.4j
    num1 = math.sqrt(4)
    print("{:f},{:}".format(num1, type(num1)))
    print(type(fs))
    # 商余
    print(divmod(10, 3))
    # pow(x,y,[z]) z 用于取后几位, 可省略
    print(pow(3, pow(3, 99), 10000))
    n1 = 2
    n2 = 4
    n1 **= n2
    print(n1)
