# Craig Busch
# -- FILE: features/steps/picker_menu_steps.py
from behave import given, when, then, step
from cursesmenu import PickerMenu


@given('we have a PickerMenu created with 3 unselected items')
def step_impl(context):
    context.result = []
    context.menu = PickerMenu("Test Menu", ["item1", "item2", "item3"])
    context.menu.show()
    pass


@when('we toggle the first item')
def step_impl(context):
    context.menu.items[0].toggle_selection()
    pass


@then('the first item is now selected')
def step_impl(context):
    assert context.menu.items[0].is_selected()


@given('we have a PickerMenu created with the first item set as selected')
def step_impl(context):
    context.result = []
    context.menu = PickerMenu("Test Menu", ["item1", "item2", "item3"])
    context.menu.show()
    context.menu.items[0].toggle_selection()
    pass


@when('we toggle the second item')
def step_impl(context):
    context.menu.items[1].toggle_selection()
    pass


@then('the second item is now selected')
def step_impl(context):
    assert context.menu.items[0].is_selected()


@given('we have a PickerMenu created with 3 selected items')
def step_impl(context):
    context.result = []
    context.menu = PickerMenu("Test Menu", ["item1", "item2", "item3"])
    context.menu.show()
    context.menu.items[0].toggle_selection()
    context.menu.items[1].toggle_selection()
    context.menu.items[2].toggle_selection()
    pass


@when('we toggle the last item')
def step_impl(context):
    context.menu.items[2].toggle_selection()
    pass


@then('the last item is now un-selected')
def step_impl(context):
    assert not context.menu.items[2].is_selected()


@given('we have a PickerMenu created with 2 selected items and 1 unselected items')
def step_impl(context):
    context.result = []
    context.menu = PickerMenu("Test Menu", ["item1", "item2", "item3"])
    context.menu.show()
    context.menu.items[0].toggle_selection()
    context.menu.items[1].toggle_selection()
    pass


@when('we enter the selections')
def step_impl(context):
    context.result = context.menu.gather_selections()
    pass


@then("the PickerMenu will return a list of {number:d} selections")
def step_impl(context, number):
    assert len(context.result) == number
