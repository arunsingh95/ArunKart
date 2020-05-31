from django.contrib import admin
# from import_export import resources
from mykart.models import UserDetail


admin.site.register(UserDetail)


# class UseDetailResources(resources.ModelResource):
#
#     class Meta:
#         model = UserDetail
