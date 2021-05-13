"""
Time : 2020/11/4 23:20 
Author : Rex
File : test_demo.py
Software: PyCharm
"""
import pytest
class Testdemo():
    @pytest.fixture(scope="module")
    def first(self):
        print("module开始")
        yield
        print("module结束")

    @pytest.mark.usefixtures("first")
    def test_1(self):
        print("测试开始")


if __name__ == '__main__':
    pytest.main(["-v", "-s"])