from django.conf.urls import url
from API import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^users/(?P<pk>[0-9]+)/messages$', views.all_user_messages),
    url(r'^messages/$', views.receive_message),
    url(r'^messages/(?P<pk>[0-9]+)/$', views.all_user_messages),
]