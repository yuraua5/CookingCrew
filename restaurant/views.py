from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "restaurant/dish_type_form.html"


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "restaurant/dish_type_form.html"


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    template_name = "restaurant/dish_type_confirm_delete.html"


class DishListView(generic.ListView):
    model = Dish


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"


class DishDeleteView(generic.DeleteView):
    model = Dish


class CookListView(generic.ListView):
    model = Cook


class CookCreateView(generic.CreateView):
    model = Cook
    fields = "__all__"


class CookUpdateView(generic.UpdateView):
    model = Cook
    fields = "__all__"


class CookDeleteView(generic.DeleteView):
    model = Cook
