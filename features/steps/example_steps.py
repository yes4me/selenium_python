from behave import given, when, then, step


@given(u'some setup condition')
def step_impl(context):
    print("==> BACKGROUND")
    pass


@given(u'we have behave installed')
def step_impl(context):
    pass


@when(u'we implement {number:d} tests')
def step_impl(context, number):
    # NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number


@then(u'behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0


@given(u'the basket has "{number:d}" guinea pigs')
def step_impl(context, number):
    context.basket = number


@when(u'"{number:d}" guinea pigs are added to the basket')
def step_impl(context, number):
    context.basket = context.basket + number


@then(u'the basket contains "{total:d}" guinea pigs')
def step_impl(context, total):
    assert context.basket == total
