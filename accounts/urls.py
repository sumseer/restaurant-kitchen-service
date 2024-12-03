from django.urls import path, include

from accounts import views


urlapatterns = [
    path("", views.index, name="index"),
]


app_name = "accounts"
