from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, default='', blank=True)
    last_name = models.CharField(max_length=20, default='', blank=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        super(UserDetail, self).save(*args, **kwargs)

    full_name = models.CharField(max_length=50, default='', blank=True)
    age = models.PositiveIntegerField(default=0, blank=True)
    email = models.EmailField(default=None, blank=True)
    city = models.CharField(max_length=25, default='', blank=True)
    state = models.CharField(max_length=25, default='', blank=True)
    country = models.CharField(max_length=25, default='', blank=True)
    pin_code = models.BigIntegerField(default=0, blank=True)
    contact_number = models.BigIntegerField(default=0, blank=True)
    is_married = models.BooleanField(default=0, blank=False)

    profile_image = models.ImageField(upload_to='profile_image/', default='', blank=True)
    document = models.FileField(upload_to='document/', null=True, blank=True)

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=User)
def save_user_userdetail(sender, instance, **kwargs):
    instance.userdetail.save()


class Manufacture(models.Model):
    company_name = models.CharField(max_length=200, default='', blank=True)
    owner_name = models.CharField(max_length=200, default='', blank=True)
    area = models.CharField(max_length=200, default='', blank=True)
    city = models.CharField(max_length=200, default='', blank=True)
    state = models.CharField(max_length=200, default='', blank=True)
    country = models.CharField(max_length=200, default='', blank=True)
    pin_code = models.BigIntegerField(default=0, blank=True)

    def __str__(self):
        return self.company_name


class Seller(models.Model):
    seller_company_name = models.CharField(max_length=250, default='', blank=True)
    seller_name = models.CharField(max_length=200, default='', blank=True)
    area = models.CharField(max_length=200, default='', blank=True)
    city = models.CharField(max_length=200, default='', blank=True)
    state = models.CharField(max_length=200, default='', blank=True)
    country = models.CharField(max_length=200, default='', blank=True)
    pin_code = models.BigIntegerField(default=0, blank=True)

    def __str__(self):
        return self.company_name


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.category_name


class ProductDetail(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, related_name='+')
    product_name = models.CharField(max_length=200, default='', blank=True)
    price = models.PositiveIntegerField(default=0, blank=True)
    quantity = models.PositiveIntegerField(default=0, blank=True)
    discount = models.PositiveIntegerField(default=0, blank=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, related_name='+')
    product_seller = models.ManyToManyField(Seller, blank=True)
    # product_image = models.ImageField(upload_to='product_image/', default='', blank=True)
    product_image = ProcessedImageField(upload_to='product_image',
                                        processors=[ResizeToFill(100, 100)],
                                        format='JPEG',
                                        options={'quality': 60},
                                        null=True)

    def __str__(self):
        return self.product_name


class PurchaseLog(models.Model):
    buyer = models.ForeignKey(UserDetail, on_delete=models.DO_NOTHING, related_name='+')
    product = models.ForeignKey(ProductDetail, on_delete=models.DO_NOTHING, related_name='+')
    quantity_purchase = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.buyer.full_name}_{self.product.product_name}_{self.quantity_purchase}"


class AddToKart(models.Model):
    user = models.ForeignKey('UserDetail', on_delete=models.DO_NOTHING, related_name='+')
    product = models.ForeignKey(ProductDetail, on_delete=models.DO_NOTHING, related_name='+')
    quantity_added = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.user.full_name}_{self.product.product_name}_{self.quantity_added}"


class Task(models.Model):
    task = models.CharField(max_length=100, primary_key=True)
    task_start_date = models.DateField(null=True, blank=True)
    task_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.task
