from cursesmenu.items import MenuItem

class PickerItem(MenuItem):
    """
    The item type used in :class:`cursesmenu.SelectionMenu`
    """

    def __init__(self, color, text, menu=None):
        """
        :ivar int index: The index of this item in the list used to initialize the :class:`cursesmenu.PickerMenu`
        """
        super(PickerItem, self).__init__(color=color, text=text, menu=menu, should_exit=True)
        self.selected = False
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