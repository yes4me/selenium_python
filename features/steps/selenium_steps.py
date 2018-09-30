from behave import given, when, then, step
from selenium import webdriver


@given(u'user goes to {website}')
def step_impl(context, website):
    global driver
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    driver.get(website)


@when(u'user searches "{text_to_search}"')
def step_impl(context, text_to_search):
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(text_to_search)
    search_box.submit()


@then(u'user closes browser')
def step_impl(context):
    driver.quit()
