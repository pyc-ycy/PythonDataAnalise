# PyCharm
# Python大数据
# sy01
# 御承扬
# 2019/12/18


if __name__ == '__main__':
    xi = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    yi = [1.0]
    for i in range(0, 10, 1):
        t = yi[i] + 0.1 * (2 / 3 * xi[i] * (yi[i] ** (-2)))
        yi.append(t)
    yi[1]=yi[0]+0.1*(2/3*xi[0]*(yi[0]**(-2)))
    for k in yi:
        print("%d:\t%f\t%f" % (yi.index(k), xi[yi.index(k)], k))
        print('\n')