from behave import *
from venv.features.functions_and_variables.functions import cookie_data_validation


@given('we navigate to the zebra attribution page')
def step(context):
    context.driver.get(context.zebra_url + 'car-insurance-companies/esurance-auto-insurance/')


@then('we verify attribution with cookie info validation')
def step(context):
    zebra_start_page_cookie = context.driver.get_cookies()
    desired_source = 'thezebra'
    desired_medium = 'cpc'
    desired_channel_id = '6kpw01'
    cookie_data_validation(zebra_start_page_cookie, desired_source, desired_medium, desired_channel_id)
