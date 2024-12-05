from django.test import TestCase

from kitchen.models import DishType, Dish


class DishTypeModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")

    def test_dish_type_str_method(self):
        self.assertEqual(str(self.dish_type), "Main Course")


class DishModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Appetizer")
        self.dish = Dish.objects.create(
            name="Caesar Salad",
            description="A classic Caesar salad with croutons and dressing.",
            price=9.99,
            dish_type=self.dish_type,
        )

    def test_dish_str_method(self):
        self.assertEqual(str(self.dish), "Caesar Salad")
