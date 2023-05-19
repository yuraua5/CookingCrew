from django.test import TestCase
from restaurant.forms import CookCreationForm, CookUpdateForm


class FormsTests(TestCase):
    def setUp(self):
        self.form_data_cook_creation = {
            "username": "test_user",
            "password1": "passtest123",
            "password2": "passtest123",
            "first_name": "Ivan",
            "last_name": "Testovuy",
            "years_of_experience": 5
        }
        self.form_data_cook_update = {
            "first_name": "Ivan",
            "last_name": "Testovuy",
            "years_of_experience": 5
        }

    def test_cook_creation_form(self):
        form = CookCreationForm(data=self.form_data_cook_creation)
        self.assert_(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data_cook_creation)

    def test_validate_cook_creation_form_first_name_len(self):
        self.form_data_cook_creation["first_name"] = "Iv"
        form = CookCreationForm(self.form_data_cook_creation)
        self.assertFalse(form.is_valid())

    def test_validate_cook_creation_form_last_name_len(self):
        self.form_data_cook_creation["last_name"] = "Te"
        form = CookCreationForm(self.form_data_cook_creation)
        self.assertFalse(form.is_valid())

    def test_validate_cook_creation_form_first_name_letter_uppercase(self):
        self.form_data_cook_creation["first_name"] = "ivan"
        form = CookCreationForm(self.form_data_cook_creation)
        self.assertFalse(form.is_valid())

    def test_validate_cook_creation_form_last_name_letter_uppercase(self):
        self.form_data_cook_creation["last_name"] = "testovuy"
        form = CookCreationForm(self.form_data_cook_creation)
        self.assertFalse(form.is_valid())

    def test_validate_cook_creation_form_first_name_letters_only(self):
        self.form_data_cook_creation["first_name"] = "Ivan1"
        form = CookCreationForm(self.form_data_cook_creation)
        self.assertFalse(form.is_valid())

    def test_validate_cook_creation_form_last_name_letters_only(self):
        self.form_data_cook_creation["last_name"] = "Testovuy1"
        form = CookCreationForm(self.form_data_cook_creation)
        self.assertFalse(form.is_valid())

    def test_validate_cook_creation_form_min_value_years_of_experience(self):
        self.form_data_cook_creation["years_of_experience"] = -5
        form = CookCreationForm(self.form_data_cook_creation)
        self.assertFalse(form.is_valid())

    def test_validate_cook_creation_form_max_value_years_of_experience(self):
        self.form_data_cook_creation["years_of_experience"] = 71
        form = CookCreationForm(self.form_data_cook_creation)
        self.assertFalse(form.is_valid())

    def test_cook_update_form(self):
        form = CookUpdateForm(data=self.form_data_cook_update)
        self.assert_(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data_cook_update)

    def test_validate_cook_update_form_first_name_len(self):
        self.form_data_cook_creation["first_name"] = "Iv"
        form = CookCreationForm(self.form_data_cook_update)
        self.assertFalse(form.is_valid())

    def test_validate_cook_update_form_last_name_len(self):
        self.form_data_cook_creation["last_name"] = "Te"
        form = CookCreationForm(self.form_data_cook_update)
        self.assertFalse(form.is_valid())

    def test_validate_cook_update_form_first_name_letter_uppercase(self):
        self.form_data_cook_creation["first_name"] = "ivan"
        form = CookCreationForm(self.form_data_cook_update)
        self.assertFalse(form.is_valid())

    def test_validate_cook_update_form_last_name_letter_uppercase(self):
        self.form_data_cook_creation["last_name"] = "testovuy"
        form = CookCreationForm(self.form_data_cook_update)
        self.assertFalse(form.is_valid())

    def test_validate_cook_update_form_first_name_letters_only(self):
        self.form_data_cook_creation["first_name"] = "Ivan1"
        form = CookCreationForm(self.form_data_cook_update)
        self.assertFalse(form.is_valid())

    def test_validate_cook_update_form_last_name_letters_only(self):
        self.form_data_cook_creation["last_name"] = "Testovuy1"
        form = CookCreationForm(self.form_data_cook_update)
        self.assertFalse(form.is_valid())

    def test_validate_cook_update_form_min_value_years_of_experience(self):
        self.form_data_cook_creation["years_of_experience"] = -5
        form = CookCreationForm(self.form_data_cook_update)
        self.assertFalse(form.is_valid())

    def test_validate_cook_update_form_max_value_years_of_experience(self):
        self.form_data_cook_creation["years_of_experience"] = 71
        form = CookCreationForm(self.form_data_cook_update)
        self.assertFalse(form.is_valid())
