from cursesmenu import CursesMenu
from cursesmenu.items import MenuItem
from behave import *

def before_all(context):
    context.menu = None
    context.menu_item = None

@given("curses menu is installed")
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    pass

@when("user makes a menu item with the parameter 'RED'")
def step_impl(context):
    context.menu_item = MenuItem("RED", "Menu Item")

@then("color should be red")
def step_impl(context):
    assert context.menu_item.color is 2

