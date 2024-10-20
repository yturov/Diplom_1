from data import Data
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_price(self):
        ingred = Ingredient(INGREDIENT_TYPE_FILLING, Data.COWBERRY_CREAM, Data.PRICE_COWBERRY_CREAM)
        assert ingred.get_price() == Data.PRICE_COWBERRY_CREAM

    def test_get_name(self):
        ingred = Ingredient(INGREDIENT_TYPE_SAUCE, Data.CHILI_SAUCE, Data.PRICE_CHILI_SAUCE)
        assert ingred.get_name() == Data.CHILI_SAUCE

    def test_get_type(self):
        ingred = Ingredient(INGREDIENT_TYPE_SAUCE, Data.CHILI_SAUCE, Data.PRICE_CHILI_SAUCE)
        assert ingred.get_type() == INGREDIENT_TYPE_SAUCE
