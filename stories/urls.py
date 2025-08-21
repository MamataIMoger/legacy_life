from django.urls import path
from . import views

app_name = "stories"

urlpatterns = [
    path("", views.story_list, name="list"),
    path("submit/", views.story_submit, name="submit"),
    path("portal/", views.story_list, name="portal"),  # ✅ alias
]
