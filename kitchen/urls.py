from django.urls import path

from kitchen import views


urlapatterns = [
    path("", views.index, name="index"),
]


app_name = "kitchen"
