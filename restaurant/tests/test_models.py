from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import DishType, Dish


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Pasta")
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="test",
            password="123456test",
            first_name="Ivan",
            last_name="Testovuy",
            years_of_experience=1
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Pasta")
        dish = Dish.objects.create(
            name="test dish",
            description="test description",
            price=5,
            dish_type=dish_type
        )
        self.assertEqual(str(dish), dish.name)

    def test_create_cook_with_years_of_experience(self):
        username = "test"
        password = "123456test"
        years_of_experience = 1
        cook = get_user_model().objects.create_user(
            username="test",
            password="123456test",
            years_of_experience=1
        )
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
