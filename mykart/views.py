from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  DeleteView,
                                  View)
from mykart.models import (UserDetail,
                           ProductDetail,
                           ProductCategory,
                           Manufacture)
from .mixins import RequireLoginMixin


class RegisterView(View):
    def get(self, request):
        return render(request, 'mykart/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('InputPassword')
        confirm_password = request.POST.get('confirmInputPassword')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if not User.objects.filter(username=username).exists():
            if password == confirm_password:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                UserDetail.objects.create(user=user, first_name=first_name, last_name=last_name, email=email)
                return redirect('/')
            else:
                error_message = "password and current password do not match"
        else:
            error_message = "user with this username already exists"
        context = {
            'message': error_message
        }
        return render(request, 'mykart/register.html', context)


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
    # context_object_name = "product"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = ProductDetail.objects.all()
        context["category"] = ProductCategory.objects.all()
        context["manufacture"] = Manufacture.objects.all()
        return context


class ProductDetails(RequireLoginMixin, DetailView):
    model = ProductDetail
    template_name = "mykart/product_details.html"

