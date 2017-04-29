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
            self.append_item(PickerItem("NORMAL", option, self))

    def get_selections(self):
        """
        A method that returns all of the base text values of selected options in a list
        :return: results
        :rtype: list
        """
        results = []
        for option in self.items:
            if option.is_selected():
                results.append(option.get_text())
        return results

    @staticmethod
    def is_picker():
        """
        Returns True for PickerMenu
        """
        return True
