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
from venv.lib.utils.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import shutil
import logging
import os
from datetime import *
from selenium.webdriver.common.by import By
# from venv.lib.utils.core.element_action import ElementAction

#### ADMIN TESTING
class AdminLogin:
    def __init__(self):
        self.locators = {
            "login_field": "id_username",
            "password_field": "id_password",
            "login_button": "//div[@class='submit-row']/input[@class='btn btn-info']"
        }

    page_url = "/admin/login/?next=/admin/"


    def wait_for_element_to_load_and_enter_text_into_element(self, xpath, text, driver):
        try:
            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.clear()
            element.send_keys(text)
        except:
            assert False, 'This element did not load properly: ' + xpath


    def wait_for_element_to_load_and_click_on_element(self, xpath, driver):
        try:
            wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
        except:
            assert False, 'This element did not load properly: '


    def __insure_page_loaded(self):
        super(LoginPageAdmin, self)._insure_page_loaded(self.locators["login_ok_button"])
        self._check_page_url(self.page_url)

    def perform_login(self, login, password, driver):

        self.user_xpath = self.locators['login_field']
        user_name_xpath = "//*[@id='" + self.user_xpath + "']"

        self.pass_xpath = self.locators['password_field']
        last_name_xpath = "//*[@id='" + self.pass_xpath + "']"

        self.button_xpath = self.locators['login_button']

        self.wait_for_element_to_load_and_enter_text_into_element(user_name_xpath, login, driver)
        self.wait_for_element_to_load_and_enter_text_into_element(last_name_xpath, password, driver)
        self.wait_for_element_to_load_and_click_on_element(self.button_xpath, driver)


def compare_funnel_and_admin_data(context, parameter):
    error_message = 'The lead in admin does not match the lead from the funnel: '
    assert context.user_admin_info[parameter] == context.user_funnel_info[parameter], error_message + str(context.user_funnel_info[parameter]) + ' ' + str(context.user_admin_info[parameter])