from django.test import TestCase
from models import UserInfo


class UserInfoModelTest(TestCase):
    def test_set_up(self):
        self.user1 = UserInfo.objects.create(
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

    def test_user_creation(self):
        self.assertEqual(self.user1.login, "tiago")
        self.assertEqual(self.user1.html_url, "https://github.com/tiagordds")
