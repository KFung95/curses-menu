from cursesmenu.items import MenuItem


class PickerItem(MenuItem):
    """
    The item type used in :class:`cursesmenu.SelectionMenu`
    """

    def __init__(self, text, selected, menu=None):
        """
        :ivar int index: The index of this item in the list used to initialize the :class:`cursesmenu.PickerMenu`
        """
        super(PickerItem, self).__init__(text=text, menu=menu, should_exit=True)
        self.selected = selected
        self.text = "[ ] " + self.text

    def toggle_selection(self):
        """
        Toggles the selected boolean variable
        """
        if self.selected:
            self.selected = False
            self.text = self.text.replace("[X] ", "[ ] ")
        else:
            self.selected = True
            self.text = self.text.replace("[ ] ", "[X] ")

    def get_return(self):
        """
        :return: The index of this item in the list of strings
        :rtype: boolean
        """
        return self.selected
