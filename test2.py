from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class TestWikipedia(unittest.TestCase):
    soup = None
    def setUpClass():
        global soup 
        url = 'http://en.wikipedia.org/wiki/Monty_Python'
        soup = BeautifulSoup(urlopen(url), 'lxml')

    def test_titleText(self):
        global soup
        pageTitle = soup.find('h1').get_text()
        self.assertEqual('Monty Python', pageTitle)

    def test_contentExists(self):
        global soup
        content = soup.find('div', {'id': 'mw-content-text'})
        self.assertIsNotNone(content)

if __name__ == '__main__':
    unittest.main()