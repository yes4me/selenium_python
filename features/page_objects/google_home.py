from selenium.webdriver.common.by import By
from lib.browser import Browser
from page_objects.base_page import BasePage


class GoogleHomePage(BasePage):
    def __init__(self):
        super(GoogleHomePage, self).__init__()
        self.HOME = "http://www.google.com"

    def navigate(self):
        Browser().navigate(self.HOME)

    def search(self, text_to_search):
        element = Browser().find_element_by_name('q')
        Browser().type(element, text_to_search)
        Browser().submit(element)
