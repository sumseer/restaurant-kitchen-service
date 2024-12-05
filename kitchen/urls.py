from django.urls import path

from kitchen import views
from kitchen.views import toggle_cook_in_dish

app_name = "kitchen"


urlpatterns = [
    path("", views.index, name="index"),
    path("dish-types/", views.DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/create/", views.DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-types/<int:pk>/update/", views.DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish-types/<int:pk>/delete/", views.DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dish/<int:pk>/toggle-cook/", toggle_cook_in_dish, name="dish-toggle-cook"),

    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", views.DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", views.DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", views.DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", views.DishDeleteView.as_view(), name="dish-delete"),
]
