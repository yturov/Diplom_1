from data import Data
from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self):
        data = Database()
        buns = data.available_buns()
        assert buns[0].name == Data.BLACK_BUN

    def test_available_ingredients(self):
        data = Database()
        ingredients = data.available_ingredients()
        assert ingredients[2].name == Data.CHILI_SAUCE
