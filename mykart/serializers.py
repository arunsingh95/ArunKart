from mykart.models import (UserDetail,
                           ProductDetail,
                           Manufacture,
                           ProductCategory,
                           Seller)
from rest_framework import serializers


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetail
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):
    product_image = serializers.ImageField(required=False, use_url=False)
    manufacture = serializers.SlugRelatedField(queryset=Manufacture.objects.only('company_name'), slug_field='company_name')
    product_category = serializers.SlugRelatedField(queryset=ProductCategory.objects.only('category_name'), slug_field='category_name')

    class Meta:
        model = ProductDetail
        fields = "__all__"
