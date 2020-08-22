"""Define URL patterns for credit_apply"""
from django.urls import path, include

from . import views

app_name='credit_apply'
urlpatterns = [
    path('',views.index, name='index'),
]
