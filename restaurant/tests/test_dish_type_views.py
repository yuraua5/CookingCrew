from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import DishType

DISH_TYPE_LIST_URL = reverse("restaurant:dish-type-list")


class PublicDishTypeTests(TestCase):

    def test_login_required(self):
        response = self.client.get(DISH_TYPE_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="12345test",
            years_of_experience=5
        )
        self.dish_type = DishType.objects.create(name="Pasta")
        self.client.force_login(self.user)

    def test_retrieve_dish_type_list(self):
        DishType.objects.create(name="Pizza")
        response = self.client.get(DISH_TYPE_LIST_URL)
        dish_types = DishType.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dishtype_list"]),
            list(dish_types)
        )

    def test_search_dish_type_list(self):
        response = self.client.get(DISH_TYPE_LIST_URL, {"name": "Pasta"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dishtype_list"]),
                         list(DishType.objects.filter(name="Pasta")))
