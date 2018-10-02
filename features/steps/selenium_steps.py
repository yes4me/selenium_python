from behave import given, when, then, step


@given(u'user goes to {website}')
def step_impl(context, website):
    context.browser.go(website)


@when(u'user searches "{text_to_search}"')
def step_impl(context, text_to_search):
    # search_box = context.browser.find_element_by_name('q')
    # search_box.send_keys(text_to_search)
    # search_box.submit()
    pass


@then(u'user closes browser')
def step_impl(context):
    pass
