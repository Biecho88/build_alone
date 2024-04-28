from django.urls import path
from . import views

urlpatterns = [
    path('', views.excavator, name='excavator'),
    path('add/', views.add_excavator, name='add_excavator'),
]
