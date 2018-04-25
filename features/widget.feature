# Created by ryankavanaugh at 3/23/18
@all
#@ zfront
@widget

Feature: Verifying we can bridge from the widget to funnel and see rates at the end
    In this test we verify we can start at the widget
    and get to the funnel with the correct driver information
    being transfered to the funnel from the widget. Finally,
    we make sure that we can get to the end of the funnel
    and get rates.

  Scenario: Verifying we can bridge from the widget to funnel and see rates at the end
#    Given we navigate to "https://spiral-quiver.glitch.me/"
    Given we navigate to "https://13.onebox.thezebra.com/external_partner_test/"
    Then we enter "97210" into the "Zip Code" field
    Then we click "2017" in the "Vehicle Year"
    Then we click "Audi" in the "Vehicle Make"
    Then we click "A3" in the "Vehicle Model"
    Then we click the button that contains the text "Compare Now"
    Then we click the age button that contains the text "37-59"
    Then we select "no" for the "currently insured" section
    Then we select "yes" for the "homeowner" section
    Then we select "yes" for the "married" section
    Then we wait
    Then we click the button that contains the text "Compare More & Save"
    Then we switch to the current tab
    Then we sleep

    # Enter car info into the funnel
    Then we click the "Save & Continue" button
    Then we enter "paid in full" for "ownership status"
    And we enter "personal/commuting" for "primary use"
    And we enter "average" for "mileage"
    And we enter the street address is "105-135 Southeast Hawthorne Boulevard"
    Then we click the "Save & Continue" button
    Then we click the "Save & Continue " button

    # Driver Info Page 1
    Then we enter "Terry" in the "first_name" field
    And we enter "Kinderson" in the "last_name" field
    And verify dob info
    And we enter "abc@thezebra.com" in the "email" field
    And we enter "(888) 888-8888" in the "phone" field
    And we enter "male" for "gender"
    Then we click the "Save & Continue" button

    # Driver Info Page 2 / Verify Widget Info carried over properly
    Then we check that the "marital_status" section has been selected with the "Married" button
    And we enter "good credit" for "credit score"
    And we enter "no diploma" for "education"
    And we check that the "residence_ownership" section has been selected with the "Own home" button
#    And we select "No" for the "Number of Tickets" field
#    Then we click the "Save & Continue" button
#    Then we click the "Save & Continue " button

#    # Go through the discounts page
#    Then we click "Yes" on the "Are you currently employed full time?" question
#    And we click "No" on the "Are you active duty military or a veteran?" question
#    And we click "Yes" on the "Do you plan to pay in full at the start of your policy?" question
#    And we click "Yes" on the "Do you want to set up auto-pay from your bank account?" question
#    And we click "Yes" on the "Do you want to go paperless?" question
#    Then we click the "Save & Continue" button
#    Then we click the "Save & Continue " button
#    Then we click the "Show My Quotes" button
#    Then we assert there are "class" "carrier-info" objects on the page
#    Then we verified we can go through the entire funnel and get to the rates page from the widget

