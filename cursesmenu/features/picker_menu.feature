#Craig Busch
# -- FILE: features/picker_menu.feature
Feature: Multi-selection submenu (picker_item)

  Scenario: Select a single item
    Given we have a curse menu created
    And we have a PickerMenu created with a list
    And the PickerMenu is appended as a SubmenuItem to the curse menu
    And the PickerMenu has no selections
      When we hit the space bar while hovering over an unselected item
      Then the item is now selected

  Scenario: Select multiple items
    Given we have a curse menu created
    And we have a PickerMenu created with a list
    And the PickerMenu is appended as a SubmenuItem to the curse menu
    And the PickerMenu has existing selections
      When we hit the space bar while hovering over an unselected item
      Then the item is now selected

  Scenario: Un-select an item
    Given we have a curse menu created
    And we have a PickerMenu created with a list
    And the PickerMenu is appended as a SubmenuItem to the curse menu
      When we hit the space bar while hovering over a selected item
      Then the item is now un-selected

  Scenario: Submit selected item(s)
    Given we have a curse menu created
    And we have a PickerMenu created with a list
    And the PickerMenu is appended as a SubmenuItem to the curse menu
      When we hit the enter key with 2 selections
      Then the PickerMenu will return a list of 2 selections