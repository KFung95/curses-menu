# Created by michael at 4/4/2017
Feature: Select the First Matching Menu Item
  # The program will select the first matching menu item
  # when the user types

  Scenario: The user types nothing
    Given The user does not type anything
    When No input is put into the search
    Then The menu will not go to any matching item

  Scenario: The user types one letter
    Given The user types only one letter
    When The letter is typed
    Then The menu will show the first matching item

  Scenario: The user types one word
    Given The user types a single word
    When The word is inputted into the search
    Then The menu will show the first matching item

  Scenario: The user types a whole phrase
    Given The user types a phrase
    When The phrase is inputted into the search
    Then The menu will show the first matching item

  Scenario: The user types a number
    Given The user inputs a number
    When The number is inputted into the search
    Then The menu will show the first matching item