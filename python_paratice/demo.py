a = 1


def fun():
    #  全局变量
    global a
    a = 2
    # 打印a的内存地址
    print(id(a))
    print(f"变量a的值：{a}")
    print("这是一个方法")


# print(a)
# fun()
# print(id(a))
# print(a)
# print(fun())

if __name__ == '__main__':
    print("start")
    fun()
    print("end")

# def fun():
#     a = 2
#     print(id(a))
#     print(f"变量a的值： {a}")
#     print("这是一个方法")
#
#
# print(a)
# fun()
# print(a)
#
# if __name__ == '__main__':
#     fun()
