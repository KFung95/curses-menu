from cursesmenu import CursesMenu
from cursesmenu.items import PickerItem


class PickerMenu(CursesMenu):
    """
    A menu that simplifies item creation, just give it a list of strings and it builds the menu for you
    """

    def __init__(self, options, title=None, subtitle=None, show_exit_option=True):
        """
        :ivar list[str] options: The list of strings this menu should be built from
        """
        arrow = "-->"
        footer = "Space = toggle, Enter = accept, q = cancel"
        more = "..."
        border = "||--++++"
        c_selected = "[X]"
        c_empty = "[ ]"
        aborted = False

        super(PickerMenu, self).__init__(title, subtitle, show_exit_option)

        self.title = title
        self.arrow = arrow
        self.footer = footer
        self.more = more
        self.border = border
        self.c_selected = c_selected
        self.c_empty = c_empty
        self.aborted = aborted

        self.all_options = []
        for option in options:
            self.all_options.append(PickerItem(option, False, self))  # May need to override append_item
        self.length = len(self.all_options)

