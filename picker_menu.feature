#Craig Busch
# -- FILE: features/picker_menu.feature
Feature: Multi-selection submenu (picker_item)

  Scenario: Select a single item
    Given we have a PickerMenu created with 3 unselected items
      When we toggle the first item
      Then the first item is now selected

  Scenario: Select multiple items
    Given we have a PickerMenu created with the first item set as selected
      When we toggle the second item
      Then the second item is now selected

  Scenario: Un-select an item
    Given we have a PickerMenu created with 3 selected items
      When we toggle the last item
      Then the last item is now un-selected

  Scenario: Gather selections
    Given we have a PickerMenu created with 2 selected items and 1 unselected items
      When we enter the selections
      Then the PickerMenu will return a list of 2 selections