from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class TestWikipedia(unittest.TestCase):
    soup = None
    url = None

    def test_PageProperties(self):
        global soup
        global url

        url = 'http://en.wikipedia.org/wiki/Monty_Python'
        for i in range(1, 100):
            soup = BeautifulSoup(urlopen(url), 'lxml')
            titles = self.titleMatchesURL()
            self.assertEquals(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print('Done!')

    def titleMatchesURL(self):
        global soup
        global url
        pageTitle = soup.find('h1').get_text()
        urlTitle = url[(url.index('/wiki/')+6):]
        urlTitle = urlTitle.replace('_', ' ')
        urlTitle = unquote(urlTitle) #unquote 不存在？
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global soup
        content = soup.find('div', {"id": "mw-content-text"})
        if content is not None:
            return True
        return False

if __name__ == '__main__':
    unittest.main()