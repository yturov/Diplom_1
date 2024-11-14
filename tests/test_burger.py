from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from data import Data


class TestBurger:

    def test_set_buns(self):
        mock = Mock()
        burger = Burger()
        mock.get_name.return_value = Data.TASTELESS_BUN
        mock.get_price.return_value = Data.PRICE_TASTELESS_BUN
        burger.set_buns(mock)
        assert burger.bun.get_name() == Data.TASTELESS_BUN
        assert burger.bun.get_price() == Data.PRICE_TASTELESS_BUN

    def test_add_ingredient(self):
        mock = Mock()
        burger = Burger()
        mock.get_name.return_value = Data.FIRST_SAUCE
        mock.get_price.return_value = Data.PRICE_FIRST_SAUCE
        mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock)
        assert burger.ingredients == [mock]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.FIRST_SAUCE, Data.PRICE_FIRST_SAUCE)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingred0 = Ingredient(INGREDIENT_TYPE_SAUCE, Data.FIRST_SAUCE, Data.PRICE_FIRST_SAUCE)
        ingred1 = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SECOND_SAUCE, Data.PRICE_SECOND_SAUCE)
        burger.add_ingredient(ingred0)
        burger.add_ingredient(ingred1)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].name == Data.SECOND_SAUCE
        assert burger.ingredients[1].price == Data.PRICE_FIRST_SAUCE

    def test_get_price(self):
        burger = Burger()
        bun = Bun(Data.TASTY_BUN, Data.PRICE_TASTY_BUN)
        burger.set_buns(bun)
        sauce_1 = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SECOND_SAUCE, Data.PRICE_SECOND_SAUCE)
        burger.add_ingredient(sauce_1)
        assert burger.get_price() == 37.0
        assert type(burger.get_price()) == float

    def test_get_receipt(self):
        mock = Mock()
        burger = Burger()
        mock.get_name.return_value = Data.TASTY_BUN
        mock.get_price.return_value = Data.PRICE_TASTY_BUN
        burger.set_buns(mock)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SECOND_SAUCE, Data.PRICE_SECOND_SAUCE)
        burger.add_ingredient(sauce)
        assert burger.get_receipt() == Data.RECEIPT
