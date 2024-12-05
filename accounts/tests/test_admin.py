from django.contrib.admin import site
from django.test import TestCase

from accounts.models import Cook
from accounts.admin import CookAdmin


class CookAdminTests(TestCase):
    def test_cook_model_registered(self):
        self.assertIn(Cook, site._registry)
        self.assertIsInstance(site._registry[Cook], CookAdmin)

    def test_list_display(self):
        admin_instance = site._registry[Cook]
        self.assertIn("years_of_experience", admin_instance.list_display)

    def test_search_fields(self):
        admin_instance = site._registry[Cook]
        self.assertEqual(
            admin_instance.search_fields,
            ["username", "first_name", "last_name", "years_of_experience"],
        )
