from selenium import webdriver


class Browser():
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    def __init__(self):
        pass

    def go(self, website):
        self.driver.get(website)

    def close(self):
        self.driver.close()
