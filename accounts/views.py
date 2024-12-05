from lib2to3.fixes.fix_input import context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import CookCreationForm, CookSearchForm
from accounts.models import Cook


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "accounts/cook_list.html"
    context_object_name = "cooks"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        search_name = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"username": search_name}
        )
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        search_name = self.request.GET.get("username")
        if search_name:
            return queryset.filter(username__icontains=search_name)
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "accounts/cook_detail.html"
    context_object_name = "cook"
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


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


def add_year_of_experience(request, pk):
    cook = get_object_or_404(Cook, pk=pk)
    cook.years_of_experience += 1
    cook.save()
    return redirect("accounts:cook-detail", pk=cook.pk)
