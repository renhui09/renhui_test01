'''
发礼物
1、拥有礼物的标识
2、定义一个发礼物的方法
3、定义一个展示礼物的方法
4、启动方法
'''

# 拥有礼物的标识
have_git = False


# 发礼物的方法
def send():
    print("发礼物啦")
    global have_git
    have_git = True


# 展示礼物
def show():
    if have_git == True:
        print("收到礼物啦，好开心～")
    else:
        print("没有礼物")


if __name__ == '__main__':
    send()
    show()
