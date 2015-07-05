from unittest import TestCase
from crawler.CrawlerProcess import CrawlerProcess


class CrawlerProcessTestCase(TestCase):
    def setUp(self):
        self.first_url = 'www.google.co.in'
        self.crawler = CrawlerProcess(self.first_url)

        self.second_url = "https://www.python.org/"
        self.second_crawler = CrawlerProcess(self.second_url)

    def test_for_Valid_url_string(self):
        expected_url = self.first_url
        actual_url = self.crawler.start_url
        self.assertEqual(actual_url, expected_url)

    def test_for_invalid_url_string(self):
        expected_url = 'www.google.com'
        actual_url = self.crawler.start_url
        self.assertNotEquals(actual_url, expected_url)

    def test_for_valid_response(self):
        expected_output = True
        actual_output = CrawlerProcess.check_url_status(self.first_url)
        self.assertEqual(expected_output, actual_output)

    def test_for_invalid_response(self):
        expected_output = False
        actual_output = CrawlerProcess.check_url_status('google.com')
        self.assertNotEquals(actual_output, expected_output)
