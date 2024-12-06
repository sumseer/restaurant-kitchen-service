from django.db import models
from django.contrib.auth import settings


class DishType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "dish type"
        verbose_name_plural = "dish types"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType, on_delete=models.PROTECT, related_name="dishes"
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="dishes"
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self):
        return self.name
