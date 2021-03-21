a = 1


def fun():
    a = 2
    print(f"变量a的值： {a}")
    print("这是一个方法")


print(a)
fun()
print(a)

if __name__ == '__main__':
    fun()
