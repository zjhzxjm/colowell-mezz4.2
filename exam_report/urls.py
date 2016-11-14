from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<sample_code>\d{12})/$', views.report, name='report'),
]
