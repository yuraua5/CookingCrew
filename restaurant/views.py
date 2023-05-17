from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant.models import DishType, Dish, Cook


@login_required
def index(request):
    num_dish_types = DishType.objects.count()
    num_cooks = get_user_model().objects.count()
    num_dishes = Dish.objects.count()

    context = {
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
    }
    return render(request, "restaurant/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "restaurant/dish_type_list.html"
    paginate_by = 5


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "restaurant/dish_type_form.html"
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "restaurant/dish_type_form.html"
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    template_name = "restaurant/dish_type_confirm_delete.html"
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-list")


class DishDetailView(generic.DetailView):
    model = Dish


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant:dish-list")

class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5


class CookCreateView(generic.CreateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("restaurant:cook-list")


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "restaurant/cook_detail.html"


class CookUpdateView(generic.UpdateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("restaurant:cook-list")


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("restaurant:cook-list")
