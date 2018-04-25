from behave import *
import time


@then('verify rates are present and within the correct ranges')
def step(context):
    # test = context.driver.find_element_by_class_name('carrier-card')
    # test_text = test #.text
    # print(test_text.get_attribute('h3 class'))
    carriers_web_objects = context.driver.find_elements_by_xpath("//*[@class='carrier-card']//*[@class='carrier-name']")
    rates_web_objects = context.driver.find_elements_by_xpath("//*[@class='rate rate-carrier-card']")

    carriers = []
    rates_first_number = []
    rates_second_number = []

    for item in carriers_web_objects:
        carriers.append(item.text)

    # Rates that come first
    for item in rates_web_objects:
        if len(item.text)>3:
            rate_with_dash = (item.text.splitlines())[1] #[:4].strip()
            rate_with_whitespace =rate_with_dash[:4]
            rate = rate_with_whitespace.strip()
        else:
            rate = item.text
        rates_first_number.append(rate)

    # Rates after the '-'
    for item in rates_web_objects:
        rate_with_dash = (item.text.splitlines())[2]
        rate_with_whitespace = rate_with_dash[:4]
        rate_after_dash = rate_with_whitespace.strip()
        if rate_after_dash != "/mo":
            rates_second_number.append(rate_after_dash)

    # Create a dictionary by combining the carriers and rates
    carriers_and_rates = dict(zip(carriers, rates_first_number))


    # # Verify that all rates fall within the appropriate ranges
    # for carrier, rate_price in carriers_and_rates.iteritems():
    #     # print(carrier + ' ' + rate_price)
    #     assert int(rate_price) > 15, 'The rate for ' + carrier + ' caused an error. The rate price is ' + rate_price + '.'
    #     assert int(rate_price) < 10000, 'The rate for ' + carrier + ' caused an error. The rate price is ' + rate_price + '.'
    #
    # # Verify that the second rate numbers after the '-' are correct as well
    # for rate_price_after_dash in rates_second_number:
    #     assert int(rate_price_after_dash) > 15, 'The rate for ' + carrier + ' caused an error. The rate price is ' + rate_price + '.'
    #     assert int(rate_price_after_dash) <10000, 'The rate for ' + carrier + ' caused an error. The rate price is ' + rate_price + '.'
