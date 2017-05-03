from cursesmenu import CursesMenu
from cursesmenu.items import MenuItem
from behave import *

def before_all(context):
    context.menu = None
    context.menu_item = None
    context.menu_item1 = None
    context.menu_item2= None
    context.menu_item3 = None
    context.menu_item4 = None
    context.menu_item5 = None
    context.menu_item6 = None
    context.menu_item7 = None
#Red
@given("curses menu is installed")
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    pass

@when("user makes a menu item with the parameter 'RED'")
def step_impl(context):
    context.menu_item = MenuItem("RED", "Menu Item")

@then("the text color should be red")
def step_impl(context):
    assert context.menu_item.color is 2

#Green
@given("curses menu is installed")
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    pass

@when("user makes a menu item with the parameter 'GREEN'")
def step_impl(context):
    context.menu_item1 = MenuItem("GREEN", "Menu Item")

@then("the text color should be green")
def step_impl(context):
    assert context.menu_item1.color is 3

#Yellow
@given("curses menu is installed")
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    pass

@when("user makes a menu item with the parameter 'BLUE'")
def step_impl(context):
    context.menu_item2 = MenuItem("YELLOW", "Menu Item")

@then("the text color should be yellow")
def step_impl(context):
    assert context.menu_item2.color is 4

#Blue
@given("curses menu is installed")
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    pass

@when("user makes a menu item with the parameter 'BLUE'")
def step_impl(context):
    context.menu_item3 = MenuItem("BLUE", "Menu Item")

@then("the text color should be blue")
def step_impl(context):
    assert context.menu_item3.color is 5

#Magenta
@given("curses menu is installed")
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    pass

@when("user makes a menu item with the parameter 'MAGENTA'")
def step_impl(context):
    context.menu_item4 = MenuItem("MAGENTA", "Menu Item")

@then("the text color should be magenta")
def step_impl(context):
    assert context.menu_item4.color is 6

#Cyan
@given("curses menu is installed")
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    pass

@when("user makes a menu item with the parameter 'CYAN'")
def step_impl(context):
    context.menu_item5 = MenuItem("CYAN", "Menu Item")

@then("the text color should be cyan")
def step_impl(context):
    assert context.menu_item5.color is 7

#WHITE
@given("curses menu is installed")
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    pass

@when("user makes a menu item with the parameter 'WHITE'")
def step_impl(context):
    context.menu_item6 = MenuItem("WHITE", "Menu Item")

@then("the text color should be white")
def step_impl(context):
    assert context.menu_item6.color is 8



