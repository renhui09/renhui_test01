def setup_function():
    print("函数级别 setup")


def teardown_function():
    print("函数级别 teardown")


def test_fun1():
    print("测试函数1")


class TestDemo:

    def setup_class(self):
        print("类级别的 setup")

    def teardown_class(self):
        print("类级别的 teardown")

    def setup(self):
        print("方法级别的 setup")

    def teardown(self):
        print("方法级别的 teardown")

    def test_demo1(self):
        print("test_demo1")

    def test_demo2(self):
        print("test_demo2")
