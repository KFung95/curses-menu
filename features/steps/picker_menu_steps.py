#Craig Busch
# -- FILE: features/steps/picker_menu_steps.py
from behave import given, when, then, step
from cursesmenu import curses_menu, picker_menu


@given('we have a curse menu created')
def step_impl(context):
    context.result = None
    context.menu = curses_menu.CursesMenu("Test Menu", "Subtitle")
    context.menu.show()
    pass


@step('we have a PickerMenu created with a list')
def step_impl(context):
    context.picker_menu = picker_menu.PickerMenu(["item1", "item2", "item3"])
    pass


@step('the PickerMenu is appended as a SubmenuItem to the curse menu')
def step_impl(context):
    context.menu.append_item(context.picker_menu)
    context.menu.show()
    pass


@step("the PickerMenu has no selections")
def step_impl(context):
    assert len(context.picker_menu.selections) == 0


@when("we hit the space bar while hovering over an unselected item")
def step_impl(context):
    assert context.picker_menu.current_item in context.picker_menu.selections
    context.picker_menu.toggle_item(context.picker_menu.current_item)


@then("the item is now selected")
def step_impl(context):
    assert context.picker_menu.current_item in context.picker_menu.selections


@step("the PickerMenu has existing selections")
def step_impl(context):
    assert len(context.picker_menu.selections) != 0


@when("we hit the space bar while hovering over a selected item")
def step_impl(context):
    assert context.picker_menu.current_item not in context.picker_menu.selections
    context.picker_menu.toggle_item(context.picker_menu.current_item)


@then("the item is now un-selected")
def step_impl(context):
    assert context.picker_menu.current_item not in context.picker_menu.selections


@when("we hit the enter key with {number:d} selections")
def step_impl(context, number):
    assert number >= 0
    context.result = context.picker_menu.submit_selections()


@then("the PickerMenu will return a list of {number:d} selections")
def step_impl(context, number):
    assert len(context.result) == number
