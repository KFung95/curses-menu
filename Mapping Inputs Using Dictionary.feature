# Created by michael at 4/2/2017

Feature: Mapping Inputs Using Dictionary
  # The program will map user inputs by comparing them
  # to words in the dictionary.

  Scenario: The given input is in the dictionary.
    Given The input is in the dictionary
    When The user runs the menu
    Then The input should be mapped

  Scenario: The given input is not in the dictionary.
    Given The input is not in the dictionary
    When The user runs curses menu
    Then The input will not be mapped.

  Scenario: One letter input in the dictionary.
    Given The input is a one letter word in the dictionary
    When The user uses the menu
    Then The input will be mapped

  Scenario: One letter input not in the dictionary
    Given The input is a one letter word not in the dictionary.
    When The user uses the curses menu
    Then The input should not be mapped

  Scenario: Input is a Homograph.
    Given The input is a homograph in the dictionary
    When The user starts the curses menu
    Then The input should map

  Scenario: Input is a Heteronym
    Given the input is a heteronym in the dictionary
    When The user starts the menu
    Then the input is mapped

  Scenario: Input is a Homonym
    Given The input is a homonym in the dictionary
    When The user runs curses
    Then the input is then mapped

  Scenario: The input is misspelled
    Given The input is a misspelled word
    When The user starts the program
    Then the input is not mapped

  Scenario: The input is not an English word.
    Given The input is not a word in the English language
    When The user runs the program
    Then the input isnt mapped

  Scenario: The given input is a number
    Given The input is a number
    When The user starts up curses menu
    Then The input is not to be mapped
