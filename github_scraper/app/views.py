from django.core.paginator import Paginator
from django.shortcuts import render

from .models import UserInfo


def user_list(request):
    user_list = UserInfo.objects.all().order_by("id")
    per_page = request.GET.get("per_page", 50)
    per_page_options = [10, 25, 50, 75, 100]
    per_page = int(per_page)
    if per_page not in per_page_options:
        per_page = 50

    user_search = request.GET.get("search", "")
    search_type = request.GET.get("search_type", "contains")
    if user_search:
        if search_type == "startswith":
            user_list = user_list.filter(login__istartswith=user_search)
        elif search_type == "contains":
            user_list = user_list.filter(login__icontains=user_search)

    paginator = Paginator(user_list, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "app/users_list.html",
        {
            "page_obj": page_obj,
            "per_page": per_page,
            "per_page_options": per_page_options,
            "user_search": user_search,
            "search_type": search_type,
        },
    )


def full_user_list(request):
    full_user_list = UserInfo.objects.all().order_by("id")
    per_page = request.GET.get("per_page", 50)
    per_page_options = [10, 25, 50, 75, 100]
    per_page = int(per_page)
    if per_page not in per_page_options:
        per_page = 50

    user_search = request.GET.get("search", "")
    search_type = request.GET.get("search_type", "contains")
    if user_search:
        if search_type == "startswith":
            full_user_list = full_user_list.filter(login__istartswith=user_search)
        elif search_type == "contains":
            full_user_list = full_user_list.filter(login__icontains=user_search)

    paginator = Paginator(full_user_list, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "app/full_user_list.html",
        {
            "page_obj": page_obj,
            "per_page": per_page,
            "per_page_options": per_page_options,
            "user_search": user_search,
            "search_type": search_type,
        },
    )
