from django.core.paginator import Paginator
from django.shortcuts import render

from .models import UserInfo

PER_PAGE_OPTIONS = [10, 25, 50, 100]


def get_per_page(request):
    per_page = int(request.GET.get("per_page", 50))
    if per_page not in PER_PAGE_OPTIONS:
        per_page = per_page
    return per_page


def get_user_search(queryset, request):
    user_search = request.GET.get("search", "")
    search_type = request.GET.get("seartch_type", "contains")

    if user_search:
        if search_type == "startswith":
            queryset = queryset.filter(login__istartswith=user_search)
        elif search_type == "contains":
            queryset = queryset.filter(login__icontains=user_search)

    return queryset, user_search, search_type


def user_list(request):
    base_user_list = UserInfo.objects.all().order_by("id")
    per_page = get_per_page(request)
    filtered_user_list, user_search, search_type = get_user_search(
        base_user_list, request
    )

    paginator = Paginator(filtered_user_list, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "app/users_list.html",
        {
            "page_obj": page_obj,
            "per_page": per_page,
            "per_page_options": PER_PAGE_OPTIONS,
            "user_search": user_search,
            "search_type": search_type,
        },
    )


def full_user_list(request):
    base_full_user_list = UserInfo.objects.all().order_by("id")
    per_page = get_per_page(request)
    filtered_full_user_list, user_search, search_type = get_user_search(
        base_full_user_list, request
    )

    paginator = Paginator(filtered_full_user_list, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "app/full_user_list.html",
        {
            "page_obj": page_obj,
            "per_page": per_page,
            "per_page_options": PER_PAGE_OPTIONS,
            "user_search": user_search,
            "search_type": search_type,
        },
    )
