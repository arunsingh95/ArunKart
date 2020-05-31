from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=20, default='', blank=True)
    last_name = models.CharField(max_length=20, default='', blank=True)
    full_name = models.CharField(max_length=20, default='', blank=True)
    age = models.PositiveIntegerField(default=0, blank=True)
    email = models.EmailField(default=None, blank=True)
    city = models.CharField(max_length=25, default='', blank=True)
    state = models.CharField(max_length=25, default='', blank=True)
    country = models.CharField(max_length=25, default='', blank=True)
    pincode = models.BigIntegerField(default=0, blank=True)
    contact_number = models.BigIntegerField(default=0, blank=True)
    is_married = models.BooleanField(default=0, blank=False)

    profile_image = models.ImageField(upload_to='profile_image/', default='', blank=True)
    document = models.FileField(upload_to='document/', null=True, blank=True)

    def __str__(self):
        return self.full_name