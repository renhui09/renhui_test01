import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)


def test_a():
    print("测试用例a")


class TestCalc:
    def setup_class(self):
        # 实例化计算器
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    #  参数化，a,b是参数，expect是预期结果
    # ids是给用来命名
    # @pytest.mark.parametrize(
    #     "a,b,expect",
    #     [
    #         (1,1,2),
    #         (0.1,0.1,0.2),
    #         (-1,-1,-2),
    #         (0.1,0.2,0.3)
    #     ],ids=['int','float','negative','round']
    # )

    # yaml方式
    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas, ids=myid
    )
    def test_add4(self, a, b, expect):
        result = self.calc.add(a, b)
        # 判断是否是浮点数
        if isinstance(result, float):
            result = round(result, 2)

        assert result == expect

    # #由于float会丢位，所以用round函数，保留两位
    # def test_add5(self):
    #     result = self.calc.add(0.1,0.2)
    #     assert round(result,2)==0.3

    # def test_add(self):
    #     # #实例化计算器
    #     # calc = Calculator()
    #     #调用add方法
    #     result = self.calc.add(1,1)
    #
    #     #得到结果后，需要写短言
    #     assert result==2
    #
    # def test_add1(self):
    #     #实例化计算器
    #     # calc = Calculator()
    #     #调用add方法
    #     result = self.calc.add(0.1,0.1)
    #
    #     #得到结果后，需要写短言
    #     assert result==0.2
    #
    # def test_add2(self):
    #     #实例化计算器
    #     # calc = Calculator()
    #     #调用add方法
    #     result = self.calc.add(-1,-1)
    #
    #     #得到结果后，需要写短言
    #     assert result==-2

    @pytest.mark.parametrize('a', [1, 2, 3])
    @pytest.mark.parametrize('b', [4, 5, 6])
    def test_param(self, a, b):
        print(f"a={a},b={b}")
