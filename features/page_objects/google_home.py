from lib.browser import Browser


class GoogleHomePage(Browser):
    def __init__(self):
        self.HOME = "http://www.google.com"

    def navigate(self):
        Browser().navigate(self.HOME)
