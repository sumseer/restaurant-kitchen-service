from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Cook
from kitchen.models import DishType, Dish


def index(request: HttpRequest) -> HttpResponse:
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_visits": num_visits + 1,
    }
    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_types"
    paginate_by = 5


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishListView(generic.ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"
    context_object_name = "dishes"
    paginate_by = 5



class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"
    context_object_name = "dish"


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-list")
