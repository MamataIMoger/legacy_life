from django.urls import path
from . import views

app_name = "important_dates"

urlpatterns = [
    path("", views.important_dates_view, name="important_dates_list"),

]
