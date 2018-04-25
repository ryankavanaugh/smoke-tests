from behave import *
import time
from venv.features.functions_and_variables.variables import prepop_link, jesse_durante_payload, laura_johnson_payload, release_and_prod_prepop_headers, thirteen_prepop_headers
from venv.features.functions_and_variables.functions import enter_form_field, select_form_option, click_prepop_button, wait_for_drivers_page_element_to_load_and_verify_text
from venv.features.functions_and_variables.functions import wait_for_element
from venv.features.functions_and_variables.functions import post_to_API_and_return_link
from venv.features.functions_and_variables.prepop_variables import *

@given('we navigate to Prepop')
def step(context):
    context.driver.get(prepop_link)


@given('we post "{}" to the Prepop API')
def step(context, JsonName):
    if JsonName == 'Jesse Durante Json':
        payload = jesse_durante_payload

    if JsonName == 'Laura Johnson Json':
        payload = laura_johnson_payload

    if context.test_environment == 'onebox-13':
        prepop_headers = thirteen_prepop_headers
    else:
        prepop_headers = release_and_prod_prepop_headers

    context.prepop_to_funnel_link = post_to_API_and_return_link(context, payload, context.prepop_api_link, prepop_headers)


@then('we navigate to the API response link')
def step(context):
    context.driver.get(context.prepop_to_funnel_link)


@when('we enter "{}" "{}" in the "{}" section')
def step(context, field, value, form):
    enter_form_field(field=field, value=value, form=form, driver=context.driver)


@when('we select "{}" "{}" in the "{}" section')
def step(context, fields, text, form):
    select_form_option(text=text, fields=fields, form=form, driver=context.driver)


@then('we click the "{}" prepop button')
def step(context, button):
    click_prepop_button(button, driver=context.driver)


@then('we verify the "{}" is correct')
def step(context, button):
    json = context.driver.find_element_by_xpath('//*[@id="request"]').text
    assert prepopPayloadJsonJesseDurante == json


@then('we check that "{}" has populated the "{}" field')
def step(context, text, xpathID):
    xpath = "//*[@id='" + xpathID + "']"
    wait_for_drivers_page_element_to_load_and_verify_text(xpath, text, driver=context.driver)


@then('we check that the gender button has been selected correctly as "{}"')
def step(context, gender):
    selectedGenderButton = context.driver.find_element_by_xpath("//*[@id='gender']//button[@class='button-anim active btn btn-secondary btn-wide active']")
    assert selectedGenderButton.text == gender


@then('we check that the "{}" section has been selected with the "{}" button')
def step(context, section, button):
    xpath = '//*[@id="' + section + '"]//button[@class="button-anim active btn btn-secondary btn-wide active"]'
    wait_for_element(xpath, context.driver)
    selectedButton = context.driver.find_element_by_xpath(xpath)
    assert selectedButton.text == button


@then('we check that "{}" has been selected with the "{}" button')
def step(context, category, button_name):
    xpath = '//*[@id="' + prepop_locators[category] + '"]//button[@class="button-anim active btn btn-secondary btn-wide active"]'
    wait_for_element(xpath, context.driver)
    selectedButton = context.driver.find_element_by_xpath(xpath)
    assert selectedButton.text == button


@then('we check that the "{}" dropdown has been selected with "{}"')
def step(context, section, text):
    xpath = '//*[@id="' + section + '"]//*[@class="form-control"]'
    wait_for_element(xpath, context.driver)
    selectedMenuItem = context.driver.find_element_by_xpath(xpath)
    assert selectedMenuItem.get_attribute('placeholder') == text, selectedMenuItem.get_attribute('placeholder')


@then('we have verified that we see the proper prepop data in the funnel and we can see rates on the rates select page at the end of the funnel')
def step(context):
    pass


@then('we sleep')
def step(context):
    time.sleep(60)
    pass


@then('we go to the drivers primary page')
def step(context):
    url = context.zebra_url + 'z/questions/start/'
    context.driver.get(url)