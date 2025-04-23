from django.core.paginator import Paginator
from django.shortcuts import render

from .models import UserInfo


def user_list(request):
    user_list = UserInfo.objects.all().order_by("id")
    paginator = Paginator(user_list, 50)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "app/users_list.html", {"page_obj": page_obj})


def full_user_list(request):
    full_user_list = UserInfo.objects.all().order_by("id")
    paginator = Paginator(full_user_list, 50)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "app/full_user_list.html", {"page_obj": page_obj})
