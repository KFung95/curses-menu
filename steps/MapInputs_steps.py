from behave import *
from behave import given, when, then
import enchant
import re

use_step_matcher("re")


@given("The input is in the dictionary")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user runs the menu")
def step_impl(context, string):
    """
     :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)
    pass # the menu has words in dictionary

@then("The Input Should be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()
    pass # input is mapped


@given("The input is not in the dictionary")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user runs curses menu")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)
    pass # any input not in the dictionary

@then("The input will not be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()
    pass # input not mapped

@given("The input is a one letter word in the dictionary")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user uses the menu")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)
    pass #input is one letter word in dictionary

@then("The input will be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()
    pass #input is mapped

@given("The input is a one letter word not in the dictionary")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user uses the curses menu")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)
    pass #input is one letter word not in dictionary

@then("The input should not be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass #input not mapped


@given("The input is a Homograph")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user starts the curses menu")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)
    pass #input is a homograph in the dictionary

@then("The input should map")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()
    pass #input is mapped


@given("The input is a Heteronym")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user starts the menu")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)
    pass #input is a heteronym in dictionary

@then("The input is mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()
    pass #input is mapped


@given("The input is a Homonym")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user runs curses")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)
    pass #input is a homonym in dictionary

@then("The input is then mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()
    pass #input is mapped


@given("The input is a misspelled word")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user starts the program")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)
    pass #input is a misspelled word not in dictionary

@then("The input is not mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass #input is not mapped


@given("The input is not a word in the English language")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user runs the program")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)
    pass #input is not word in english dictionary

@then("The input isnt mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass #input is not mapped

@given("The input is a number")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user starts up curses menu")
def step_impl(context, string):
    """
    :type int: input
    :type context behave.runner.Context 
    """
    assert re.match("^[0-9 ]+$", string)
    pass #the input is a number not in the dictionary

@then("The input is not to be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass #input is not mapped