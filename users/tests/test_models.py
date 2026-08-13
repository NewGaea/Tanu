from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTests(TestCase):
    def test_project_uses_its_swappable_user_model(self) -> None:
        user = get_user_model().objects.create_user(
            username="reader",
            email="reader@example.test",
            password="a-long-test-password",
        )

        self.assertEqual(user.email, "reader@example.test")
        self.assertTrue(user.check_password("a-long-test-password"))
