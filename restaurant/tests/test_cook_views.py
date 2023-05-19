from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

COOK_LIST_URL = reverse("restaurant:cook-list")


class PublicCookTests(TestCase):

    def test_login_required(self):
        response = self.client.get(COOK_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateCookTests(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="test",
            password="123456test",
            years_of_experience=5
        )
        self.client.force_login(self.cook)

    def test_retrieve_cook_list(self):
        get_user_model().objects.create_user(
            username="test1",
            password="123456test2",
            years_of_experience=3
        )
        response = self.client.get(COOK_LIST_URL)
        cooks = get_user_model().objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks)
        )

    def test_create_cook(self):
        form_data = {
            "username": "test_user",
            "password1": "passtest123",
            "password2": "passtest123",
            "first_name": "Ivan",
            "last_name": "Testovuy",
            "years_of_experience": 5
        }
        self.client.post(reverse("restaurant:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(
            new_user.years_of_experience,
            form_data["years_of_experience"]
        )

    def test_search_cook_list(self):
        response = self.client.get(COOK_LIST_URL, {"username": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(get_user_model().objects.filter(username="test"))
        )
