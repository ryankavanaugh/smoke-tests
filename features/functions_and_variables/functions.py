from behave import *
from selenium.webdriver.support.ui import Select
import requests
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from exceptions import Exception
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException, WebDriverException
from venv.lib.utils.seleniumwrappers import Element
# from venv.features.functions_and_variables.variables import zebra_url, prepop_api_link, prepop_headers
from venv.lib.utils.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import shutil
import logging
import os
import sys
from datetime import *
from selenium.webdriver.common.by import By


def return_environment_prefix(test_environment):
    environment = ''
    if test_environment == 'onebox-release':
        environment = 'https://release.onebox'
    if test_environment == 'onebox-13':
        environment = 'https://13.onebox'
    if test_environment == 'production':
        environment = 'https://www'
    return environment


def create_zebra_link(environment_prefix):
    return environment_prefix + '.thezebra.com/'


def create_prepop_link(environment_prefix):
    return environment_prefix + '.thezebra.com/prepoptest/'


def create_prepop_api_link(environment_prefix):
    return environment_prefix + '.thezebra.com/api/ext/v1/prepop/'


def create_drift_api_link(environment_prefix):
    if environment_prefix == 'https://www':
        return 'https://release.onebox.thezebra.com/rate_request/itc/auto/'
    else:
        return environment_prefix + '.thezebra.com/rate_request/itc/auto/'


def navigate_to_the_zebra(context, driver):
    driver.get(context.zebra_url)


def navigate_to_the_zebra_paid_landing_page(context, driver):
    zebra_paid_landing_page_url = context.zebra_url + 'compare/start/'
    driver.get(zebra_paid_landing_page_url)


def return_xpath(type, locator):
    if type == 'id':
        return "//*[@id='" + locator + "']"
    elif type == 'class':
        return "//*[@class='" + locator + "']"
    else:
        assert False, 'no xpath was created via the return_xpath function'


def wait_for_element_to_load_and_click_on_element(xpath, driver):
    try:
        wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
    except:
        assert False, 'This element did not load properly: '


def wait_for_element_to_load_and_enter_text_into_element(xpath, text, driver):
    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.clear()
        element.send_keys(text)
    except:
        assert False, 'This element did not load properly: ' + xpath


def action_chains_move_to_element_and_click_on_it(driver, xpath):
    element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    ActionChains(driver).move_to_element(element).click().perform()


def wait_for_drivers_page_element_to_load_and_verify_text(xpath, text_for_verification, driver):
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    page_text = element.get_attribute('value')
    assert page_text == text_for_verification, 'Page text:' + page_text


def wait_for_drivers_page_element_to_load_and_enter_text(xpath, text, driver):
    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(text)
    except:
        assert False, 'This element did not load properly: ' + xpath


def switch_to_current_tab(driver):
    WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])


def switch_to_current_tab_option_2(driver):
    WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+Keys.PAGE_UP)


def wait_for_element(xpath, driver):
    try:
        wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        assert False, 'This element did not load properly: ' + xpath


def print_test():
    print('Test complete!')


def click_button_found_via_inner_text(driver, inner_text):
    xpath = "//*[contains(text(), '" + inner_text + "')]"
    wait_for_element(xpath, driver)
    driver.find_element_by_xpath(xpath)


prepopLocators = {
        "prepop": (By.XPATH, "//span[text()='%s']"),
        "check_section": (By.XPATH, "//div[@class='container prepop-page']/div[@class='row']/div[%s]"),
        "select_form_field": (By.XPATH, "//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]//label[text()='%s']/parent::div/select"),
        "form_button": (By.XPATH, "//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]//*[text()='%s']"),
        "form_field": (By.XPATH, "//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]//input[contains(@placeholder,'%s')]"),
        "additional_form_field": (By.XPATH, "//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]//div[contains(@class,'%s-form')]["
                                            "%s]//input[contains(@placeholder,'%s')]"),
        "select_additional_form_field": (By.XPATH, "//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]//div[contains(@class,'%s-form')]["
                                                   "%s]//label[text()='%s']/parent::div/select"),
        "select_incident": (By.XPATH, "//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]//div[contains(@class,'driver-form')][%s]//div["
                                      "contains(@class,'incident-form')][%s]//select[@name='%s']"),
        "add_incident": (By.XPATH, "//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]//div[contains(@class,'driver-form')]["
                                   "%s]//button[text()='%s']"),
        "select_second_incident": (By.XPATH, "//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]//div[contains(@class,'driver-form')]["
                                             "%s]//div[contains(@class,'incident-div')]//select[@name='%s']"),
        "select_second_driver_second_incident": (By.XPATH, "//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]//div[contains(@class,"
                                                           "'driver-form')][%s]//div[contains(@class,'form-group incident-form')]//select["
                                                           "@name='%s']"),
        "post_button": (By.XPATH, "//a[@id='postButton' and contains(text(),'%s')]"),
        "request_result": (By.XPATH, "//pre[@id='request']//span"),
        "actual_request_result": (By.XPATH, "//pre[@id='%s']"),
        "redirect_button": (By.XPATH, "//a[@id='posturl' and contains(text(),'%s')]"),
        "complete_active_start_tab": (By.XPATH, "//div[@class='secondary-nav-item complete active']//span[text()='Start']"),
        "complete_start_tab": (By.XPATH, "//div[@class='secondary-nav-item complete']//span[text()='Start']"),
        "form_input_field": ("//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]//input"), # here!!! 7x
        "personal_information_form_fields_name": (By.XPATH, "(//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]/div[@class='%s'])["
                                                            "%s]//input | (//div[contains(@class,'section-sm')]/div[@class='%s'])[%s]//select"),
        "form_fields_name": (By.XPATH, "(//h4[text()='%s']/ancestor::div[contains(@class,'section-sm')]/div[@class='%s']/div[@class='form-group'])"
                                       "[%s]//input | (//div[contains(@class,'section-sm')]/div[@class='%s']/div[@class='form-group'])[%s]//select"),
        "personal_information_form_fields": (By.XPATH, "//h4[text()='Personal Information']/ancestor::div[contains(@class,'section-sm')]//div["
                                                       "@class='form-group']//input | //div[contains(@class,'section-sm')]/div["
                                                       "@class='form-group']//select"),
        "vehicle_nformation_form_fields": (By.XPATH, "//h4[text()='Vehicle Information']/ancestor::div[contains(@class,'section-sm')]/div["
                                                     "@class='vehicle-form']/div[@class='form-group']//input | //div[contains(@class,"
                                                     "'section-sm')]/div[@class='vehicle-form']/div[@class='form-group']//select"),
        "driver_information_form_fields": (By.XPATH, "//h4[text()='Driver Information']/ancestor::div[contains(@class,'section-sm')]/div["
                                                     "@class='driver-form primaryDriver']/div[@class='form-group']//input | //div[contains(@class,"
                                                     "'section-sm')]/div[@class='driver-form primaryDriver']/div[@class='form-group']//select"),

    }


def modify_custom_xpath_locator(locator, *values):
    xpath = locator[1] #[1]
    xpath = xpath % (values)
    return xpath


def wait_until_element_contains_value(locator, text_value, driver, parent_element=None):
    if parent_element is None:
        element = driver.find_element_by_xpath(locator)
        try:
            WebDriverWait(driver, 10, 0.5, Exception).until(
                lambda driver: element.get_attribute("value") == text_value)
        except TimeoutException:
            assert False, "Element '%s' does not contain value '%s'. Actual value: '%s'" % (
                locator[1], text_value, element.get_attribute("value"))
    else:
        element = parent_element.find_element(*locator)
        try:
            WebDriverWait(driver, 10, 0.5, Exception).until(
                lambda driver: element.get_attribute("value") == text_value)
        except TimeoutException:
            assert False, "Element '%s' does not contain value '%s'. Actual value: '%s'" % (
                locator[1], text_value, element.get_attribute("value"))


def select_by_visible_text(locator, option_text, driver, parent_element, with_wait_for_selection):
    try:
        if parent_element is None:
            self.wait_for_element_become_clickable(locator)
            element = Select(self.driver.find_element(*locator))
        else:
            element = Select(parent_element.find_element(*locator))

        element.select_by_visible_text(option_text)

        if (parent_element is None and with_wait_for_selection):
            self.wait_for_option_to_be_selected(locator, option_text)
        return True
    except Exception:
        return False


def enter_form_field(field, value, form, driver):
    elementXpath = modify_custom_xpath_locator(prepopLocators["form_field"], form, field)
    wait_for_element_to_load_and_click_on_element(elementXpath, driver)
    wait_for_element_to_load_and_enter_text_into_element(elementXpath, value, driver)
    wait_until_element_contains_value(elementXpath, value, driver)


def select_form_option(form, fields, text, driver):
    elementXpath = modify_custom_xpath_locator(prepopLocators["select_form_field"], form, fields)
    # print(elementXpath)
    newElem = elementXpath + '/option[text()=' + "'" + text + "'" + ']'
    driver.find_element_by_xpath(newElem).click()


def click_prepop_button(button, driver):
    if button == "Post":
        postXpath = modify_custom_xpath_locator(prepopLocators["post_button"], button)
        wait_for_element_to_load_and_click_on_element(postXpath, driver)
        assert is_visible_with_wait(prepopLocators["request_result"], driver) == True, "Request Result not displayed"
    if button == "Redirect":
        postXpath = modify_custom_xpath_locator(prepopLocators["redirect_button"], button)
        wait_for_element_to_load_and_click_on_element(postXpath, driver)
        assert is_visible_with_wait(prepopLocators["request_result"], driver) == True, "Request Result not displayed"


def is_visible_with_wait(xpath, driver, timeout=60):
    return WebDriverWait(driver, timeout, 0.5, StaleElementReferenceException).until(lambda driver: driver.find_element(*xpath).is_displayed())


def post_to_API_and_return_link(context, payload, link, headers):
    context.response = requests.request("POST", link, data=payload, headers=headers)
    json1 = context.response.text
    json1_data = json.loads(json1)
    return json1_data.get('location')


def post_to_API_and_return_response_json(payload, link, headers):
    response = requests.request("POST", link, data=payload, headers=headers)
    json_data = json.loads(response.text)
    return json_data


def wait_element_present_and_find(driver, xpath, base_element=None):
    cur_time = int(round(time.time() * 1000))
    end_time = cur_time + 60 * 1000
    if base_element is None:
        base = driver
    else:
        base = base_element
    while cur_time < end_time:
        try:
            return Element(driver, driver.find_element_by_xpath(xpath))
        except:
            time.sleep(0.1)
            cur_time = int(round(time.time() * 1000))
    raise ElementNotFoundException("Element was not found using strategy"
                                   " [%s] with locator \"%s\"" % (xpath, driver))


def cookie_data_validation(zebra_cookie, desired_source, desired_medium, desired_channel_id):
    source_value = ''
    medium_value = ''
    channel_id_value = ''

    for item in zebra_cookie:
        if item.get('name') == 'source':
            source_value = item.get('value')
        if item.get('name') == 'medium':
            medium_value = item.get('value')
        if item.get('name') == 'channel_id':
            channel_id_value = item.get('value')

    assert source_value == desired_source
    assert medium_value == desired_medium
    assert channel_id_value == desired_channel_id


def click_button_that_contains_passed_in_text(text_input, driver):
    xpath = "//*[contains(text(), '" + text_input + "')]"
    driver.find_element_by_xpath(xpath).click()


def get_dob_midnight_from_age(age):
    time = datetime.now()
    dob = time - relativedelta(years=age, days=1)
    dob_midnight = datetime(dob.year, dob.month, dob.day)
    return dob_midnight


logger = logging.getLogger(__name__)


def remove_report_folder(path, context):
    if "parallel" not in context.config.userdata and os.path.exists(path):
        shutil.rmtree(path)
        logger.info("Remove '{}' folder".format(path))


def assert_status_code(api_name, status_code):
    assert status_code == 200 or status_code == 201, 'The ' + api_name + ' returned a ' + str(status_code)


def return_quote_id(session_id, context):
    url = context.prefix + ".thezebra.com/api/v3/users/quote/current"
    user_cookie = {'sessionid' : str(session_id)}
    try:
        response = requests.request("GET", url, cookies=user_cookie)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        sys.exit(1)
    quote_id = json.loads(response.text).get('id')
    return quote_id
