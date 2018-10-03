from selenium.webdriver.common.by import By
from lib.browser import Browser


class GoogleHomePage(Browser):
    def __init__(self):
        self.HOME = "http://www.google.com"

    def navigate(self):
        Browser().navigate(self.HOME)

    def search(self, text_to_search):
        element = Browser().find_element_by_name('q')
        Browser().type(element, text_to_search)
        Browser().submit(element)
