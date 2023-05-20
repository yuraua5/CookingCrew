from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="test12345",
            years_of_experience=5
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="test",
            password="12345test",
            years_of_experience=5
        )

    def test_cook_years_of_experience_listed(self):
        url = reverse("admin:restaurant_cook_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.cook.years_of_experience)

    def test_cook_add_years_of_experience_listed(self):
        url = reverse("admin:restaurant_cook_add")
        response = self.client.get(url)
        self.assertContains(response, "First name:")
        self.assertContains(response, "Last name:")
        self.assertContains(response, "Years of experience:")

    def test_cook_detail_license_number_listed(self):
        url = reverse("admin:restaurant_cook_change", args=[self.cook.id])
        response = self.client.get(url)
        self.assertContains(response, self.cook.years_of_experience)
