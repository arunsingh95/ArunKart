from mykart.models import UserDetail
from rest_framework.generics import ListCreateAPIView,UpdateAPIView
from mykart.serializers import UserDetailSerializer
from rest_framework.response import Response
from rest_framework import status


class UserDetailApi(ListCreateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer


class UserDetailUpdateApi(UpdateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
