from behave import *
from behave import given, when, then
import re
from cursesmenu import *

menu = CursesMenu('Title', 'Subtitle')

use_step_matcher("re")

@given("The user does not type anything")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("No input is put into the search")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    assert isinstance(string, str)
    context.tests_input = string
    pass  # there is no input

@then("The menu will not go to any matching item")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    assert menu.show()
    pass # there is no matching item


@given("The user types only one letter")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The letter is typed")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    assert isinstance(string, str)
    assert string == len(string) * string[0]
    context.tests_input = string
    pass  # input is a string of one letter

@then("The menu will show the first matching item")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    assert menu.show()
    pass # the menu will show a matching item if there is one

@given("The user types a single word")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The word is inputted into the search")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    assert isinstance(string, str)
    assert re.match(r'\A[\w-]+\Z', string)
    context.tests_input = string
    pass  # input is a string of one word

@then("The menu will show the first matching item")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    assert menu.show()
    pass # the menu will show the matching item if there is one


@given("The user types a phrase")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The phrase is inputted into the search")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    assert isinstance(string, str)
    context.tests_input = string
    pass  # input is a string of many words

@then("The menu will show the first matching item")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    assert menu.show()
    pass # the menu will show the matching item if there is one

@given("The user inputs a number")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The number is inputted into the search")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    assert re.match("^[0-9 ]+$", string)
    context.tests_input = string
    pass  # input is a string of numbers

@then("The menu will show the first matching item")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    assert menu.show()
    pass #the menu will show the matching item if there is one