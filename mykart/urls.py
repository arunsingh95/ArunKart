from django.conf.urls import url
from mykart import views
from mykart import api

urlpatterns = [
    # URLS
    url(r'^$', views.Home.as_view(), name='home'),

    #API's
    url(r'^api/user_details/$', api.UserDetailApi.as_view(), name='user_detail_api'),
    url(r'^api/user_details/edit/(?P<pk>\d+)$', api.UserDetailUpdateApi.as_view(), name='user_detail_update_api')
]
