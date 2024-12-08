from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import DishType, Dish
from accounts.models import Cook


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Cook.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.dish_type = DishType.objects.create(name="Appetizer")
        self.dish = Dish.objects.create(
            name="Caesar Salad", price=9.99, dish_type=self.dish_type
        )

    def test_index_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)


class DishTypeListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Cook.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.dish_type1 = DishType.objects.create(name="Main Course")
        self.dish_type2 = DishType.objects.create(name="Dessert")

    def test_dish_type_list_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Main Course")
        self.assertContains(response, "Dessert")

    def test_dish_type_list_view_search(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(
            reverse("kitchen:dish-type-list"), {"name": "Main"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Main Course")
        self.assertNotContains(response, "Dessert")


class ToggleCookInDishTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cook = Cook.objects.create_user(
            username="testcook", password="testpassword"
        )
        self.dish_type = DishType.objects.create(name="Main Course")
        self.dish = Dish.objects.create(
            name="Grilled Chicken", price=15.99, dish_type=self.dish_type
        )

    def test_toggle_cook_in_dish_add(self):
        self.client.login(username="testcook", password="testpassword")
        response = self.client.post(
            reverse("kitchen:dish-toggle-cook", args=[self.dish.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.cook, self.dish.cooks.all())

    def test_toggle_cook_in_dish_remove(self):
        self.dish.cooks.add(self.cook)  # Add the cook first
        self.client.login(username="testcook", password="testpassword")
        response = self.client.post(
            reverse("kitchen:dish-toggle-cook", args=[self.dish.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(self.cook, self.dish.cooks.all())
