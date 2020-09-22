from django.conf.urls import url, include
from mykart import views
from mykart import api

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', api.ProductViewset, basename='products')

urlpatterns = [
    # URLS
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^users/$', views.Home.as_view(), name='users'),
    url(r'^delete_users/(?P<pk>\d+)$', views.DeleteUsers.as_view(), name='delete'),
    url(r'^product/$', views.Product.as_view(), name='product'),
    url(r'^product_details/(?P<pk>\d+)$', views.ProductDetails.as_view(), name='product_details'),

    #API's
    url(r'^api/user_details/$', api.UserDetailApi.as_view(), name='user_detail_api'),
    url(r'^api/user_details/edit/(?P<pk>\d+)$', api.UserDetailUpdateApi.as_view(), name='user_detail_update_api'),
    url(r'^api/user_details/delete/(?P<pk>\d+)$', api.UserDetailDeleteApi.as_view(), name='user_detail_delete_api'),
    url(r'^api/products/$', api.ProductDetailApi.as_view(), name='products_api'),
    url(r'^api/products/edit/(?P<pk>\d+)$', api.ProductUpdateApi.as_view(), name='product_update_api'),
    # url(r'^', include(router.urls)),
]
