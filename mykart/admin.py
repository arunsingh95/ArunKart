from django.contrib import admin
# from import_export import resources
from mykart.models import (UserDetail,
                           ProductDetail,
                           Manufacture,
                           Seller,
                           ProductCategory)


admin.site.register(UserDetail)
admin.site.register(ProductDetail)
admin.site.register(Manufacture)
admin.site.register(Seller)
admin.site.register(ProductCategory)


# class UseDetailResources(resources.ModelResource):
#
#     class Meta:
#         model = UserDetail
