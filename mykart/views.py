from django.shortcuts import render
from django.views.generic import ListView
from mykart.models import UserDetail


class Home(ListView):
    model = UserDetail
    template_name = 'mykart/home.html'
