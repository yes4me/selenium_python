from selenium import webdriver


class Browser():
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    def __init__(self):
        pass

    def navigate(self, url):
        self.driver.get(url)

    def type(self, selector, text):
        selector.send_keys(text)

    def submit(self, selector):
        selector.submit()

    def close(self):
        self.driver.close()
