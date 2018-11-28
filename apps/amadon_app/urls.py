from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^amadon$', views.index),
    url(r'^amadon/process$', views.process),
    url(r'^amadon/checkout$', views.checkout),
]