from django.urls import path
from . import views

app_name = 'pledges'

urlpatterns = [
    path('form/', views.pledge_form, name='pledge_form'),
]
