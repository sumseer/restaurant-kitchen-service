from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import CookCreationForm
from accounts.models import Cook


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "accounts/cook_list.html"
    context_object_name = "cooks"
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "accounts/cook_detail.html"
    context_object_name = "cook"


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    template_name = "accounts/cook_form.html"
    success_url = reverse_lazy("accounts:cook-list")
    form_class = CookCreationForm

class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    template_name = "accounts/cook_form.html"
    success_url = reverse_lazy("accounts:cook-list")
    form_class = CookCreationForm


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "accounts/cook_confirm_delete.html"
    success_url = reverse_lazy("accounts:cook-list")
