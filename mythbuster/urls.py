from django.urls import path
from . import views

urlpatterns = [
    path('', views.myths_view, name='myths'),
]
