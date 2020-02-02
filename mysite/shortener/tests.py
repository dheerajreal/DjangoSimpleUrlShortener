from django.test import TestCase


def Homepage(TestCase):
    def test_homepage_status_code():
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)
