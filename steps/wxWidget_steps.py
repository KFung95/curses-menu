from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
from wxwidget_example import MainFrame
from behave import *
import wx

def before_all(context):
    context.menu = None
    context.menu_item = None

def start_hci():
    app = wx.PySimpleApp()
    f = MainFrame(parent=None, id=-1)
    f.Show()
    f.Destroy()
    app.MainLoop()

@given("curses menu is installed")
def step_impl(context):
    context.menu = CursesMenu("Test Menu", "Subtitle")
    pass

@when("user makes a menu item launching a wxWidget app")
def step_impl(context):
    context.append_item(FunctionItem("WHITE", "Start HCI", start_hci))
    context.show()
    pass

@and("user exits the wxWidget app")
def step_impl(context):
    context.select() #Selects first menu item. start_hci() rewritten to auto close on launch to simulate exit
    pass

@then("the text color should be red")
def step_impl(context):
    assert context.is_alive(context) is True

