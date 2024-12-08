from django.test import TestCase
from django.contrib.auth import get_user_model

from kitchen.models import Dish, DishType
from kitchen.forms import DishForm, DishSearchForm, DishTypeSearchForm

class DishFormTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.dish_type = DishType.objects.create(name="Main Course")
        self.dish = Dish.objects.create(
            name="Grilled Chicken", price=15.99, dish_type=self.dish_type
        )

    def test_dish_form_valid(self):
        form_data = {
            "name": "Steak",
            "price": 20.99,
            "dish_type": self.dish_type.id,
            "cooks": [self.user.id]
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_form_invalid(self):
        form_data = {
            "name": "",
            "price": 20.99,
            "dish_type": self.dish_type.id,
            "cooks": [self.user.id]
        }
        form = DishForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_dish_form_cooks_field(self):
        form_data = {
            "name": "Steak",
            "price": 20.99,
            "dish_type": self.dish_type.id,
            "cooks": [self.user.id]
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["cooks"].count(), 1)

class DishSearchFormTest(TestCase):
    def test_dish_search_form_valid(self):
        form_data = {"name": "Chicken"}
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_search_form_invalid(self):
        form_data = {"name": ""}
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "")


class DishTypeSearchFormTest(TestCase):
    def test_dish_type_search_form_valid(self):
        form_data = {"name": "Main"}
        form = DishTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_type_search_form_invalid(self):
        form_data = {"name": ""}
        form = DishTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "")
