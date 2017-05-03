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

@when("The user enters an input")
def step_impl(context, string):
    """
     :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)

@then("The Input Should be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()


@given("The input is not in the dictionary")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user enters an input")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)

@then("The input will not be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()


@given("The input is a one letter word in the dictionary")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user enters an input")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)

@then("The input should be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()

@given("The input is a one letter word not in the dictionary")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user enters an input")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)

@then("The input will not be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """


@given("The input is a Homograph")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user enters an input")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)

@then("The input should be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()


@given("The input is a Heteronym")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user enters an input")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)

@then("The input should be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()


@given("The input is a Homonym")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass
@when("The user enters an input")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)

@then("The input should be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    input.map()


@given("The input is a misspelled word")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass

@when("The user enters an input")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)

@then("The input will not be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """


@given("The input is not a word in the English language")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass
@when("The user enters an input")
def step_impl(context, string):
    """
    :type string: input
    :type context behave.runner.Context 
    """
    d = enchant.Dict("en_US")
    assert d.check(string)

@then("The input will not be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """


@given("The input is a number")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass
@when("The user enters an input")
def step_impl(context, string):
    """
    :type int: input
    :type context behave.runner.Context 
    """
    assert re.match("^[0-9 ]+$", string)

@then("The input will not be mapped")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
