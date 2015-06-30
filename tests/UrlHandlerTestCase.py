from unittest import TestCase
from Process.UrlHandler import UrlHandler


class UrlHandlerTestCase(TestCase):

    def setUp(self):

        self.handler1 = UrlHandler("www.google.com")

    def test_for_valid_output(self):
        expected_url = "www.google.com"
        actual_output = self.handler1.url_string
        self.assertEqual(actual_output, expected_url)

    def test_for_invalid_output(self):
        expected_url = "www.google.co.in"
        actual_output = self.handler1.url_string
        self.assertNotEquals(actual_output, expected_url)
    