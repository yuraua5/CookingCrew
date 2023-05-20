from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import Dish, DishType

DISH_LIST_URL = reverse("restaurant:dish-list")


class PublicDishTests(TestCase):

    def test_login_required(self):
        response = self.client.get(DISH_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="12345test",
            years_of_experience=5
        )
        self.dish_type = DishType.objects.create(name="Pasta")
        self.dish = Dish.objects.create(
            name="test dish",
            description="test description",
            price=5,
            dish_type=self.dish_type
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_list(self):
        Dish.objects.create(
            name="test dish1",
            description="test description",
            price=5,
            dish_type=self.dish_type
        )
        response = self.client.get(DISH_LIST_URL)
        dishes = Dish.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )

    def test_search_dish_list(self):
        response = self.client.get(DISH_LIST_URL, {"name": "test dish"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_list"]),
                         list(Dish.objects.filter(name="test dish")))
