import pytest


class TestDepends:

    def test_method1(self):
        print("Test method-1 is called")

    @pytest.mark.dependency()
    def test_method2(self):
        print("Test method-2 is called")
        assert 1 + 5 == 6

    @pytest.mark.dependency(depends=["TestDepends::test_method2"])
    def test_method3(self):
        print("Test method-3 is called")


class TestNew:
    @pytest.mark.dependency(depends=["TestDepends::test_method2"])
    def test_method4(self):
        print("Test method-4 is called")
