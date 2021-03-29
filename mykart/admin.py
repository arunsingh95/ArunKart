from django.contrib import admin
# from import_export import resources
from mykart.models import (UserDetail,
                           ProductDetail,
                           Manufacture,
                           Seller,
                           ProductCategory,
                           AddToKart,
                           Task)
from django.utils.html import format_html


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ("pro_image", "product_name", "price", "manufacture", "quantity")

    def pro_image(self, obj):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.product_image.url))


admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(UserDetail)
admin.site.register(Manufacture)
admin.site.register(Seller)
admin.site.register(ProductCategory)
admin.site.register(AddToKart)
admin.site.register(Task)
