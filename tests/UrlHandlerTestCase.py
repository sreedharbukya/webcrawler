from unittest import TestCase
from crawler.UrlHandler import UrlHandler


class UrlHandlerTestCase(TestCase):
    def setUp(self):
        self.handler1 = UrlHandler("www.google.com")
        self.handler2 = UrlHandler("https://docs.python.org")

    def test_for_url_string_valid_output(self):
        expected_url = "www.google.com"
        actual_output = self.handler1.url_string
        self.assertEqual(actual_output, expected_url)

    def test_for_url_string_invalid_output(self):
        expected_url = "www.google.co.in"
        actual_output = self.handler1.url_string
        self.assertNotEquals(actual_output, expected_url)

    def test_for_valid_status_for_url_path(self):
        expected_output = True
        actual_output = self.handler1.get_status_of_request()
        self.assertEqual(expected_output, actual_output)

    def test_for_valid_status_for_url_netloc(self):
        expected_output = True
        actual_output = self.handler2.get_status_of_request()
        self.assertEqual(expected_output, actual_output)
