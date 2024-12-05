from django.test import TestCase

from accounts.forms import CookCreationForm, CookSearchForm
from accounts.models import Cook


class CookCreationFormTests(TestCase):
    def test_valid_form(self):
        form_data = {
            "username": "newcook",
            "password1": "strongpassword123",
            "password2": "strongpassword123",
            "first_name": "Test",
            "last_name": "Cook",
            "years_of_experience": 5,
            "email": "newcook@example.com",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        cook = form.save()
        self.assertEqual(cook.username, "newcook")
        self.assertEqual(cook.first_name, "Test")
        self.assertEqual(cook.last_name, "Cook")
        self.assertEqual(cook.years_of_experience, 5)
        self.assertEqual(cook.email, "newcook@example.com")

    def test_invalid_password_mismatch(self):
        form_data = {
            "username": "newcook",
            "password1": "password123",
            "password2": "differentpassword123",
            "first_name": "Test",
            "last_name": "Cook",
            "years_of_experience": 5,
            "email": "newcook@example.com",
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)


class CookSearchFormTests(TestCase):
    def test_valid_search_form(self):
        form_data = {"username": "cook"}
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "cook")

    def test_empty_search_form(self):
        form_data = {"username": ""}
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "")
