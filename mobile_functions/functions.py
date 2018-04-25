import time
import requests
import json
import sys
import logging
import urllib
import urllib2
import lxml.html
from selenium.webdriver.common.by import By
from features.mobile.mobile_pages.page.rate_page_mobile import RatePageMobile
from lib.utils.core.element_action import *
from lib.utils.core.js_executors import JSExecutors
from lib.utils.exceptions import WrongStepParameter, ElementNotFoundException
from features.mobile.mobile_pages.base_page_mobile import BasePageMobile
from lib.utils.core.element_action import ElementAction
from lib.utils.core.js_executors import JSExecutors


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


locators = {
    "headline_title": (By.XPATH, "//h1[@class='headline-title' and text()='Insurance in black & white']"),
    "zip_code": (By.XPATH, "//*[@id='zipcode-form-control']"),
    "start_button": (By.XPATH, "//button[@type='submit']"),
    "phone_button": (By.XPATH, "//div[@class='header-overlay-phone']/a[@class='btn btn-sm btn-primary']"),
    "header_menu_icon": (By.XPATH, "//div[@class='header-overlay-burger']"),
    "header_brand": (By.XPATH, "//div[@role='banner']//a[@class='header-overlay-brand']//*[@id='thezebra-blue']"),
    "homepage_title": (By.XPATH, "//div[@class='homepage-hero']//h1[@class='headline-title']"),
    "homepage_subtitle": (By.XPATH, "//div[@class='homepage-hero']//h5[@class='headline-subtitle']"),
    "start_button_by_text": (By.XPATH, "//div[@class='homepage-hero']//div[@class='zipcode-input']//button[@type='submit' and contains(text(),'%s')]"),
    "page_section": (By.XPATH, "//section[@class='tab-section section-md']//h3[text()=\"%s\"]"),
    "footer_section":
    (By.XPATH, "//section[contains(@class,'content-footer section-sm')]//h5[contains(text(),\"%s\")]"),
    "footer_headline": (By.XPATH, "//*[contains(@class,'footer')]/ancestor::div//* [text()='%s']"),
    "footer_nav_links": (
    By.XPATH, "//div[@class='row footer-navs']//ul[@class='list-unstyled footer-links inline']//a[text()='%s']"),
    "follow_us": (By.XPATH,
                  "//div[@class='row footer-navs']//p[@class='preamble' and text()='%s']/ancestor::nav//span[@class='anchor-text' and "
                  "text()='The Zebra on %s']/ancestor::a"),
    "footer_bottom": (By.XPATH, "//div[contains(@class,'footer-bottom')]"),
    "navigation_menu": (By.XPATH, "//nav[@class='overlay-nav']"),
    "nav_section": (By.XPATH, "//div[@class='overlay-nav-item']/a[@class='overlay-nav-headline' and text()='%s']"),
    "nav_section_phone_number": (
    By.XPATH, "//div[@class='overlay-nav-item']/a[@class='overlay-nav-headline overlay-phone']/span[text()='%s']"),
    "nav_section_and_nav_item": (By.XPATH,
                                 "//a[@class='overlay-nav-headline' and text()='%s']/ancestor::div[@class='overlay-nav-item']//li/a[text()='%s']"),
    "header_cta_start_button": (
    By.XPATH, "//div[@class='header-overlay-cta']/div[@class='header-overlay-button']/a[text()='Start']"),
    "header_menu_close_icon": (By.XPATH, "//body[@class='show-overlay']//div[@class='header-overlay-burger']"),
    "page_title": (By.XPATH, "//div[contains(@class,'container')]//h1"),
    "header": (By.XPATH, "//div[contains(@class,'header-overlay header-white ') and @role='banner']"),
    "footer": (By.XPATH, "//footer[@role='contentinfo']"),
    "content_footer": (By.XPATH, "//section[@class='content-footer section-sm']"),
    "insurability_score_header": (By.XPATH, "//header[@class='header']"),
    "insurability_score_footer": (By.XPATH, "//footer[@class='footer']"),
    "state": (By.XPATH,
              "//div[contains(@class,'jumbotron-sm state-index-hero')]//*[local-name()='svg']//*[local-name()='a'][*|href]"),
}


def get_element_when_displayed_and_enabled_ios(locator, driver):
    try:
        element = driver.find_element(*locator)
        if element.is_displayed() and element.is_enabled() and \
                element.location["x"] in range(0, JSExecutors.get_screen_web_view_width(driver, True)):
            return element
        else:
            return False
    except StaleElementReferenceException:
        return False


def wait_for_element_become_clickable(locator, driver, timeout=60):
    try:
        if "platformName" in driver.desired_capabilities and \
                driver.desired_capabilities["platformName"] == "iOS":
            return WebDriverWait(driver, timeout).until(
                lambda driver: get_element_when_displayed_and_enabled_ios(locator, driver))
        else:
            return WebDriverWait(driver, timeout, 0.5, WebDriverException).until(
                EC.element_to_be_clickable(locator))
    except TimeoutException:
        raise ElementNotFoundException("Element was not clickable using strategy "
                                       "[%s] with locator %s" % (locator[0], locator[1]))


def wait_element_present_and_find(locator, driver):
    if not type(locator) is tuple:
        raise TypeError("Incorrect type of locator, must be tuple")
    cur_time = int(round(time.time() * 1000))
    end_time = cur_time + 60 * 1000
    base = driver
    while cur_time < end_time:
        try:
            return Element(driver, base.find_element(locator[0], locator[1]))
            print(locator[1])
            return driver.find_element_by_xpath(locator[1])
        except:
            time.sleep(0.1)
            cur_time = int(round(time.time() * 1000))
    raise ElementNotFoundException("Element was not found using strategy"" [%s] with locator \"%s\"" % (locator[0], locator[1]))


def wait_for_element_to_load(xpath, text, driver):
    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element
        # element.clear()
        # element.send_keys(text)
    except:
        assert False, 'This element did not load properly: ' + xpath


def login_to_the_mobile_application_with_valid_data(zip_code, driver):
    wait_for_element_become_clickable(locators["zip_code"], driver)
    JSExecutors.wait_for_page_to_load(driver, 60)
    # wait_for_element_to_load("//*[@id='zipcode-form-control']", zip_code, driver).send_keys(zip_code, driver)
    wait_element_present_and_find(locators["zip_code"], driver).send_keys(zip_code, driver)
    wait_element_present_and_find(locators["start_button"], driver).click()


vehicle_info_locators = {
    "vehicle_insuring_header": (By.XPATH, "//h4[text()='Please select your primary vehicle:']"),
    "continue_button_vehicle_insuring": (By.XPATH, "//button[contains(@data-reactid,'Vehicle')]/span[text()='Continue']"),
    "vehicle_select": (By.XPATH, "//select[@name='vehicle']"),
    "make_select": (By.XPATH, "//select[@name='make']"),
    "model_select": (By.XPATH, "//select[@name='model']"),
}


def wait_for_option_to_be_selected(self, locator, option):
    WebDriverWait(self.driver, self._TIMEOUT).until(
        lambda driver: self.get_selected_option_from_selectbox(locator) == option)


def select_by_visible_text(locator, option_text, parent_element, driver, with_wait_for_selection):
    try:
        if parent_element is None:
            wait_for_element_become_clickable(locator)
            element = Select(driver.find_element(*locator))
        else:
            element = Select(parent_element.find_element(*locator))

        element.select_by_visible_text(option_text)

        if (parent_element is None and with_wait_for_selection):
            wait_for_option_to_be_selected(locator, option_text)
        return True
    except Exception:
        return False


def get_select_options(element):
    list_options = []
    drop_down = Select(element)
    for option in drop_down.options:
        list_options.append(option.text.replace(u'\xa0', u' '))
    return list_options


def select_option(locator, option_text, driver, parent_element=None, with_wait_for_selection=True, timeout=60):
    try:
        WebDriverWait(driver, timeout).until(
            lambda driver: select_by_visible_text(locator, option_text, parent_element, driver, with_wait_for_selection))
    except TimeoutException as e:
        logging.ERROR(
            "%s. Available options are: %s" % (e, get_select_options(driver.find_element(*locator))))
        raise


def select_vehicle_info(text, field, driver):
    JSExecutors.wait_for_page_to_load(driver, 60)
    wait_for_element_become_clickable(vehicle_info_locators["vehicle_select"], driver)
    # select_option(vehicle_info_locators["vehicle_select"], year, driver)
    if field == 'year':
        wait_for_element_become_clickable(vehicle_info_locators["vehicle_select"], driver)
        element = Select(driver.find_element(*vehicle_info_locators["vehicle_select"]))
        element.select_by_visible_text(text)
    if field == 'make':
        wait_for_element_become_clickable(vehicle_info_locators["make_select"], driver)
        element = Select(driver.find_element(*vehicle_info_locators["make_select"]))
        element.select_by_visible_text(text)
    if field == 'model':
        wait_for_element_become_clickable(vehicle_info_locators["model_select"], driver)
        element = Select(driver.find_element(*vehicle_info_locators["model_select"]))
        element.select_by_visible_text(text)
    if field == 'body type':
        dict = (By.XPATH, "//*[@name='submodel']")
        wait_for_element_become_clickable(dict, driver)
        element = Select(driver.find_element(*dict))
        element.select_by_visible_text(text)
    # select_option(vehicle_info_locators["model_select"], model, driver)
    # model = wait_element_present_and_find(vehicle_info_locators["model_select"], driver).element
    # JSExecutors.remove_focus(driver, model)




def click_continue_button_under_vehicle_insuring(driver, moved_to_next_step=True):
    locator = vehicle_info_locators["continue_button_vehicle_insuring"]
    wait_for_element_become_clickable(locator, driver)
    wait_element_present_and_find(locator, driver).click()
    if moved_to_next_step:
        wait_until_not_visible(locator, driver)


born_screen_locators = {
    "when_were_you_born": (By.XPATH, "//h4[text()='When were you born?']"),

    "birthday": (By.XPATH, "//input[@class='form-control birthday-text']"),
    "birthday_error": (By.XPATH, "//input[@class='form-control birthday-text']/.."),
    "continue_button_birthday": (By.XPATH, "//button[contains(@data-reactid,'Birthday')]"),
}


def wait_until_element_contains_value(locator, text_value, driver, parent_element=None):
    # phone number comes out as (xxx) xxx-xxxx in certain environments (e.g. device on CBT)
    if parent_element is None and locator[1] != "phone number":
        element = driver.find_element(*locator)
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


def wait_until_not_visible(how, driver, timeout=60):
    try:
        WebDriverWait(driver, timeout, 0.5, (StaleElementReferenceException, WebDriverException, AttributeError)).until_not(
            lambda driver: driver.find_element(*how).is_displayed())
    except NoSuchElementException:
        pass
    except TimeoutException:
        raise ElementNotFoundException(
            "Element \"%s\" is still visible on the screen after timeout \"%s\"" % (how[1], timeout))


insurance_locators = {
    "are_you_currently_insured": (By.XPATH, "//span[text()='Are you currently insured?']"),

    "insured_select": (By.XPATH, "//select[@name='insured']"),
    "modal_dialog_current_provider": (
        By.XPATH, "//div[@class='modal-dialog']//h5[text()='Select your current provider']"),
    "your_current_provider": (By.XPATH, "//span[text()='%s']"),
    "current_provider_modal_name": (By.XPATH, "//div[@class='carrier-item radio']//span[1]"),
}


def get_selected_option_from_selectbox(locator, driver):
    try:
        element = Select(driver.find_element(*locator))
        text = element.first_selected_option.text
        return text
    except StaleElementReferenceException:
        pass


def select_insured_years(insured, driver):
    element = wait_for_element_become_clickable(insurance_locators["insured_select"], driver)
    if get_selected_option_from_selectbox(insurance_locators["insured_select"], driver) != insured:
        select_option(insurance_locators["insured_select"], insured, driver, None, False)
        JSExecutors.remove_focus(driver, element)
    else:
        print ("Insured '%s' already selected. Step skipped" % insured)
        JSExecutors.change_event(driver, element)



# NAMES!!!

name_locators = {
    "lets_personalize_your_quote": (By.XPATH, "//h4[contains (., \"Let's personalize your quote\")]"),
    "first_name": (By.ID, "first_name"),
    "first_name_error": (By.XPATH, "//input[@id='first_name']/.."),
    "last_name": (By.ID, "last_name"),
    "last_name_error": (By.XPATH, "//input[@id='last_name']/.."),
    "continue_button_on_personalize_your_quote": (
        By.XPATH, "//button[contains(@data-reactid,'Name')]/span[text()='Continue']"),

    "carrier_ad_name": (By.XPATH, "//div[@class='estimate-row estimate-dropdown']//span[@class='carrier-name']"),
    "quote_button": (By.XPATH, "//div[@class='estimate-row estimate-dropdown']//a[@class='btn btn-sm btn-ad']"),
    "address_continue_button": (By.XPATH, "//*[@class='m-item user-card address m-active']//*[@class='btn btn-lg bg-grad btn-loader']")
}



def click_address_continue_button(driver, move_next_step=True):
    JSExecutors.scroll_top(driver)
    locator = name_locators["address_continue_button"]
    element = wait_for_element_become_clickable(locator, driver)
    wait_element_present_and_find(locator, driver).click()
    try:
        element.click()
    except:
        pass
    JSExecutors.scroll_top(driver)
    # This seems to solve the scroll problem
    if move_next_step:
        wait_until_not_visible(locator, driver)