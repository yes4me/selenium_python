from selenium import webdriver


class Browser():
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    def __init__(self):
        pass

    def find_element_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def find_element_by_css(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def navigate(self, url):
        self.driver.get(url)

    def type(self, selector, text):
        selector.send_keys(text)

    def submit(self, selector):
        selector.submit()

    def close(self):
        self.driver.close()
