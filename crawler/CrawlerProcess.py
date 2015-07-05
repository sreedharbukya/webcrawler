import urllib2
import urlparse
import time

from BeautifulSoup import BeautifulSoup


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
        try:
            html_dump = self._url_handler(current_url)
            soup = BeautifulSoup(html_dump)
            for link in soup.findAll('a'):
                found_url = urlparse.urljoin(current_url, link.get('href'))
                if self.counter < self.maximum_links:
                    if found_url.startswith(current_url):
                        if found_url not in self.status_dict:
                            self.status_dict[found_url] = False
                            self.counter += 1
            self.status_dict[current_url] = True
        except:
            self.status_dict[current_url] = True

    def more_to_crawl_check(self):
        for url, status in iter(self.status_dict.iteritems()):
            if not status:
                print "Found URL to crawl {}".format(url)
                return url
        return False

    def url_response_handler(self, request, url):
        try:
            response = urllib2.urlopen(request)
            return response
        except urllib2.HTTPError as ex:
            print 'Problem in HTTP Response for URL: %s with Exception %s' % url, ex
            return None
        except ValueError as ex:
            print 'Problem in Response for URL %s with Exception %s' % url, ex
            return None


    def _url_handler(self, url):
        request = self._url_request_handler(url)
        if request:
            response = self.url_response_handler(request, url)
            if response:
                return response
            else:
                print "Problem in receiving response from Server"

    def _url_request_handler(self, url):
        try:
            request = urllib2.Request(url)
            return request
        except Exception as ex:
            print "Problem in HTTP request for URL: %s with Exception %s" % (url, ex)
            return None



if __name__ == "__main__":
    inputURL = "https://www.python.org/"
    handler = CrawlerProcess(inputURL)
    handler.start_web_crawler()
