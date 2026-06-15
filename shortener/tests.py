from django.test import TestCase
from django.urls import reverse

from .models import ShortURL


class ShortURLTests(TestCase):
    def test_create_short_url(self):
        obj = ShortURL.objects.create(
            original_url="https://example.com",
            short_code="abc123",
        )
        self.assertEqual(obj.clicks, 0)
        self.assertEqual(str(obj), "abc123")

    def test_redirect_short_url(self):
        obj = ShortURL.objects.create(
            original_url="https://example.com",
            short_code="go1234",
        )
        url = reverse("shortener:redirect", args=[obj.short_code])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        obj.refresh_from_db()
        self.assertEqual(obj.clicks, 1)

    def test_home_page_shows_form(self):
        response = self.client.get(reverse("shortener:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Paste your URL")