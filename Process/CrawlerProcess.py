import pprint
import urllib2
import urlparse
from urlparse import urlparse as url_parser

from BeautifulSoup import BeautifulSoup
import time


class CrawlerProcess():
    def __init__(self, start_url, maximum_links=30):
        self.start_url = start_url
        self.maximum_links = maximum_links

        self.status_dict = {self.start_url: False}

    def start_web_crawler(self):
        self.counter = 1
        self.process_html_page_and_set_status_of_crawling(self.start_url)
        while self.counter <= self.maximum_links:
            crawl = self.more_to_crawl_check()
            if not crawl:
                break
            self.process_html_page_and_set_status_of_crawling(crawl)
            time.sleep(2)

    def process_html_page_and_set_status_of_crawling(self, current_url):
        status = CrawlerProcess.check_url_status(current_url)
        if status:
            try:
                html_dump = urllib2.urlopen(current_url)
                soup = BeautifulSoup(html_dump)
                for link in soup.findAll('a'):
                    found_url = urlparse.urljoin(current_url, link.get('href'))
                    if self.counter <= self.maximum_links:
                        if found_url.startswith(current_url):
                            if found_url not in self.status_dict:
                                self.status_dict[found_url] = False
                                self.counter += 1
                self.status_dict[current_url] = True
            except:
                self.status_dict[current_url] = True
        else:
            print "Problem found in validating URL: %s" % current_url

    def more_to_crawl_check(self):
        for url, status in iter(self.status_dict.iteritems()):
            if not status:
                print "Found URL to crawl {}".format(url)
                return url
        return False

    @staticmethod
    def check_url_status(url):
        status = False
        parse = url_parser(url)
        if parse.netloc or parse.path:
            status = True
        return status


if __name__ == "__main__":
    inputURL = "https://docs.python.org"
    handler = CrawlerProcess(inputURL)
    handler.start_web_crawler()
    pprint.pprint(handler.status_dict)
