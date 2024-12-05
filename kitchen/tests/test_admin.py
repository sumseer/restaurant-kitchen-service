from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from kitchen.models import DishType, Dish
from kitchen.admin import DishTypeAdmin, DishAdmin


class MockRequest:
    pass


class DishTypeAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = DishTypeAdmin(DishType, self.site)
        self.dish_type = DishType.objects.create(name="Main Course")

    def test_list_display(self):
        self.assertEqual(self.admin.list_display, ["name"])

    def test_search_fields(self):
        self.assertEqual(self.admin.search_fields, ["name"])

    def test_queryset(self):
        queryset = self.admin.get_queryset(MockRequest())
        self.assertIn(self.dish_type, queryset)


class DishAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = DishAdmin(Dish, self.site)
        self.dish_type = DishType.objects.create(name="Appetizer")
        self.dish = Dish.objects.create(
            name="Caesar Salad",
            description="A classic Caesar salad with croutons and dressing.",
            price=9.99,
            dish_type=self.dish_type,
        )

    def test_list_display(self):
        self.assertEqual(self.admin.list_display, ["name", "price", "dish_type"])

    def test_search_fields(self):
        self.assertEqual(self.admin.search_fields, ["name", "dish_type__name"])

    def test_list_filter(self):
        self.assertEqual(self.admin.list_filter, ["dish_type"])

    def test_queryset(self):
        queryset = self.admin.get_queryset(MockRequest())
        self.assertIn(self.dish, queryset)
