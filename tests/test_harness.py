# -*- coding: utf-8 -*-
# python 2

# craw a website, list all url under a specific given path

inputURL = "https://docs.python.org"

resultUrl = {inputURL: False}
# key is a url we want. value is True or False. True means already crawled

# from urllib import urlopen
import urllib2
import urlparse
import time
import pprint

from BeautifulSoup import BeautifulSoup

def processOneUrl(url):
    """fetch URL content and update resultUrl."""
    try:  # in case of 404 error
        html_page = urllib2.urlopen(url)
        soup = BeautifulSoup(html_page)
        for link in soup.findAll('a'):
            fullurl = urlparse.urljoin(url, link.get('href'))
            print fullurl
            if fullurl.startswith(inputURL):
                if (fullurl not in resultUrl):
                    resultUrl[fullurl] = False
        resultUrl[url] = True  # set as crawled
    except:
        resultUrl[url] = True  # set as crawled


def moreToCrawl():
    """returns True or False"""
    for url, crawled in iter(resultUrl.iteritems()):
        if not crawled:
            print "moreToCrawl found {}".format(url)
            return url
    return False

processOneUrl(inputURL)


while True:
    toCrawl = moreToCrawl()
    if not toCrawl:
        break
    processOneUrl(toCrawl)
    time.sleep(2)

pprint.pprint(resultUrl)
