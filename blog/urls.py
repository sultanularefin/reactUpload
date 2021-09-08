

from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('upload/', views.pillow, name='pillow'),

    # url(r'^$', views.index, name='index'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^user/login/$', views.login, name='login'),

]