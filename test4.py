from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
import unittest

class TestAddition(unittest.TestCase):
    driver = None
    def setUp(self):
        global driver
        driver = webdriver.PhantomJS()
        url = 'http://pythonscraping.com/pages/javascript/draggableDemo.html'
        driver.get(url)

    def tearDown(self):
        print('Tearing down the test')

    def test_drag(self):
        global driver
        element = driver.find_element_by_id('draggable')
        target = driver.find_element_by_id('div2')
        actions = ActionChains(driver)
        actions.drag_and_drop(element, target).perform()

        self.assertEqual("Prove you are not a bot, by dragging the square from the blue area to the red area!", driver.find_element_by_id('message').text)

if __name__ == '__main__':
    unittest.main()