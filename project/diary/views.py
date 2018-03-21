from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day

class IndexView(generic.ListView):
    model = Day
    paginate_by = 3

class AddView(generic.CreateView):
    model = Day
    form_class = DayCreateForm
    # fields = '__all__'
    success_url = reverse_lazy('diary:index') # リダイレクト


class UpdateView(generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')


class DeleteView(generic.DeleteView):
    model = Day
    seccess_url = reverse_lazy('diary:index')


class DetailView(generic.DetailView):
    model = Day
