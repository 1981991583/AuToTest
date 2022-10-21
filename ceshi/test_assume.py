import pytest
from pytest import assume
from sql.mapper import Mapper

class Test():

    def test_01(self):
        conn = Mapper()
        re1 = conn.select_card_no()
        card = 'ceshi'
        """用例1"""
        print('执行test_01断言1')
        print(card)
        assert card in re1


if __name__ == '__main__':
    pytest.main(['-s', 'test_assume.py'])