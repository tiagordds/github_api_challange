from django.db import models


class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(unique=True, max_length=150)
    html_url = models.URLField()
    repos_url = models.URLField()
    user_type = models.CharField(max_length=200)

    def __str__(self):
        return self.login
