from urlparse import urlparse


class UrlHandler():
    def __init__(self, url_string):
        self.url_string = url_string

    def get_status_of_request(self):
        self.status = self._parser_url_string()
        return self.status

    def _parser_url_string(self):
        url = urlparse(self.url_string)
        if url.path or url.netloc:
            return True
