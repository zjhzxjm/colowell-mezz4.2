from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /sample_bind/
    url(r'^$', views.index, name='index'),
    # ex: /sample_bind/results/
    url(r'^results/$', views.results, name='results'),
    # ex: /sample_bind/bind
    url(r'^bind/$', views.bind, name='bind'),
]