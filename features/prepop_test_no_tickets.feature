# Created by ryankavanaugh at 3/12/18
@all
@frontend
@iz2
@prepop

Feature: Test with Prepop API with a single driver that does not include tickets and confirms the Prepop info bridges over to the funnel

  Scenario: Test with Prepop API with a single driver that does not include tickets and confirms the Prepop info bridges over to the funnel
    Given we post "Jesse Durante Json" to the Prepop API
    Then we navigate to the API response link

#  Scenario: Verify that the Prepop data correctly moved into the Driver's Page # 1
    Then we check that "Jesse" has populated the "first_name" field
    Then we check that "Durante" has populated the "last_name" field
    Then we check that "08/17/1990" has populated the "date_of_birth" field
    Then we check that "xyz@thezebra.com" has populated the "email" field
    Then we check that "8888888888" has populated the "phone" field
    Then we check that the gender button has been selected correctly as "Female"
    Then we click the "driver's save & continue" button

#  Scenario: Verify that the Prepop data correctly moved into the Driver's Page # 2
    Then we check that the "marital_status" section has been selected with the "Single" button
    Then we check that the "credit_score" section has been selected with the "Excellent (720+)" button
    Then we check that the "education" section has been selected with the "Bachelor's Degree" button
    Then we check that the "residence_ownership" section has been selected with the "Own condo" button
    Then we check that the "insured_length" section has been selected with the "1 to 3 years" button
    Then we check that the "current_carrier" dropdown has been selected with "AAA"
    And we enter "no" for "tickets and claims"
    Then we check that the "violations" section has been selected with the "No" button
    Then we click the "driver's save & continue" button
    Then we click the "driver's final save & continue" button

#  Scenario: Go through the Discounts page (Prepop)

    Then we enter "currently employed" on the "Are you currently employed full time?" question
    And we enter "not on active duty" on the "Are you active duty military or a veteran?" question
    And we enter "pay in full" on the "Do you plan to pay in full at the start of your policy?" question
    And we enter "set up auto-pay" on the "Do you want to set up auto-pay from your bank account?" question
    And we enter "go paperless" on the "Do you want to go paperless?" question
    Then we click the "discounts save & continue" button
    Then we click the "discounts final save & continue" button
    Then we click the "show my quotes" button
    Then we assert there are "class" "carrier-info" objects on the page
    Then we have verified that we see the proper prepop data in the funnel and we can see rates on the rates select page at the end of the funnel