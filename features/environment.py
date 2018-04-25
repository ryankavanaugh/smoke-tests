from selenium import webdriver
import requests
import datetime
import json
from allure_commons.types import AttachmentType
from allure_commons._allure import attach
from functions_and_variables.functions import create_zebra_link, create_prepop_link, return_environment_prefix, create_prepop_api_link, create_drift_api_link, remove_report_folder, return_quote_id
import os
# import sys
import glob

username = "rkavanaugh@thezebra.com"  # change this to the username associated with your account
authkey = "u4e33377b1a94e4a"  # change this the authkey found on the 'Manage Account' section of our site

test_environment = os.environ["TESTING_ENVIRONMENT"]

def before_all(context):
    print('\n' + 'Browser: ' + os.environ["BROWSER"] + '\n')

    context.test_environment = test_environment

    environment_prefix = return_environment_prefix(test_environment)
    context.prefix = environment_prefix
    context.zebra_url = create_zebra_link(environment_prefix)
    context.prepop_link = create_prepop_link(environment_prefix)
    context.prepop_api_link = create_prepop_api_link(environment_prefix)
    context.drift_api_link = create_drift_api_link(environment_prefix)

    # # Remove all previous files from the past report
    # folder = glob.glob('reports/')
    # directory = "reports/"
    # folder = os.listdir(directory)
    # for file in folder:
    #     if file.endswith(".json"):
    #         os.remove(os.path.join(directory, file))
    #         # os.remove(file)


def before_feature(context, feature):
    if "skip" in feature.tags:
        feature.skip("Marked with @skip")
        # return

    browser = os.environ["BROWSER"]
    context.session_driver = browser

    caps = {}
    caps['name'] = 'The Zebra QA Automation Test: ' + browser
    caps['build'] = ''
    # caps['browserName'] = "Chrome"  # pulls the latest version of Chrome by default
    caps['platform'] = "Mac OSX 10.12"  # to specify a version, add caps['version'] = "desired version"
    caps['screen_resolution'] = '1366x768'
    caps['record_video'] = 'true'
    caps['record_network'] = 'true'
    caps['take_snapshot'] = 'true'

    mobile_caps = {}
    mobile_caps['browserName'] = 'Safari'
    mobile_caps['deviceName'] = 'iPad Pro Simulator'
    mobile_caps['platformVersion'] = '9.3'
    mobile_caps['platformName'] = 'iOS'
    mobile_caps['deviceOrientation'] = 'landscape'
    mobile_caps['record_video'] = 'true'
    mobile_caps['record_network'] = 'true'
    mobile_caps['take_snapshot'] = 'true'

    context.api_session = requests.Session()
    context.api_session.auth = (username, authkey)

    if browser == 'mobile':
        context.driver = webdriver.Remote(
            desired_capabilities=mobile_caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (username, authkey)
        )

    if browser == 'chrome':
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()

    if browser == 'firefox':
        context.driver = webdriver.Firefox()

    if browser == 'cbt-chrome':
        caps['browserName'] = "Chrome"
        context.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (username, authkey)
        )

    if browser == 'cbt-safari':
        caps['browserName'] = "Safari"
        context.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (username, authkey)
        )

    if browser == 'cbt-firefox':
        caps['browserName'] = "Firefox"
        context.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (username, authkey)
        )

    if browser == 'cbt-ie':
        caps['browserName'] = "Internet Explorer"
        caps['platform'] = "Windows 10"
        context.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (username, authkey)
        )

    if browser == 'docker-chrome':
        context.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.CHROME.copy())

    context.user_funnel_info = {}


def after_feature(context, feature):
    # print('\n' + 'Test ran with: ' + context.session_driver)
    if os.environ["BROWSER"] != 'docker-chrome':
        context.driver.quit()


def after_all(context):
    pass
    # attach(os.environ["TESTING_ENVIRONMENT"], )


def after_step(context, step):

    if step.status == 'failed':
        # Save session ID and quote ID
        zebra_cookie = context.driver.get_cookies()
        for item in zebra_cookie:
            if item.get('name') == 'sessionid':
                session_id = item.get('value')
                quote_id = return_quote_id(session_id, context)
                session_id_and_quote_id = 'Session ID: ' + session_id + '\n\n' + 'Quote ID: ' + quote_id

                attach(
                    session_id_and_quote_id,
                    name='Session ID and Quote ID',
                    attachment_type='text/plain'
                )

        # Save console logs
        string_of_logs = 'CONSOLE lOG' + '\n\n'
        for entry in context.driver.get_log('browser'):
            human_readable_time_stamp = datetime.datetime.fromtimestamp(entry['timestamp']/1000.0).strftime('%Y-%m-%d %H:%M:%S')
            timestamp = 'Timestamp: ' + str(human_readable_time_stamp)
            error_message = 'Error Message: ' + entry['message']
            string_of_logs = string_of_logs + timestamp + '\n' + error_message + '\n\n'
        attach(
            str(string_of_logs),
            name='Console Log',
            attachment_type='text/plain'
        )

        # Save screenshot
        attach(
            context.driver.get_screenshot_as_png(),
            name='{}'.format(step.name.encode('utf-8').strip()),
            attachment_type=AttachmentType.PNG
        )

























# attach(name='{}: {}'.format(context.scenario.name, step.name.encode('utf-8').strip(), context.session_id))



# def step_status(context, step):
#     context.test_name = context.scenario.name
#     step_name = re.sub('[^A-Za-z0-9]+', '_', step.name)
#
#     if step.status == 'failed':
#         report_dir = Logger.create_test_folder(context.scenario.name)
#         _screenshot = os.path.join(report_dir, '{}__Fail.png'.format(step_name))
#         try:
#             save_report_screenshot(context=context, step_name=step_name, screenshot=_screenshot)
#             time.sleep(5)
#             # attach_report_screenshot(context=context, step=step, screenshot=_screenshot)
#         except Exception as e:
#             print ('Failed to save or attach report: {}', e)
#         finally:
#             # context.allure.stop_step(Status.FAILED)
#             context.last_traceback = step.error_message
#             try:
#                 context.last_error_message = step.error_message.split('ERROR:')[1]
#             except IndexError:
#                 context.last_error_message = step.error_message

# def save_report_screenshot(context, step_name, screenshot):
#     try:
#         context.driver.save_screenshot(screenshot)
#     except Exception as e:
#         print ('Failed to take screenshot to: {}. \n{}'.format(conf.config['logs'], e))
#         print ('Screenshot name: {}'.format(step_name))

# def attach_report_screenshot(context, step, screenshot):
#     try:
#         with open(screenshot, 'rb') as _file:
#             allure.attach(_file.read(), name='{}_{}'.format(context.test_name, step.name.encode('utf-8').strip()), attachment_type=allure.attachment_type.PNG)
#             # context.allure.attach('{}_{}'.format(context.test_name, step.name.encode('utf-8').strip()), _file.read(), attachment_type=allure.attachment_type.PNG)
#
#     except Exception as e:
#         print ('Failed to attach to report screenshot: {}. \nError: {}\n'.format(screenshot, e))