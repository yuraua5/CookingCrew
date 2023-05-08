from django.contrib.auth.models import AbstractUser
from django.db import models

from restaurant_kitchen_service import settings


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        ordering = ["years_of_experience"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")

    class Meta:
        ordering = ["name"]
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self):
        return self.name
