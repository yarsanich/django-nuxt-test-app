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

        self.recipe_raw_data = {
            'name': 'test',
            'prep_time': 1,
            'difficulty': Recipe.DIFFICULTY_LEVELS[0],
            'ingredients': 'test',
            'prep_guide': 'test'
        }

    def test_get_recipes(self):
        response = self.client.get(self.URL)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.json()), self.NUMBER_OF_RECIPES)

    def test_create_recipe(self):
        response = self.client.post(self.URL, self.recipe_raw_data)

        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_delete_recipe(self):
        pass

    def test_update_recipe(self):
        pass