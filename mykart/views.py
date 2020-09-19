from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import (ListView,
                                  DetailView,
                                  DeleteView,
                                  View)
from mykart.models import UserDetail, ProductDetail
from .mixins import RequireLoginMixin


class LoginView(View):
    def get(self, request):
        return render(request, "mykart/login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('InputPassword')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("users")
        else:
            error_message = "username or password is invalid"
            return render(request, 'mykart/login.html', {'message': error_message})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class Home(RequireLoginMixin , ListView):
    model = UserDetail
    template_name = 'mykart/home.html'
    context_object_name = 'users'


class DeleteUsers(RequireLoginMixin, DeleteView):
    model = UserDetail
    success_url = "/users/"


class Product(RequireLoginMixin, ListView):
    model = ProductDetail
    template_name = "mykart/product.html"
    context_object_name = "product"


class ProductDetails(RequireLoginMixin, DetailView):
    model = ProductDetail
    template_name = "mykart/product_details.html"
