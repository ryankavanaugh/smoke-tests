# Created by ryankavanaugh at 3/5/18
@all
@frontend
@firefox
@e2e

Feature: End to end test for the entire application that verifies rates's are present at the end
  Scenario: End to end test for the entire application that verifies rates's are present at the end
    Given we navigate to the Zebra
    When we enter "zip code" "97210" and click submit
    When we select "Yes, I have insurance" on the Start page

#  Scenario: A2 Go through section one of the Vehicles page
    When we enter "2015" for car "year"
    And we enter "Acura" for car "make"
    And we enter "Ilx" for car "model"
    And we enter "2.0l4drSedan" for car "style"
    Then we click the "vehicle's save & continue" button

#  Scenario: A3 Go through section two of the Vehicles page
    Then we enter "paid in full" for "ownership status"
    And we enter "personal/commuting" for "primary use"
    And we enter "low" for "mileage"
    And we enter the street address is "105-135 Southeast Hawthorne Boulevard"
    Then we click the "vehicle's save & continue" button
    Then we click the "vehicle's final save & continue" button

#  Scenario: A4 Go through the Driver's page
    Then we enter "Jerry" in the "first name" field
    And we enter "Garcia" in the "last name" field
    And we enter "08161990" in the "birthdate" field
    And we enter "abc@thezebra.com" in the "email" field
    And we enter "(888) 888-8888" in the "phone" field
    And we enter "male" for "gender"
    Then we click the "driver's save & continue" button

#  Scenario: A5 Verify we can finish the Driver's page info
    Then we enter "single" for "relationship"
    And we enter "good credit" for "credit score"
    And we enter "bachelor's degree" for "education"
    And we enter "own home" for "living status"
    And we enter "6 to 12 months" for "Length of Insurance"
    And we enter "AAA" as the current insurance provider
    And we enter "no" for "tickets and claims"
    Then we click the "driver's save & continue" button
    Then we click the "driver's final save & continue" button
#    Then we check if the ethnio survey is open and close it if it is
#  Scenario: A6 Go through the Discounts page
    Then we enter "currently employed" on the "Are you currently employed full time?" question
    And we enter "not on active duty" on the "Are you active duty military or a veteran?" question
    And we enter "pay in full" on the "Do you plan to pay in full at the start of your policy?" question
    And we enter "set up auto-pay" on the "Do you want to set up auto-pay from your bank account?" question
    And we enter "go paperless" on the "Do you want to go paperless?" question
    Then we click the "discounts save & continue" button
    Then we click the "discounts final save & continue" button
    Then we click the "show my quotes" button
    Then we assert there are "class" "carrier-info" objects on the page
    Then verify rates are present and within the correct ranges
    Then we verify we can go through the entire funnel and get to the rates page

##  Scenario: Check admin panel to find new lead
#    Then we open up the admin panel
#    Then we login to the admin panel
#    Then we navigate to the admin core lead page
#    Then we print out the admin info
#    Then we verify the newly created lead showed up in admin via session id
