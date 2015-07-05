from unittest import TestCase
from crawler.CrawlerProcess import CrawlerProcess


class CrawlerProcessTestCase(TestCase):
    def setUp(self):
        self.first_url = 'www.google.co.in'
        self.crawler = CrawlerProcess(self.first_url, 30)

        self.second_url = "https://www.python.org/"
        self.second_crawler = CrawlerProcess(self.second_url, 2)

    def test_for_Valid_url_string(self):
        expected_url = self.first_url
        actual_url = self.crawler.start_url
        self.assertEqual(actual_url, expected_url)

    def test_for_invalid_url_string(self):
        expected_url = 'www.google.com'
        actual_url = self.crawler.start_url
        self.assertNotEquals(actual_url, expected_url)

    def test_for_html_process_status_dict(self):
        expected_output = True
        self.crawler.start_web_crawler()
        actual_output = self.crawler.status_dict.get(self.first_url)
        self.assertEqual(actual_output, expected_output)

    def test_for_valid_maximum_links(self):
        expected_output = 2
        self.second_crawler.start_web_crawler()
        actual_output = len(self.second_crawler.status_dict.keys())
        self.assertEqual(actual_output, expected_output)

    def test_for_invalid_maximum_links(self):
        expected_output = 10
        self.crawler.start_web_crawler()
        actual_output = len(self.crawler.status_dict.keys())
        self.assertNotEquals(actual_output, expected_output)

    def test_for_valid_less_than_maximum_links(self):
        expected_output = 40
        self.crawler.start_web_crawler()
        actual_output = len(self.crawler.status_dict.keys())
        self.assertLess(actual_output, expected_output)
