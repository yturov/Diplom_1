import pytest
from data import Data
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', [(Data.TASTY_BUN, Data.PRICE_TASTY_BUN),
                                             (Data.TASTELESS_BUN, Data.PRICE_TASTELESS_BUN)
                                             ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert type(bun.get_name()) == str

    @pytest.mark.parametrize('name, price', [(Data.TASTY_BUN, Data.PRICE_TASTY_BUN),
                                             (Data.TASTELESS_BUN, Data.PRICE_TASTELESS_BUN)
                                             ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
        assert type(bun.get_price()) == float
