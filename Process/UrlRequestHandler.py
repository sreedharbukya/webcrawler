import urllib
import urllib2
from Process.UrlHandler import UrlHandler


def get_response_from_url(url):
    response = urllib2.urlopen(url)
    return response


class UrlRequestHandler():
    def __init__(self, url_string):
        self.url_string = url_string

    def check_url_request(self):
        response = None
        handler = UrlHandler(self.url_string)
        if handler.get_status_of_request():
            try:
                response = get_response_from_url(self.url_string)
            except Exception as ex:
                print ex
        else:
            print "URL %s status request is Not valid" % self.url_string
        return response
