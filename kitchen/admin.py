from django.contrib import admin
from kitchen.models import DishType, Dish


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "dish_type"]
    search_fields = ["name", "dish_type__name"]
    list_filter = ["dish_type"]
