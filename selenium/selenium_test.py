from pyvirtualdisplay import Display
from selenium import webdriver
import time


# display = Display(visible=0, size=(1024, 768))
# display.start()
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get('http://google.com/')

search_box = driver.find_element_by_name('q')
search_box.send_keys('123')
search_box.submit()
time.sleep(5)
driver.quit()
# display.stop()
