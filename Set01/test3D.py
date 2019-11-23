# -*- coding:utf-8 -*-
# Time : 2019/11/23 下午 9:55 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  Python大数据
# File : test3D.py 
# @software: PyCharm


import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__ == "__main__":
    delta = 0.2
    x = np.arange(-3, 3, delta)
    y = np.arange(-3, 3, delta)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2
    x = X.flatten() # 返回一维数组
    y = Y.flatten()
    z = Z.flatten()
    fig = plt.figure(figsize=(12, 6))
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.01)
    plt.title("3D")
    ax2 = fig.add_subplot(122)
    cs = ax2.contour(X, Y, Z, 15, cmap='jet')
    ax2.clabel(cs, inline=True, fontsize=10, fmt='%1.1f')
    plt.title("Contour")
    plt.show()