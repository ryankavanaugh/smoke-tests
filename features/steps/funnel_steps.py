from behave import *
from random import *
import time
from venv.features.functions_and_variables.functions import wait_for_element_to_load_and_click_on_element
from venv.features.functions_and_variables.functions import wait_for_element_to_load_and_enter_text_into_element
from venv.features.functions_and_variables.functions import wait_for_element, action_chains_move_to_element_and_click_on_it
from venv.features.functions_and_variables.functions import navigate_to_the_zebra, return_xpath
from venv.features.functions_and_variables.functions import wait_for_drivers_page_element_to_load_and_enter_text, wait_element_present_and_find
from venv.lib.utils.core.element_action import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


def brief_wait():
    time.sleep(1)


funnel_id_locators = {
    # home page
    'zip code' : 'zipcode-form-control',

    # start page
    'Yes, I have insurance' : 'qmcCurrently_insuredYesIHaveInsurance',
    "No, I don't" : 'qmcCurrently_insuredNoIDont',

    # vehicle's page 1
    'vehicle\'s save & continue' : 'vehiclesPrimarySaveBtn',
    'additional vehicle save & continue' : 'vehiclesAdditionalSaveBtn',
    
    # vehicle's page 2
    'paid in full' : 'qmcOwnershipOwn-PaidInFull',
    'making payments' : 'qmcOwnershipOwn-MakingPayments',
    'lease' : 'qmcOwnershipLease',
    'personal/commuting' : 'qmcPrimary_usePersonalcommuting',
    'pleasure' : 'qmcPrimary_usePleasure',
    'farm' : 'qmcPrimary_useFarm',
    'business' : 'qmcPrimary_useBusiness',
    'very low' : 'qmcMiles0-7500',
    'low' : 'qmcMiles7501-10000',
    'average' : 'qmcMiles10001-15000Average',
    'high' : 'qmcMilesMoreThan15000',

    # vehicles summary page
    'vehicle\'s final save & continue' : 'vehicleSaveBtn',
    'add vehicle' : 'vehiclesAddVehicleBtn',
    'edit vehicle' : 'vehiclesEditBtn0',
    'remove vehicle' : 'vehiclesRemoveBtn0',
    'edit second vehicle': 'vehiclesEditBtn1',
    'remove second vehicle': 'vehiclesRemoveBtn1',

    # driver's page 1
    'first name' : 'first_name',
    'last name' : 'last_name',
    'birthdate' : 'date_of_birth',
    'email' : 'email',
    'phone' : 'phone',
    'male' : 'qmcGenderMale',
    'female' : 'qmcGenderFemale',
    'driver\'s save & continue' : 'driversPrimarySaveBtn',

    # driver's page 2
    'single' : 'qmcMarital_statusSingle',
    'married' : 'qmcMarital_statusMarried',
    'divorced' : 'qmcMarital_statusDivorced',
    'widowed' : 'qmcMarital_statusWidowed',
    'poor credit' : 'qmcCredit_scorePoorBelow580',
    'average credit' : 'qmcCredit_scoreAverage580-679',
    'good credit' : 'qmcCredit_scoreGood680-719',
    'excellent credit' : 'qmcCredit_scoreExcellent720',
    'no diploma' : 'qmcEducationNoDiploma',
    'high school diploma' : 'qmcEducationHighSchoolDiplomaged',
    'bachelor\'s degree' : 'qmcEducationBachelorsDegree',
    'master\'s degree' : 'qmcEducationMastersDegree',
    'doctoral degree' : 'qmcEducationDoctoralDegree',
    'own home' : 'qmcResidence_ownershipOwnHome',
    'own condo' : 'qmcResidence_ownershipOwnCondo',
    'rent' : 'qmcResidence_ownershipRent',
    'other' : 'qmcResidence_ownershipOther',
    'less than 6 months' : 'qmcInsured_lengthLessThan6Months',
    '6 to 12 months' : 'qmcInsured_length6To12Months',
    '1 to 3 years' : 'qmcInsured_length1To3Years',
    'more than 3 years' : 'qmcInsured_lengthGreaterThan3Years',
    'yes' : 'qmcViolationsYes',
    'no' : 'qmcViolationsNo',

    # drivers summary page
    'driver\'s final save & continue' : 'driverSaveBtn',
    'edit driver' : 'driversEditBtn0',
    'remove driver' : 'driversRemoveBtn0',
    'edit second driver' : 'driversEditBtn1',
    'remove second driver' : 'driversRemoveBtn1',

    # 2nd driver specific IDs
    'add driver' : 'driversAddDriverBtn',
    'additional driver save & continue' : 'driversAdditionalSaveBtn',

    # discount's page 1
    'currently employed' : 'currently_employed-0',
    'currently unemployed' : 'currently_employed-1',
    'on active duty' : 'active_military-0',
    'not on active duty' : 'active_military-1',
    'pay in full' : 'pay_up_front-0',
    'do not pay in full' : 'pay_up_front-1',
    'set up auto-pay' : 'auto_pay-0',
    'do not set up auto-pay' : 'auto_pay-1',
    'go paperless' : 'paperless-0',
    'do not go paperless' : 'paperless-1',
    'discounts save & continue' : 'discountsUndefinedSaveBtn',
    'discounts final save & continue' : 'discountSaveBtn',

    # summary page
    'show my quotes' : 'summaryShowQuotesBtn',
    'edit vehicles' : 'summaryVehicleEditBtn',
    'edit drivers': 'summaryDriverEditBtn'
}


@given('we navigate to the Zebra')
def step(context):
    navigate_to_the_zebra(context, context.driver)


@then('we enter "{}" into the zip code field')
def step(context, zipcode):
    zipCodeID = context.driver.find_element_by_id('zipcode-form-control')
    zipCodeID.send_keys(zipcode)


@then('we clear the zipcode text')
def step(context):
    context.driver.find_element_by_id('zipcode-form-control').clear()


@when('we enter "{}" "{}" and click submit')
def step(context, zip_code, zip_code_number):
    context.user_funnel_info['zipcode'] = zip_code_number
    zip_code_xpath = return_xpath('id', funnel_id_locators[zip_code])
    wait_for_element_to_load_and_enter_text_into_element(zip_code_xpath, zip_code_number, context.driver)
    brief_wait()
    context.driver.find_element_by_xpath(zip_code_xpath).submit()


@when('we select "{}" on the Start page')
def step_impl(context, insurance_status):
    wait_for_element_to_load_and_click_on_element(return_xpath('id', funnel_id_locators[insurance_status]), context.driver)


@when('we enter "{}" for car "{}"')
def step_impl(context, variable, car_variable):
    brief_wait()
    id = car_variable + variable
    wait_for_element_to_load_and_click_on_element(return_xpath('id', id), context.driver)


@then('we enter "{}" for "{}"')
def step_impl(context, user_input, use):
    if use != 'ownership status' or use != 'relationship' or use != 'gender':
        brief_wait()
    wait_for_element_to_load_and_click_on_element(return_xpath('id', funnel_id_locators[user_input]), context.driver)


@then('we enter "{}" in the "{}" field')
def step(context, user_input, id):
    # gathers info for admin tests
    dict_key = id.replace("_", " ") # 777
    context.user_funnel_info[dict_key] = user_input
    wait_for_drivers_page_element_to_load_and_enter_text(return_xpath('id', funnel_id_locators[id]), user_input, context.driver)


@then('we enter the street address is "{}"')
def step(context, street_address):
    context.user_funnel_info['address'] = street_address
    addressFormXpath = "//input[@id='garaging_addressInput']"
    wait_for_element_to_load_and_enter_text_into_element(addressFormXpath, street_address, context.driver)
    try:
        # Wait for the drop down menu to show and click to close it
        xpath = "//div[@id='PlacesAutocomplete__autocomplete-container']"
        wait_for_element(xpath, context.driver)
        wait_for_element_to_load_and_click_on_element(xpath, context.driver)
        # element = wait_element_present_and_find(context.driver, xpath)
    except:
        pass


@then('we enter "{}" as the current insurance provider')
def step(context, current_insurance):
    brief_wait()
    xpath = "//div[text()='" + current_insurance + "']"
    wait_for_element_to_load_and_click_on_element(xpath, context.driver)


@then('we click the "{}" button')
def step(context, button):
    brief_wait()
    wait_for_element_to_load_and_click_on_element(return_xpath('id', funnel_id_locators[button]), context.driver)


@then('we click the second driver "{}" button')
def step(context, button):
    brief_wait()
    xpath = "//span[text()='2 Drivers']/ancestor::*[position()=1]//span[text()='Edit']"
    wait_for_element(xpath, context.driver)
    context.driver.find_element_by_xpath(xpath).click()


@then('we click the second "{}" button to "{}"')
def step(context, button, step_descriptor):
    brief_wait()
    xpath = "*//span[text()='" + button + "']"
    wait_for_element(xpath, context.driver)
    edit_list = context.driver.find_elements_by_xpath(xpath)
    edit_list[1].click()


@then('we enter "{}" on the "{}" question')
def step(context, answer, question):
    xpath = return_xpath('id', funnel_id_locators[answer]) + '/ancestor::label'
    wait_for_element_to_load_and_click_on_element(xpath, context.driver)


@then('we assert there are "{}" "{}" objects on the page')
def step(context, property, text):
    time.sleep(5)
    try:
        wait_for_element("//*[contains(@" + property + ", '" + text + "')]", context.driver)
        element = context.driver.find_element_by_class_name(text)
        assert element.is_displayed()
        # print(element.text)
    except Exception as e:
        print(e)
        assert False


@then('we wait')
def step(context):
    time.sleep(4)


@then('we verify we can go through the entire funnel and get to the rates page')
def step(context):
    # Save the session id to a global variable for admin info
    zebra_cookie = context.driver.get_cookies()
    for item in zebra_cookie:
        if item.get('name') == 'sessionid':
            context.session_id = item.get('value')
            context.user_funnel_info['session id'] = context.session_id
    pass


@then('we have verified that we were able to create multiple drivers and vehicles and delete a driver and a vehicle successfully')
def step(context):
    pass


@then('we check if the ethnio survey is open and close it if it is')
def step(context):
    try:
        context.driver.find_element_by_xpath("//*[@id='ethnio-campaign-theme']/div[2]").click()
    except:
        pass
