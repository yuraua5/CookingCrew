import re

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

from restaurant.models import Cook, Dish, DishType


def validate_first_letter_uppercase(value):
    if not value[0].isupper():
        raise ValidationError(
            "The first letter must be uppercase."
        )


def validate_letters_only(value):
    pattern = r"^[a-zA-Z\s]+$"
    if not re.match(pattern, value):
        raise ValidationError("The value must contain only letters.")


class DishForm(forms.ModelForm):
    name = forms.CharField(
        min_length=3,
        validators=[validate_first_letter_uppercase,
                    validate_letters_only],
    )
    description = forms.CharField(
        min_length=3,
        validators=[validate_first_letter_uppercase],
        widget=forms.Textarea(attrs={
            "rows": 4,
            "placeholder": "Write a short description for the dish"
        })
    )
    price = forms.IntegerField(
        validators=[MinValueValidator(1)]
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishTypeForm(forms.ModelForm):
    name = forms.CharField(
        min_length=3,
        validators=[
            validate_first_letter_uppercase,
            validate_letters_only
        ])

    class Meta:
        model = DishType
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    first_name = forms.CharField(
        min_length=3,
        required=True,
        validators=[
            validate_first_letter_uppercase,
            validate_letters_only,
        ]
    )
    last_name = forms.CharField(
        min_length=3,
        required=True,
        validators=[
            validate_first_letter_uppercase,
            validate_letters_only,
        ]
    )
    years_of_experience = forms.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(70)]
    )

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class CookUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=3,
        required=True,
        validators=[
            validate_first_letter_uppercase,
            validate_letters_only,
        ]
    )
    last_name = forms.CharField(
        min_length=3,
        required=True,
        validators=[
            validate_first_letter_uppercase,
            validate_letters_only,
        ]
    )
    years_of_experience = forms.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(70)]
    )

    class Meta:
        model = Cook
        fields = ["first_name", "last_name", "years_of_experience"]


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"})
    )
