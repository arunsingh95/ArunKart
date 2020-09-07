from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView)
from mykart.models import UserDetail, ProductDetail


class Home(ListView):
    model = UserDetail
    template_name = 'mykart/home.html'
    context_object_name = 'users'


class Product(ListView):
    model = ProductDetail
    template_name = "mykart/product.html"
    context_object_name = "product"


class ProductDetails(DetailView):
    model = ProductDetail
    template_name = "mykart/product_details.html"
