from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url("index", views.index, name='index'),
    url("vacation_update", views.vacation_update, name='vacation_update'),
    url("delete_vacation", views.delete_vacation, name='delete_vacation'),
]
