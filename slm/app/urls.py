from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^answers/$', views.get_answers),
    url(r'^home/$', views.home),
    url(r'^sync/$', views.db),
    url(r'^getTerms/$', views.get_terms),
    url(r'^getHeaders/$', views.get_headers)
]