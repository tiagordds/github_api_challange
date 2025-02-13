from django.db import models


class UserData(models.Model):
    login = models.CharField(max_length=100)
    user_id = models.IntegerField()
    html_url = models.CharField(max_length=150)
