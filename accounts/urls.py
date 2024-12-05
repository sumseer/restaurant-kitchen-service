from django.urls import path, include

from accounts import views
from accounts.views import add_year_of_experience

app_name = "accounts"


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("cooks/", views.CookListView.as_view(), name="cook-list"),
    path("<int:pk>/", views.CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create", views.CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update", views.CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete", views.CookDeleteView.as_view(), name="cook-delete"),
    path("cook/<int:pk>/increment-years/", add_year_of_experience, name="cook-add-year"),
]
