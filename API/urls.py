from django.conf.urls import url
from API import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^message/$', views.receive_message),
    url(r'^message/(?P<pk>[0-9]+)/$', views.all_user_messages),
]