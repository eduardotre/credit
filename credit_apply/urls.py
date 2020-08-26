"""Define URL patterns for credit_apply"""
from django.urls import path

from . import views

app_name = 'credit_apply'
urlpatterns = [
    path('', views.index, name='index'),
    # path to apply for credit
    path('apply/', views.apply, name='apply'),
    # path after succesful submission
    path('submitted/', views.submitted, name='submitted')
]
