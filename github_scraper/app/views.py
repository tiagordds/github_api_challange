import json

from django.shortcuts import render

from .models import UserData


def import_data(request):
    if request.method == "POST" and request.FILES["json_file"]:
        json_file = request.FILES["json_file"]
        data = json.load(json_file)

        if isinstance(data, dict):
            data = [data]

        for item in data:
            user_data = UserData(
                login=item["login"],
                user_id=item["id"],
                html_url=item["html_url"],
            )
            user_data.save()
        return render(request, "success.html")
    return render(request, "form.html")
