from cursesmenu import CursesMenu
from cursesmenu.items import PickerItem


class PickerMenu(CursesMenu):
    """
    A menu that simplifies item creation, just give it a list of strings and it builds the menu for you
    """

    def __init__(self, options, title=None, subtitle="Space = toggle, Enter = accept, q = quit", show_exit_option=False):
        """
        :ivar list[str] options: The list of strings this menu should be built from
        """
        super(PickerMenu, self).__init__(title, subtitle, show_exit_option)
        for option in options:
            self.append_item(PickerItem(option, self))

    @classmethod
    def get_selection(cls, options, title, subtitle, exit_option=False, _menu=None):
        """
        Single-method way of getting a selection out of a list of strings

        :param list[str] strings: the list of string used to build the menu
        :param list _menu: should probably only be used for testing, pass in a list and the created menu used \
        internally by the method will be appended to it
        """
        menu = cls(options, title, subtitle, exit_option)
        if _menu is not None:
            _menu.append(menu)
        menu.show()
        menu.join()
        return menu.selected_option

    def gather_selections(self):
        """
        A method that returns all of the base text values of selected options in a list
        :return: results
        :rtype: list
        """
        results = []
        for option in self.items:
            if option.selected:
                results.append(option.text.replace("[X] ", ""))
        return results


