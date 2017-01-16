from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^answers/$', views.get_answers),
    # url(r'^answers/$', views.hey),
    url(r'^home/$', views.home)
]