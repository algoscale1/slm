from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^qna$', views.main_function),
    url(r'^answers/$', views.hey),
    url(r'^home/$', views.home)
]