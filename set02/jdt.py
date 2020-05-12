# -*- coding:utf-8 -*-
# Time:2020/4/28 16:16
# Author: 御承扬
# e-mail:2923616405@qq.com
# project: Python大数据
# File: jdt
# PyCharm


# -*- coding: UTF-8 -*-

import sys
import time


class ShowProcess:
    """
    显示处理进度的类
    调用该类相关函数即可实现处理进度的显示
    """
    i = 0  # 当前的处理进度
    max_steps = 0  # 总共需要处理的次数
    max_arrow = 50  # 进度条的长度
    infoDone = 'done'

    # 初始化函数，需要知道总共的处理次数
    def __init__(self, maxSteps, infoDone='Done'):
        self.max_steps = maxSteps
        self.i = 0
        self.infoDone = infoDone

    # 显示函数，根据当前的处理进度i显示进度
    # 效果为[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def show_process(self, i=None):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps)  # 计算显示多少个'>'
        num_line = self.max_arrow - num_arrow  # 计算显示多少个'-'
        percent = self.i * 100.0 / self.max_steps  # 计算完成进度，格式为xx.xx%
        processBar = '[' + '>' * num_arrow + '-' * num_line + ']' \
                     + '%.2f' % percent + '%' + '\r'  # 带输出的字符串，'\r'表示不换行回到最左边
        sys.stdout.write(processBar)  # 这两句打印字符到终端
        sys.stdout.flush()
        if self.i >= self.max_steps:
            self.close()

    def close(self):
        print('')
        print(self.infoDone)
        self.i = 0


if __name__ == '__main__':
    max_steps = 100

    process_bar = ShowProcess(max_steps, 'OK')

    for i in range(max_steps):
        process_bar.show_process()
        time.sleep(0.1)
# ————————————————
# 版权声明：本文为CSDN博主「持久决心」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/u013832707/java/article/details/73608504
