# Import the necessary packages
from cursesmenu import *
from cursesmenu.items import *

# Create the menu
menu = CursesMenu("Title", "Subtitle")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("RED", "Menu Item")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem("GREEN", "Call a Python function", input, ["Enter an input: "])

# A CommandItem runs a console command
command_item = CommandItem("YELLOW", "Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example) as a submenu of another menu
submenu_item = SubmenuItem("MAGENTA", "Submenu Item (Selection Menu)", selection_menu, menu)

# A PickerMenu constructs a menu from a list of strings
picker_menu = PickerMenu(["file1", "file2", "file3"])

# A SubmenuItem lets you add a menu (the picker_menu above, for example) as a submenu of another menu
picker_submenu_item = SubmenuItem("BLUE", "Submenu Item (Picker Menu)", picker_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)
menu.append_item(picker_submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
