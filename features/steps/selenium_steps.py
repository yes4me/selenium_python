from behave import given, when, then, step
from page_objects.google_home import GoogleHomePage


@given(u'user goes to {website}')
def step_impl(context, website):
    # context.browser.navigate(website)
    context.google = GoogleHomePage()
    context.google.visit()


@when(u'user searches "{text_to_search}"')
def step_impl(context, text_to_search):
    context.google.search(text_to_search)


@then(u'user closes browser')
def step_impl(context):
    pass
