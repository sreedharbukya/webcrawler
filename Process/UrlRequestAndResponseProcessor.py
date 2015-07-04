import urllib2
import urlparse
from urlparse import urlparse as url_parser

from BeautifulSoup import BeautifulSoup


class UrlRequestAndResponseProcessor():
    def __init__(self, url_string):
        self.url_string = url_string

    def check_url_status(self):
        status = False
        parse = url_parser(self.url_string)
        if parse.netloc or parse.path:
            status = True
        return status

    def get_request_response(self):
        page_urls = []

        try:
            html_dump = urllib2.urlopen(self.url_string)
            soup = BeautifulSoup(html_dump)
            for link in soup.findAll('a'):
                url = urlparse.urljoin(self.url_string, link.get('href'))
                page_urls.append(url)
        except Exception as ex:
            print ex
        print page_urls
        return page_urls


if __name__ == "__main__":
    inputURL = "https://docs.python.org"
    handler = UrlRequestAndResponseProcessor(inputURL)
    handler.get_request_response()
