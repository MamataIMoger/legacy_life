print("✅ Simulator URLs file is being loaded!")

from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulator_home, name='simulator_home'),
    path('result/', views.simulator_result, name='simulator_result'),
]
