# PyCharm
# Python大数据
# test3X
# 御承扬
# 2019/12/9


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

if __name__ == '__main__':
    fig = plt.figure(figsize=(8, 6))
    ax = fig.gca(projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)  ## 生成二维测试数据
    ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
    cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='y', offset=-40, cmap=cm.coolwarm)
    ax.set_xlabel('X')
    ax.set_xlim(-40, 40)
    ax.set_ylabel('y')
    ax.set_ylim(-40, 40)
    ax.set_zlabel('z')
    ax.set_zlim(-100, 100)
    plt.show()

