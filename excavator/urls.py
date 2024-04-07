from django.urls import path
from . import views

urlpatterns = [
    path('', views.excavator, name='excavator')
]