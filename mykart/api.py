from mykart.models import (UserDetail,
                           ProductDetail)
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from mykart.serializers import (UserDetailSerializer,
                                ProductDetailSerializer)
from django_filters.rest_framework import DjangoFilterBackend


class UserDetailApi(ListCreateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer


class UserDetailUpdateApi(RetrieveUpdateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'pk'


class UserDetailDeleteApi(DestroyAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'pk'


class ProductDetailApi(ListCreateAPIView):
    queryset = ProductDetail.objects.select_related('manufacture', 'product_category')
    serializer_class = ProductDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('product_name',)


class ProductUpdateApi(RetrieveUpdateAPIView):
    queryset = ProductDetail.objects.select_related('manufacture', 'product_category')
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'


class ProductViewset(ViewSet):

    def list(self, request):
        queryset = ProductDetail.objects.all()
        serializer = ProductDetailSerializer(queryset, many=True)
        return Response(serializer.data)