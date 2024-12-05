from django.test import TestCase

from accounts.models import Cook


class CookModelTest(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="testcook",
            password="testpassword",
            years_of_experience=5
        )

    def test_cook_str_method(self):
        self.assertEqual(str(self.cook), "testcook")
