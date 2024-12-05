from django.test import TestCase
from django.urls import reverse

from accounts.models import Cook


class CookListViewTests(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(username="testuser", password="testpass")
        Cook.objects.create(username="cook1", years_of_experience=3)
        Cook.objects.create(username="cook2", years_of_experience=5)
        self.client.login(username="testuser", password="testpass")

    def test_cook_list_view(self):
        response = self.client.get(reverse("accounts:cook-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/cook_list.html")
        self.assertContains(response, "cook1")
        self.assertContains(response, "cook2")

    def test_cook_list_search(self):
        response = self.client.get(reverse("accounts:cook-list"), {"username": "cook1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cook1")
        self.assertNotContains(response, "cook2")


class AddYearOfExperienceViewTests(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(username="testuser", password="testpass")
        self.cook = Cook.objects.create(username="cook1", years_of_experience=3)
        self.client.login(username="testuser", password="testpass")

    def test_add_year_of_experience(self):
        response = self.client.post(reverse("accounts:cook-add-year", args=[self.cook.pk]))
        self.cook.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.cook.years_of_experience, 4)
