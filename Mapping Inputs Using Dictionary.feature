# Created by michael at 4/2/2017

Feature: Mapping Inputs Using Dictionary
  # The program will map user inputs by comparing them
  # to words in the dictionary.

  Scenario: Input is in the dictionary.
    Given The input is in the dictionary
    When The user enters an input
    Then The input should be mapped

  Scenario: Input is not in the dictionary.
    Given The input is not in the dictionary
    When The user enters an input
    Then The input will not be mapped.

  Scenario: One letter input in the dictionary.
    Given The input is a one letter word in the dictionary
    When The user enters an input
    Then The input should be mapped.

  Scenario: One letter input not in the dictionary
    Given The input is a one letter word not in the dictionary.
    When The user enters an input
    Then The input will not be mapped.

  Scenario: Input is a Homograph.
    Given The input is a homograph in the dictionary
    When The user enters an input
    Then The input should be mapped

  Scenario: Input is a Heteronym
    Given the input is a heteronym in the dictionary
    When The user enters an input
    Then the input should be mapped

  Scenario: Input is a Homonym
    Given The input is a homonym in the dictionary
    When The user enters an input
    Then the input should be mapped

  Scenario: The input is misspelled
    Given The input is a misspelled word
    When The user enters an input
    Then the input will not be mapped

  Scenario: The input is not an English word.
    Given The input is not a word in the English language
    When The user enters an input
    Then the input will not be mapped

  Scenario: The input is a number
    Given The input is a number
    When The user enters an input
    Then The input will not be mapped
