from behave import *
from venv.features.functions_and_variables.functions import wait_for_element,  wait_for_element_to_load_and_click_on_element
from venv.features.functions_and_variables.functions import click_button_that_contains_passed_in_text
from datetime import timedelta, datetime, date, time


user_age = 0


@given('we navigate to "{}"')
def step(context, link):
    context.driver.get(link)


@then('we enter "{}" into the "{}" field')
def step(context, text, field):
    xpath = "//input[@placeholder='" + field + "']"
    wait_for_element(xpath, context.driver)
    context.driver.find_element_by_xpath(xpath).send_keys(text)


@then('we click "{}" in the "{}"')
def step(context, item, menu):
    menu_xpath = "//input[@placeholder='" + menu + "']"

    wait_for_element_to_load_and_click_on_element(menu_xpath, context.driver)

    if menu == 'Vehicle Year':
        xpath = "//*[contains(text(), '" + item + "')]"

    if menu == 'Vehicle Make':
        xpath = "//*[@class='vehicle-question make']//*[contains(text(), '" + item + "')]"

    if menu == 'Vehicle Model':
        xpath = "//*[@class='vehicle-question model']//*[contains(text(), '" + item + "')]"

    wait_for_element_to_load_and_click_on_element(xpath, context.driver)


@then('we click the button that contains the text "{}"')
def step(context, text):
    click_button_that_contains_passed_in_text(text, context.driver)


@then('we select "{}" for the "{}" section')
def step(context, answer, field):
    if field == 'currently insured':
        if answer == 'yes':
            xpath = "//*[@id='prev_insured-true']"
        if answer == 'no':
            xpath = "//*[@id='prev_insured-false']"

    if field == "homeowner":
        if answer == 'yes':
            xpath = "//*[@id='home_ownership-true']"
        if answer == 'no':
            xpath = "//*[@id='home_ownership-false']"

    if field == "married":
        if answer == 'yes':
            xpath = "//*[@id='marital_status-true']"
        if answer == 'no':
            xpath = "//*[@id='marital_status-false']"

    context.driver.find_element_by_xpath(xpath).click()


@then('we click the age button that contains the text "{}"')
def step(context, text):
    user_age = text
    click_button_that_contains_passed_in_text(text, context.driver)


@then('verify dob info')
def step(context):
    dobID = 'date_of_birth'
    xpath = "//*[@id='" + dobID + "']"
    dobPageInfo = context.driver.find_element_by_xpath(xpath)
    dob = dobPageInfo.get_attribute('value').split('/')[2]
    now = datetime.now()
    years = now.year
    age = years - int(dob)

    if user_age == '16-20':
        assert age == 18

    if user_age == '21-36':
        assert age == 28

    if user_age == '37-59':
        assert age == 48

    if user_age == '60+':
        assert age == 65


@then('we verified we can go through the entire funnel and get to the rates page from the widget')
def step(context):
    pass