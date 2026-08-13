from django.test import SimpleTestCase, override_settings
from django.urls import reverse


class HomeViewTests(SimpleTestCase):
    def test_homepage_describes_the_project_honestly(self) -> None:
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A home for stories that belong to their writers")
        self.assertContains(response, "Foundation reboot")
        self.assertContains(response, "Not yet a publishing service")

    def test_homepage_has_security_headers(self) -> None:
        response = self.client.get(reverse("home"))

        self.assertEqual(response.headers["X-Content-Type-Options"], "nosniff")
        self.assertEqual(response.headers["X-Frame-Options"], "DENY")
        self.assertEqual(response.headers["Referrer-Policy"], "strict-origin-when-cross-origin")
        self.assertIn("default-src 'self'", response.headers["Content-Security-Policy"])
        self.assertEqual(
            response.headers["Permissions-Policy"],
            "camera=(), geolocation=(), microphone=(), payment=(), usb=()",
        )


class HealthViewTests(SimpleTestCase):
    def test_health_endpoint(self) -> None:
        response = self.client.get(reverse("health"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"service": "tanu", "status": "ok"})

    def test_health_endpoint_rejects_post(self) -> None:
        response = self.client.post(reverse("health"))

        self.assertEqual(response.status_code, 405)


class ErrorPageTests(SimpleTestCase):
    @override_settings(DEBUG=False)
    def test_custom_not_found_page(self) -> None:
        response = self.client.get("/this-page-does-not-exist/")

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "This chapter is missing", status_code=404)
