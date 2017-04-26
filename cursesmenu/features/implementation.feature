#Craig Busch
# -- FILE: features/implementation.feature
Feature: Implementing curses-menu

  Scenario: Create a CursesMenu
    Given we have curses-menu installed
     When we implement a CursesMenu with the title "Test Menu" and the subtitle "Subtitle"
     Then we will have an empty curses menu with a title

  Scenario: Create a PickerMenu
    Given we have curses-menu installed
      When we implement a PickerMenu with a list of selections
      Then we will have a populated PickerMenu

  Scenario: Create a SelectionMenu
    Given we have curses-menu installed
      When we implement a SelectionMenu with a list of selections
      Then we will have a populated SelectionMenu

  Scenario: Create MenuItem named "MenuItem" in a curses menu
    Given we have a curse menu created
      When we implement a MenuItem
      Then we will have a curse menu containing a MenuItem

  Scenario: Create FunctionItem in a curses menu
    Given we have a curse menu created
      When we implement a FunctionItem
      Then we will have a curse menu containing a FunctionItem

  Scenario: Create CommandItem in a curses menu
    Given we have a curse menu created
      When we implement a CommandItem
      Then we will have a curse menu containing a CommandItem

  Scenario: Create selection SubmenuItem in a curses menu
    Given we have a curse menu created
      When we implement a selection SubmenuItem
      Then we will have a curse menu containing a SubmenuItem that contains a SelectionMenu

  Scenario: Create picker SubmenuItem in a curses menu
    Given we have a curse menu created
      When we implement a picker SubmenuItem
      Then we will have a curse menu containing a SubmenuItem that contains a PickerMenu