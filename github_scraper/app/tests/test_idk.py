from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

from app.models import UserInfo


class UserViewTest(TestCase):
    def setUp(self):
        self.test_user = UserInfo.objects.create(
            id=10,
            login="tiago",
            avatar_url="https://github.com/tiagordds",
            html_url="https://github.com/tiagordds",
            followers_url="https://github.com/tiagordds",
            following_url="https://github.com/tiagordds",
            gist_url="https://github.com/tiagordds",
            starred_url="https://github.com/tiagordds",
            subscriptions_url="https://github.com/tiagordds",
            organizations_url="https://github.com/tiagordds",
            repos_url="https://github.com/tiagordds",
            event_url="https://github.com/tiagordds",
            received_events_url="https://github.com/tiagordds",
            user_type="user",
            user_view_type="default",
            site_admin=False,
        )

    def test_user_list_returns_200(self):
        response = self.client.get(reverse("user_list"))
        self.assertEqual(response.status_code, 200)

    def test_search_contains(self):
        response = self.client.get(
            reverse("user_list") + "?search=iag&seartch_type=contains"
        )
        self.assertContains(response, "tiago")


class UserInfoModelTest(TestCase):
    def setUp(self):
        self.test_user = UserInfo.objects.create(
            id=10,
            login="tiago",
            avatar_url="https://github.com/tiagordds",
            html_url="https://github.com/tiagordds",
            followers_url="https://github.com/tiagordds",
            following_url="https://github.com/tiagordds",
            gist_url="https://github.com/tiagordds",
            starred_url="https://github.com/tiagordds",
            subscriptions_url="https://github.com/tiagordds",
            organizations_url="https://github.com/tiagordds",
            repos_url="https://github.com/tiagordds",
            event_url="https://github.com/tiagordds",
            received_events_url="https://github.com/tiagordds",
            user_type="user",
            user_view_type="default",
            site_admin=False,
        )

    def test_create_user(self):
        self.assertEqual(self.test_user.id, 10)
        self.assertEqual(self.test_user.login, "tiago")
        self.assertEqual(self.test_user.site_admin, False)
        self.assertEqual(self.test_user.user_type, "user")

    def test_login_is_unique(self):
        with self.assertRaises(IntegrityError):
            UserInfo.objects.create(
                id=11,
                login="tiago",
                avatar_url="https://github.com/tiagorddss",
                html_url="https://github.com/tiagorddss",
                followers_url="https://github.com/tiagorddss",
                following_url="https://github.com/tiagorddss",
                gist_url="https://github.com/tiagorddss",
                starred_url="https://github.com/tiagorddss",
                subscriptions_url="https://github.com/tiagorddss",
                organizations_url="https://github.com/tiagorddss",
                repos_url="https://github.com/tiagorddss",
                event_url="https://github.com/tiagorddss",
                received_events_url="https://github.com/tiagorddss",
                user_type="user",
                user_view_type="default",
                site_admin=False,
            )

    def test_id_is_unique(self):
        with self.assertRaises(IntegrityError):
            UserInfo.objects.create(
                id=12,
                login="tiago",
                avatar_url="https://github.com/tiagorddss",
                html_url="https://github.com/tiagorddss",
                followers_url="https://github.com/tiagorddss",
                following_url="https://github.com/tiagorddss",
                gist_url="https://github.com/tiagorddss",
                starred_url="https://github.com/tiagorddss",
                subscriptions_url="https://github.com/tiagorddss",
                organizations_url="https://github.com/tiagorddss",
                repos_url="https://github.com/tiagorddss",
                event_url="https://github.com/tiagorddss",
                received_events_url="https://github.com/tiagorddss",
                user_type="user",
                user_view_type="default",
                site_admin=False,
            )
