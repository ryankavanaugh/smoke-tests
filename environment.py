from selenium import webdriver
import requests
import datetime
import json
from allure_commons.types import AttachmentType
from allure_commons._allure import attach
import os
import glob
from features.mobile_functions.functions import return_environment_prefix, create_zebra_link, return_quote_id

username = "rkavanaugh@thezebra.com"  # change this to the username associated with your account
authkey = "u4e33377b1a94e4a"  # change this the authkey found on the 'Manage Account' section of our site

test_environment = os.environ["TESTING_ENVIRONMENT"]



def before_all(context):
    context.device = os.environ["DEVICE"]
    context.test_environment = test_environment
    environment_prefix = return_environment_prefix(test_environment)
    context.prefix = environment_prefix
    context.zebra_url = create_zebra_link(environment_prefix)

    # Remove all previous files from the past report
    folder = glob.glob('reports/')
    directory = "reports/"
    folder = os.listdir(directory)
    for file in folder:
        if file.endswith(".json"):
            os.remove(os.path.join(directory, file))
        if file.endswith(".attach"):
            os.remove(os.path.join(directory, file))
            # os.remove(file)


def before_feature(context, feature):
    if "skip" in feature.tags:
        feature.skip("Marked with @skip")

    mobile_caps = {}
    mobile_caps['browserName'] = 'Safari'
    mobile_caps['deviceName'] = 'iPad Pro Simulator'
    mobile_caps['platformVersion'] = '9.3'
    mobile_caps['platformName'] = 'iOS'
    mobile_caps['deviceOrientation'] = 'landscape'
    mobile_caps['record_video'] = 'true'
    mobile_caps['record_network'] = 'true'
    mobile_caps['take_snapshot'] = 'true'

    caps = {}
    caps['browserName'] = 'Chrome'
    caps['deviceName'] = 'Nexus 9'
    caps['platformVersion'] = '6.0'
    caps['platformName'] = 'Android'
    caps['deviceOrientation'] = 'portrait'

    context.api_session = requests.Session()
    context.api_session.auth = (username, authkey)

    if context.device == 'cbt':
        context.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (username, authkey)
        )

    # if browser == 'cbt-chrome':
    #     caps['browserName'] = "Chrome"
    #     context.driver = webdriver.Remote(
    #         desired_capabilities=caps,
    #         command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (username, authkey)
    #     )


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

        # context.driver.save_screenshot('heredude.png')

        # # Save screenshot
        # attach(
        #     context.driver.get_screenshot_as_base64(),
        #     name='{}'.format(step.name.encode('utf-8').strip()),
        #     attachment_type=AttachmentType.JPG
        # )

























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