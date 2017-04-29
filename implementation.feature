#Craig Busch
# -- FILE: features/implementation.feature
Feature: Implementing curses-menu

  Scenario: Create a CursesMenu
    Given we have curses-menu installed
     When we implement a CursesMenu with the title "Test Menu" and the subtitle "Subtitle"
     Then we will have an empty curses menu with a title

  Scenario: Create MenuItem named "MenuItem" in a curses menu
    Given we have a curse menu created
      When we implement a MenuItem
      Then we will have a curse menu containing a MenuItem

  Scenario: Create FunctionItem in a curses menu
    Given we have a curse menu created with a MenuItem
      When we implement a FunctionItem
      Then we will have a curse menu containing a FunctionItem

  Scenario: Create CommandItem in a curses menu
    Given we have a curse menu created with a MenuItem and a FunctionItem
      When we implement a CommandItem
      Then we will have a curse menu containing a CommandItem

  Scenario: Create selection SubmenuItem in a curses menu
    Given we have a curse menu created with a MenuItem and a FunctionItem and a CommandItem
      When we implement a selection SubmenuItem
      Then we will have a curse menu containing a SubmenuItem that contains a SelectionMenu

  Scenario: Create picker SubmenuItem in a curses menu
    Given we have a curse menu created with a MenuItem and a FunctionItem and a CommandItem and a selection SubmenuItem
      When we implement a picker SubmenuItem
      Then we will have a curse menu containing a SubmenuItem that contains a PickerMenu