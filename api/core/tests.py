from http import HTTPStatus

from django.test import TestCase
from .models import Recipe

class TestRecipes(TestCase):
    NUMBER_OF_RECIPES = 5
    URL = '/api/recipes/'

    def setUp(self):
        for index in range(self.NUMBER_OF_RECIPES):
            Recipe.objects.create(
                name=f"Recipe {index}",
                difficulty=Recipe.DIFFICULTY_LEVELS[0],
                ingredients="i, a, b",
                prep_time=index
            )


    def test_get_recipes(self):
        response = self.client.get(self.URL)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.json()), self.NUMBER_OF_RECIPES)

    def test_create_recipe(self):
        pass

    def test_delete_recipe(self):
        pass

    def test_update_recipe(self):
        pass