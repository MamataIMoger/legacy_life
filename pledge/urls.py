from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_pledge, name='make_pledge'),
]
