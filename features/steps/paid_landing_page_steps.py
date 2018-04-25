from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from venv.features.functions_and_variables.functions import navigate_to_the_zebra_paid_landing_page, wait_for_element, switch_to_current_tab, wait_for_drivers_page_element_to_load_and_enter_text
from venv.features.functions_and_variables.functions import click_button_found_via_inner_text, switch_to_current_tab_option_2


landing_page_elements = {"zipcode": "zipcode-form-control"}


@given('we navigate to the Zebra paid landing page')
def step(context):
    navigate_to_the_zebra_paid_landing_page(context, context.driver)


@then('we click the paid landing page button that contains the text "{}"')
def step(context, inner_text):
    click_button_found_via_inner_text(context.driver, inner_text)
    # context.driver.find_element_by_xpath("//*[contains(text(), '" + inner_text + "')]")


@then('we enter "{}" in the "{}" landing page field')
def step(context, text, field_name):
    element_id = landing_page_elements[field_name]
    xpath = "//*[@id='" + element_id + "']"
    wait_for_drivers_page_element_to_load_and_enter_text(xpath, text, context.driver)


@then('we assert that a valid "{}" is required to move onto the funnel')
def step(context, field_name):
    element_id = landing_page_elements[field_name]
    context.driver.find_element_by_id(element_id).submit()
    assert context.driver.find_element_by_xpath("//*[@class='zip-error-text']")
    assert len(context.driver.find_elements_by_xpath('*//span[text()="Yes, I have insurance"]')) < 1


@then('we clear the "{}" field')
def step(context, field_name):
    element_id = landing_page_elements[field_name]
    context.driver.find_element_by_id(element_id).clear()


@then('we click submit on the "{}" field')
def step(context, field_name):
    element_id = landing_page_elements[field_name]
    context.driver.find_element_by_id(element_id).submit()
    # xpath = '*//span[text()="Yes, I have insurance"]'
    # wait_for_element(xpath, context.driver)


@then('we switch to the current tab')
def step(context):
    switch_to_current_tab(context.driver)


@then('we print the page title')
def step(context):
    page_title = (context.driver.title)
    if 'Compare Car Insurance Rates: Fast, Free, Simple | The Zebra' in page_title:
        print('Yas!!!')


@then('we assert "{}" is on the page')
def step(context, field):
    xpath = '*//span[text()="' + field + '"]'
    wait_for_element(xpath, context.driver)
    pageText = context.driver.find_element_by_xpath(xpath).text
    assert pageText == field, 'Page text:' + pageText


@then('we have verified we can bridge over from the paid landing page to the funnel and see rates on the rate select page')
def step(context):
    pass


@then('we have verified a correct zip code is required to move onto the funnel from the paid landing page')
def step(context):
    pass



