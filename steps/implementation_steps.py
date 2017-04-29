# Craig Busch
# -- FILE: features/steps/implementation_steps.py
from cursesmenu import CursesMenu, SelectionMenu, PickerMenu
from cursesmenu.items import MenuItem, FunctionItem, CommandItem, SubmenuItem
from behave import *


def before_all(context):
    context.menu_item = None
    context.function_item = None
    context.command_item = None
    context.selection_menu = None
    context.selection_submenu_item = None
    context.picker_submenu_item = None
    context.menu = None
    context.selection_menu = None
    context.picker_menu = None


@given("we have curses-menu installed")
def step_impl(context):
    pass


@when('we implement a CursesMenu with the title "Test Menu" and the subtitle "Subtitle"')
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    pass


@then("we will have an empty curses menu with a title")
def step_impl(context):
    assert context.menu is not None


@given("we have a curse menu created")
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    pass


@when("we implement a MenuItem")
def step_impl(context):
    context.menu_item = MenuItem("NORMAL", "Menu Item")
    context.menu.append_item(context.menu_item)
    pass


@then("we will have a curse menu containing a MenuItem")
def step_impl(context):
    assert context.menu is not None
    assert context.menu_item is not None


@given('we have a curse menu created with a MenuItem')
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    context.menu_item = MenuItem("NORMAL", "Menu Item")
    context.menu.append_item(context.menu_item)
    pass


@when("we implement a FunctionItem")
def step_impl(context):
    context.function_item = FunctionItem("NORMAL", "Call a Python function", input, ["Enter an input"])
    context.menu.append_item(context.function_item)
    pass


@then("we will have a curse menu containing a FunctionItem")
def step_impl(context):
    assert context.menu is not None
    assert context.menu_item is not None
    assert context.function_item is not None


@given('we have a curse menu created with a MenuItem and a FunctionItem')
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    context.menu_item = MenuItem("NORMAL", "Menu Item")
    context.menu.append_item(context.menu_item)
    context.function_item = FunctionItem("NORMAL", "Call a Python function", input, ["Enter an input"])
    context.menu.append_item(context.function_item)
    pass


@when("we implement a CommandItem")
def step_impl(context):
    context.command_item = CommandItem("NORMAL", "Run a console command",  "ipconfig /all")
    context.menu.append_item(context.command_item)
    pass


@then("we will have a curse menu containing a CommandItem")
def step_impl(context):
    assert context.menu is not None
    assert context.menu_item is not None
    assert context.function_item is not None
    assert context.command_item is not None


@given('we have a curse menu created with a MenuItem and a FunctionItem and a CommandItem')
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    context.menu_item = MenuItem("NORMAL", "Menu Item")
    context.menu.append_item(context.menu_item)
    context.function_item = FunctionItem("NORMAL", "Call a Python function", input, ["Enter an input"])
    context.menu.append_item(context.function_item)
    context.command_item = CommandItem("NORMAL", "Run a console command",  "ipconfig /all")
    context.menu.append_item(context.command_item)
    pass


@when("we implement a selection SubmenuItem")
def step_impl(context):
    context.selection_menu = SelectionMenu(["item1", "item2", "item3"])
    context.selection_submenu_item = SubmenuItem("NORMAL", "Submenu item", context.selection_menu)
    context.menu.append_item(context.selection_submenu_item)
    pass


@then("we will have a curse menu containing a SubmenuItem that contains a SelectionMenu")
def step_impl(context):
    assert context.menu is not None
    assert context.menu_item is not None
    assert context.function_item is not None
    assert context.command_item is not None
    assert context.selection_menu is not None
    assert context.selection_submenu_item is not None


@given('we have a curse menu created with a MenuItem and a FunctionItem and a CommandItem and a selection SubmenuItem')
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    context.menu_item = MenuItem("NORMAL", "Menu Item")
    context.menu.append_item(context.menu_item)
    context.function_item = FunctionItem("NORMAL", "Call a Python function", input, ["Enter an input"])
    context.menu.append_item(context.function_item)
    context.command_item = CommandItem("NORMAL", "Run a console command",  "ipconfig /all")
    context.menu.append_item(context.command_item)
    context.selection_menu = SelectionMenu(["item1", "item2", "item3"])
    context.selection_submenu_item = SubmenuItem("NORMAL", "Submenu item", context.selection_menu)
    context.menu.append_item(context.selection_submenu_item)
    pass


@when("we implement a picker SubmenuItem")
def step_impl(context):
    context.picker_menu = PickerMenu(["item1", "item2", "item3"])
    context.picker_submenu_item = SubmenuItem("NORMAL", "Submenu item", context.picker_menu)
    context.menu.append_item(context.picker_submenu_item)
    pass


@then("we will have a curse menu containing a SubmenuItem that contains a PickerMenu")
def step_impl(context):
    assert context.menu is not None
    assert context.menu_item is not None
    assert context.function_item is not None
    assert context.command_item is not None
    assert context.selection_menu is not None
    assert context.selection_submenu_item is not None
    assert context.picker_menu is not None
    assert context.picker_submenu_item is not None
