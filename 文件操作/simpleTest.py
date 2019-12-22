# PyCharm
# Python大数据
# simpleTest
# 御承扬
# 2019/12/22


def createFile():
    newfile = r'.\t1.txt'
    b_new_file = open(newfile, 'w')
    t_n = b_new_file.write("I am using python to option file,and trying to write!")
    b_new_file.close()
    print("往文件里写入%d字节内容" % t_n)


def readFile():
    file = r'\t1.txt'
    r_file = open(file)
    context = r_file.read()
    print("文件内容：\n")
    print(context)


if __name__ == '__main__':
    createFile()
    readFile()
