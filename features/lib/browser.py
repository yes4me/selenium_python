from selenium import webdriver
from selenium.webdriver.common.by import By


class Browser(object):
    def __init__(self):
        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    def find_element_by_id(self, id):
        # return self.driver.find_element_by_id(id)
        return self.driver.find_element(By.ID, id)

    def find_element_by_name(self, name):
        # return self.driver.find_element_by_name(name)
        return self.driver.find_element(By.NAME, name)

    def find_element_by_xpath(self, xpath):
        # return self.driver.find_element_by_xpath(xpath)
        return self.driver.find_element(By.XPATH, xpath)

    def find_element_by_link(self, link):
        # return self.driver.find_element_by_link_text(link)
        return self.driver.find_element(By.LINK_TEXT, link)

    def find_element_by_partial_link(self, link):
        # return self.driver.find_element_by_partial_link_text(link)
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, link)

    def find_element_by_tag(self, tag_name):
        # return self.driver.find_element_by_tag_name(tag_name)
        return self.driver.find_element(By.TAG_NAME, tag_name)

    def find_element_by_class(self, class_name):
        # return self.driver.find_element_by_class_name(class_name)
        return self.driver.find_element(By.CLASS_NAME, class_name)

    def find_element_by_css(self, selector):
        # return self.driver.find_element_by_css_selector(selector)
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def navigate(self, url):
        self.driver.get(url)

    def type(self, selector, text):
        selector.send_keys(text)

    def click(self, selector):
        selector.click()

    def submit(self, selector):
        selector.submit()

    def close(self):
        self.driver.close()
