from behave import *
from venv.features.functions_and_variables.variables import drift_api_payload_1, drift_api_payload_2, drift_api_headers
from venv.features.functions_and_variables.functions import post_to_API_and_return_response_json


@given('we post single and multiple driver payloads to the Drift API')
def step(context):
    # get the responses from drift with our payloads
    drift_payloads = [drift_api_payload_1, drift_api_payload_2]
    context.all_drift_json_responses = []
    for drift_payload in drift_payloads:
        context.all_drift_json_responses.append(post_to_API_and_return_response_json(drift_payload, context.drift_api_link, drift_api_headers))


@then('we will receive and perform data validation on the reponses')
def step(context):
    # Verify that the payment plans are populated and have the correct kinds of data
    carrier_tracker = 0

    for response_json_data in context.all_drift_json_responses:
        offered_carriers = response_json_data['offeredCarriers']

        for carrier in offered_carriers:
            offered_products = carrier['offeredProducts']

            for offered_product in offered_products:
                payment_plan_data = offered_product['paymentPlanInformation']['paymentPlans']

                # print('Offered Carrier ' + str(carrier_tracker + 1) + '. Number of payment plans: ' + str(len(payment_plan_data)))

                for payment_plan in payment_plan_data:
                    plan_id = payment_plan['planId']
                    term_amount = payment_plan['fullTermAmount']
                    installment_amount = payment_plan['installmentAmount']
                    installments = payment_plan['installments']
                    down_payment = payment_plan['downPayment']
                    plan_type = payment_plan['planType']
                    policy_term = payment_plan['policyTerm']
                    full_term_amount = payment_plan['fullTermAmount']
                    # print(full_term_amount)

                    # print(str(plan_id) + ' ' + str(plan_type))

                    if full_term_amount > 0:
                        # Verify data in payment plans
                        assert full_term_amount > 0, plan_type + ' has an incorrect full term amount: ' + str(full_term_amount)
                        assert plan_id > 0, plan_type + ' has an incorrect plan ID: ' + str(plan_id)
                        assert type(plan_type) == unicode, 'Plan type is not a string'
                        assert len(plan_type) > 0, 'There is no plan type'
                        assert type(policy_term) == unicode, 'Policy term is not a string'
                        assert len(policy_term) > 0, 'There is no plan type'

                        if (plan_type) == "PAID_IN_FULL":
                            # Add in fulltermamount
                            pass
                        elif (plan_type) == "TWO_PAY":
                            assert down_payment > 0, plan_type + ' has an incorrect downpayment: ' + str(down_payment)
                            assert term_amount > 0, plan_type + ' has an incorrect term amount: ' + str(term_amount)
                            assert installments > 0, plan_type + ' has an incorrect installment number'
                        else:
                            assert down_payment > 0, plan_type + ' has an incorrect downpayment: ' + str(down_payment)
                            assert term_amount > 0, plan_type + ' has an incorrect term amount: ' + str(term_amount)
                            assert installments > 0, plan_type + ' has an incorrect installment number'
                            assert installment_amount > 0, 'The installment amount is incorrect: ' + str(installment_amout)
            carrier_tracker += 1