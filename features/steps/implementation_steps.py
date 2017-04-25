#Craig Busch
# -- FILE: features/steps/implementation_steps.py
from cursesmenu import curses_menu, selection_menu, picker_menu
from cursesmenu.items import function_item, command_item, submenu_item
from behave import given, when, then


def before_all(context):
    context.menu_item = None
    context.function_item = None
    context.command_item = None
    context.selection_menu = None
    context.selection_submenu_item = None
    context.picker_submenu_item = None


@given("we have curses-menu installed")
def step_impl(context):
    context.list = ["item1", "item2", "item3"]
    context.menu = None
    context.selection_menu = None
    context.picker_menu = None
    pass


@when('we implement a CursesMenu with the title "Test Menu" and the subtitle "Subtitle"')
def step_impl(context):
    context.menu = curses_menu.CursesMenu("Test Menu", "Subtitle")
    context.menu.show()
    pass


@then("we will have an empty curses menu with a title")
def step_impl(context):
    assert context.menu is not None
    assert context.menu.is_alive()
    assert context.menu.is_running()


@given("we have a curse menu created")
def step_impl(context):
    context.menu = curses_menu.CursesMenu("Test Menu", "Subtitle")
    context.menu.show()
    pass


@when("we implement a MenuItem")
def step_impl(context):
    context.menu_item = curses_menu.MenuItem("NORMAL", "Menu Item")
    context.menu.append_item(context.menu_item)
    context.menu.draw()
    pass


@then("we will have a curse menu containing a MenuItem")
def step_impl(context):
    assert context.menu_item.__str__() == "Test Menu Menu Item"
    assert context.menu.is_alive()
    assert context.menu.is_running()


# @given previously stated
@when("we implement a FunctionItem")
def step_impl(context):
    context.function_item = function_item.FunctionItem("NORMAL", "Call a Python function", input, ["Enter an input"])
    context.menu.append_item(context.function_item)
    context.menu.draw()
    pass


@then("we will have a curse menu containing a FunctionItem")
def step_impl(context):
    assert context.menu.is_alive()
    assert context.menu.is_running()


# @given previously stated
@when("we implement a CommandItem")
def step_impl(context):
    context.command_item = command_item.CommandItem("NORMAL", "Run a console command",  "ipconfig /all")
    context.menu.append_item(context.command_item)
    context.menu.draw()
    pass


@then("we will have a curse menu containing a CommandItem")
def step_impl(context):
    assert context.menu.is_alive()
    assert context.menu.is_running()


# @given previously stated
@when("we implement a SelectionMenu with a list of selections")
def step_impl(context):
    assert len(context.list) != 0
    context.selection_menu = selection_menu.SelectionMenu(context.list)
    pass


@then("we will have a populated SelectionMenu")
def step_impl(context):
    assert context.selection_menu is not None
    assert context.selection_menu.is_alive()
    assert context.selection_menu.is_running()


# @given previously stated
@when("we implement a selection SubmenuItem")
def step_impl(context):
    context.selection_submenu_item = submenu_item.SubmenuItem("NORMAL", "Submenu item", context.selection_menu, context.menu)
    context.menu.append_item(context.submenu_item)
    context.menu.draw()
    pass


@then("we will have a curse menu containing a SubmenuItem that contains a SelectionMenu")
def step_impl(context):
    assert context.menu.is_alive()
    assert context.menu.is_running()


@when("we implement a PickerMenu with a list of selections")
def step_impl(context):
    assert len(context.list) != 0
    context.picker_menu = picker_menu.PickerMenu(context.list)
    pass


@then("we will have a populated PickerMenu")
def step_impl(context):
    assert context.picker_menu is not None
    assert context.picker_menu.is_alive()
    assert context.picker_menu.is_running()


@when("we implement a picker SubmenuItem")
def step_impl(context):
    context.selection_submenu_item = submenu_item.SubmenuItem("NORMAL", "Submenu item", context.picker_menu, context.menu)
    context.menu.append_item(context.submenu_item)
    context.menu.draw()
    pass


@then("we will have a curse menu containing a SubmenuItem that contains a PickerMenu")
def step_impl(context):
    assert context.menu.is_alive()
    assert context.menu.is_running()
