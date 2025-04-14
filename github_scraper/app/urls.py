from django.urls import path

from .views import full_user_list, user_list

urlpatterns = [
    path("", user_list, name="user_list"),
    path("full/", full_user_list, name="full_user_list"),
]
