from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Cook


class CookListView(generic.ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"
    context_object_name = "cooks"
    paginate_by = 5


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"
    context_object_name = "cook"


class CookCreateView(generic.CreateView):
    model = Cook
    template_name = "kitchen/cook_form.html"
    fields = "__all__"
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(generic.UpdateView):
    model = Cook
    template_name = "kitchen/cook_form.html"
    fields = "__all__"
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(generic.DeleteView):
    model = Cook
    template_name = "kitchen/cook_confirm_delete.html"
    success_url = reverse_lazy("kitchen:cook-list")
