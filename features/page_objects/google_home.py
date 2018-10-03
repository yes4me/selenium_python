from lib.browser import Browser


class GoogleHomePage(Browser):
    def __init__(self):
        self.HOME = "http://www.google.com"

    def navigate(self):
        Browser().navigate(self.HOME)

    def search(self, text_to_search):
        selector = self.driver.find_element_by_name('q')
        Browser().type(selector, text_to_search)
        Browser().submit(selector)
