#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup

class Client(object):

    def get_web(self, url):
        t = urllib2.urlopen(url)
        html = t.read()
        t.close()
        return html

    def parse_web(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find("div", "dotd-title")
        t = elements.find("h2")
        return t.text

    def result(self, result):
        return result.replace("\t", "").replace("\n", "")

    def main(self):
        web = self.get_web("https://www.packtpub.com/packt/offers/free-learning/")
        result = self.parse_web(web)
        title = self.result(result)
        print title

if __name__ == "__main__":
    client = Client()
    client.main()
