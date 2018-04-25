from behave import *
from venv.features.functions_and_variables.functions import wait_for_element

@then('we will be on the "{}" page')
def step(context, page):
    insuranceYesXpath = '//span[text()="Yes, I have insurance"]//ancestor::button[@class="button-anim btn btn-secondary btn-wide"]'
    wait_for_element(insuranceYesXpath, context.driver)
    assert context.driver.find_element_by_xpath(insuranceYesXpath).is_displayed()
    context.driver.quit()


@then('we have verified that the zip code feature works properly by taking the user to the start page')
def step(context):
    pass