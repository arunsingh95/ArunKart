from faker import Faker
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  DeleteView,
                                  View,
                                  UpdateView)
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
        """
        faker - Adding user data
        """
        # fake = Faker()
        # for i in range(50):
        #     fake_data = fake.name().split(' ')
        #     username_fake = '.'.join(fake_data).lower()
        #     password_fake = 'admin123'
        #     first_name_fake = fake_data[0]
        #     last_name_fake = fake_data[1]
        #     email_fake = fake.email()
        #     user_fake = User.objects.create_user(username_fake, email_fake, password_fake)
        #     UserDetail.objects.create(user=user_fake, first_name=first_name_fake,
        #                               last_name=last_name_fake, email=email_fake,
        #                               age=fake.random_digit(), city=fake.city(), country=fake.country(),
        #                               pin_code=fake.postalcode(), contact_number=fake.random_number(), state=fake.state(),
        #                               profile_image=fake.image_url())
        ######
        if user is not None:
            login(request, user)
            return redirect("product")
        else:
            error_message = "username or password is invalid"
            return render(request, 'mykart/login.html', {'message': error_message})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class Home(RequireLoginMixin, ListView):
    model = UserDetail
    template_name = 'mykart/home.html'
    # context_object_name = 'users'


class Users(RequireLoginMixin, ListView):
    model = UserDetail
    template_name = 'mykart/users.html'
    context_object_name = 'users'


class UserUpdate(UpdateView):
    model = UserDetail
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = "/users/"


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


class UsersTest(RequireLoginMixin, ListView):
    model = UserDetail
    template_name = 'mykart/users_test.html'
    filter_template_name = 'mykart/user_test_table.html'
    context_object_name = 'users'

    def get_queryset(self):
        first_name = self.request.GET.get("first_name")
        last_name = self.request.GET.get("last_name")
        queryset = UserDetail.objects.all()
        print(first_name)
        if first_name and last_name:
            queryset = UserDetail.objects.filter(Q(first_name__icontains=first_name) | Q(last_name__icontains=last_name))
        if first_name:
            queryset = UserDetail.objects.filter(first_name__icontains=first_name)
        if last_name:
            queryset = UserDetail.objects.filter(last_name__icontains=last_name)
        return queryset

    def get_template_names(self):
        print("###", self.request.GET.get("first_name"))
        if self.request.GET.get("first_name") or self.request.GET.get("last_name"):
            print("AAA", self.request.GET.get("first_name"))
            return self.filter_template_name
        return self.template_name
