from behave import *
import time
from venv.features.functions_and_variables.admin_functions import AdminLogin, compare_funnel_and_admin_data
from venv.lib.utils.core.element_action import ElementAction


@then('we open up the admin panel')
def step(context):
    context.driver.get('https://release.onebox.thezebra.com/admin/')


@then('we login to the admin panel')
def step(context):
    login = 'admin'
    password = 'cryRodVandOn'
    loginNow = AdminLogin()
    loginNow.perform_login(login, password, context.driver)


@then('we navigate to the admin core lead page')
def step(context):
    context.driver.get('https://release.onebox.thezebra.com/admin/core/lead/')


@then('we print out the admin info')
def step(context):
    context.jerry_number = context.driver.find_element_by_xpath("//td[@class='field-first_name' and contains(., 'Jerry')]/../td[3]")
    # print(context.jerry_number.text)
    context.driver.find_element_by_xpath("//td[@class='field-first_name' and contains(., 'Jerry')]/..//a").click()
    time.sleep(3)
    admin_session_id_element = context.driver.find_element_by_xpath("//*[@id='id_session_key']")
    admin_session_id = admin_session_id_element.get_attribute('value')

    context.user_admin_info = {}
    phone_number = context.driver.find_element_by_xpath("//*[@id='id_phone_no']").get_attribute('value')
    first_name = context.driver.find_element_by_xpath("//*[@id='id_first_name']").get_attribute('value')
    last_name = context.driver.find_element_by_xpath("//*[@id='id_last_name']").get_attribute('value')
    email = context.driver.find_element_by_xpath("//*[@id='id_email']").get_attribute('value')
    address = context.driver.find_element_by_xpath("//*[@id='id_address']").get_attribute('value')
    zipcode = context.driver.find_element_by_xpath("//*[@id='id_zipcode']").get_attribute('value')
    context.user_admin_info = {'session id': admin_session_id , 'phone' : phone_number, 'first name' : first_name, 'last name' : last_name, 'email' : email, 'address' : address, 'zipcode' : zipcode}


@then('we verify the newly created lead showed up in admin via session id')
def step(context):
    all_parameters = []
    all_parameters = ['session id', 'phone', 'first name', 'last name', 'email', 'address', 'zipcode']
    for parameter in all_parameters:
        compare_funnel_and_admin_data(context, parameter)

