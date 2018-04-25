from behave import *
from selenium import webdriver
from features.mobile import HomePageMobile
from lib.utils.core.js_executors import JSExecutors
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from features.mobile_functions.functions import *


mobile_locators = {
    # drop down menu items
    "mileage" : "//*[@name='mileage']//*[@value='0']",
    "insured" : "//*[@name='insured']//*[@value='-2']",
    "education" : "//*[@name='education']//*[@value='2']",
    "coverage" : "//select[@name='coverage']//*[@value='2']",

    # user input buttons
    "male" : "//*[@id='gender-male']//ancestor::label",
    "good credit" : "//*[@id='credit-good']//ancestor::label",
    "own a home" : "//*[@id='homeowner-yes']//ancestor::label",
    "married" : "//*[@id='maritalstatus-yes']//ancestor::label",
    "no additional drivers" : "//*[@class='option-wrap option-drivers']//*[contains(text(),'Nope')]",
    "no additional vehicles" : "//*[@class='option-wrap option-vehicles']//*[contains(text(),'Nope')]",
    "no tickets" : "//*[@id='incidents-no']//ancestor::label",

    # continue buttons
    "birthday button" : "//button[contains(@data-reactid,'Birthday')]",
    "name button" : "//button[contains(@data-reactid,'Name')]/span[text()='Continue']",
    "get quotes button" : "//span[text()='Get Quotes']",

    # text
    "birthday": "//input[@class='form-control birthday-text']",
    "first name" : "//*[@id='first_name']",
    "last name" : "//*[@id='last_name']",
    "address" : '//*[@id="address"]',
    "phone number" :"//*[@id='phone_number']",
    "email" : "//*[@id='email']"
}


@given('I navigate to the zebra on mobile')
def step(context):
    if context.device == 'local':
        desired_caps = {
            "browserName": "Chrome",
            "platformName": "Android",
            "platformVersion": "8.1.0",
            "deviceName": "Nexus 5X API 21 1080x1920",
            "ID": 1}
        context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    if context.device == 'real':
        desired_caps = {
            "browserName": "Chrome",
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "Android",
            "ID": 1
        }
        context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    context.driver.get(context.prefix + '.thezebra.com/')


@then('I enter zip code "{}"')
def step(context, zip):
    login_to_the_mobile_application_with_valid_data(zip, context.driver)


@then('I enter "{}" as the car "{}"')
def step(context, text, field):
    select_vehicle_info(text, field, context.driver)


@then('I click continue')
def step(context):
    click_continue_button_under_vehicle_insuring(context.driver)


@then('we select "{}" for "{}"')
def step(context, input, category):
    xpath = mobile_locators[category]
    element = WebDriverWait(context.driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element = WebDriverWait(context.driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    JSExecutors.wait_for_page_to_load(context.driver, 60)
    element.click()


@then('we select the "{}" button for "{}"')
def step(context, input, category):
    xpath = mobile_locators[input]
    element = WebDriverWait(context.driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    JSExecutors.wait_for_page_to_load(context.driver, 60)
    element.click()
    if 'additional drivers' not in input:
        wait_until_not_visible((By.XPATH, xpath), context.driver)


@then('we enter "{}" for "{}"')
def step(context, input, category):
    updated_input = input.replace("/", "")
    element = WebDriverWait(context.driver, 60).until(EC.element_to_be_clickable((By.XPATH, mobile_locators[category])))
    element.send_keys(updated_input)
    # wait_until_element_contains_value((By.XPATH, mobile_locators[category]), input, context.driver)
    JSExecutors.remove_focus(context.driver, element)
    JSExecutors.scroll_top(context.driver)

@then('back up address funcion')
def step(context):
    click_address_continue_button(context.driver)


@then('we click the "{}"')
def step(context, button_category):
    JSExecutors.scroll_top(context.driver)
    xpath = mobile_locators[button_category]
    locator = (By.XPATH, xpath)
    wait_for_element_become_clickable(locator, context.driver)
    wait_element_present_and_find(locator, context.driver).click()
    wait_until_not_visible(locator, context.driver)
    JSExecutors.scroll_top(context.driver)


@then('we click the continue button on the address page')
def step(context):
    click_address_continue_button(context.driver)


@then('we click the get quotes button')
def step(context):
    try:
        JSExecutors.scroll_top(context.driver)
        button_xpath = "//span[text()='Get Quotes']"
        button_element = WebDriverWait(context.driver, 5).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        button_element.click()
    except:
        pass


@then('we verify rates are on the page')
def step(context):
    xpath = "//*[@class='carrier-name']"
    element = WebDriverWait(context.driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    assert context.driver.find_element_by_xpath(xpath)
