from mykart.models import UserDetail
from rest_framework import serializers


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetail
        fields = "__all__"
