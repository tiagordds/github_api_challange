from django.db import models


class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(unique=True, max_length=150)
    avatar_url = models.URLField()
    html_url = models.URLField()
    followers_url = models.URLField()
    following_url = models.URLField()
    gist_url = models.URLField()
    starred_url = models.URLField()
    subscriptions_url = models.URLField()
    organizations_url = models.URLField()
    repos_url = models.URLField()
    event_url = models.URLField()
    received_events_url = models.URLField()
    user_type = models.CharField(max_length=200)
    user_view_type = models.CharField(max_length=200)
    site_admin = models.BooleanField()

    def __str__(self):
        return self.login
