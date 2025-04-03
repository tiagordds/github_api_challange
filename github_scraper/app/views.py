from django.shortcuts import render

from .models import UserInfo


def user_list(request):
    users = UserInfo.objects.all()
    return render(request, "app/users_list.html", {"users": users})
