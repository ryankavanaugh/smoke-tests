# Created by ryankavanaugh at 3/22/18
@all
@multidriver

Feature: This smoke test runs end to end through the funnel and creates/deletes multiple drivers/vehicles

  Scenario: Walk through funnel, enter basic info, and mulitple vehicles
    Given we navigate to the Zebra
    When we enter "zip code" "78704" and click submit
    When we select "Yes, I have insurance" on the Start page

    # Car 1
    When we enter "2016" for car "year"
    And we enter "Honda" for car "make"
    And we enter "Fit" for car "model"
    And we enter "Ex4drHatchback6m" for car "style"
    Then we click the "vehicle's save & continue" button
    Then we enter "paid in full" for "ownership status"
    And we enter "pleasure" for "primary use"
    And we enter "very low" for "mileage"
    And we enter the street address is "1"
    Then we click the "vehicle's save & continue" button
    Then we click the "add vehicle" button

    # Car 2
    When we enter "1987" for car "year"
    And we enter "Honda" for car "make"
    And we enter "Accord" for car "model"
    And we enter "Lx4drSedan" for car "style"
    Then we click the "additional vehicle save & continue" button
    Then we enter "paid in full" for "ownership status"
    And we enter "business" for "primary use"
    And we enter "average" for "mileage"
    Then we click the "additional vehicle save & continue" button
    Then we click the "vehicle's final save & continue" button

    # Driver 1
    Then we enter "Jim" in the "first name" field
    And we enter "Halpert" in the "last name" field
    And we enter "10121987" in the "birthdate" field
    And we enter "abc@thezebra.com" in the "email" field
    And we enter "(888) 888-8888" in the "phone" field
    And we enter "male" for "gender"
    Then we click the "driver's save & continue" button

    Then we enter "married" for "relationship"
    And we enter "excellent credit" for "credit score"
    And we enter "doctoral degree" for "education"
    And we enter "own home" for "living status"
    And we enter "more than 3 years" for "Length of Insurance"
    And we enter "AAA" as the current insurance provider
    And we enter "no" for "tickets and claims"
    Then we click the "driver's save & continue" button
    Then we click the "add driver" button

    # Driver 2
    Then we enter "Pam" in the "first name" field
    And we enter "Halpert" in the "last name" field
    And we enter "05051986" in the "birthdate" field
    And we enter "female" for "gender"
    Then we enter "married" for "relationship"
    Then we click the "additional driver save & continue" button
    Then we click the "driver's final save & continue" button

    # Discounts page
    Then we enter "currently employed" on the "Are you currently employed full time?" question
    And we enter "not on active duty" on the "Are you active duty military or a veteran?" question
    And we enter "pay in full" on the "Do you plan to pay in full at the start of your policy?" question
    And we enter "set up auto-pay" on the "Do you want to set up auto-pay from your bank account?" question
    And we enter "go paperless" on the "Do you want to go paperless?" question
    Then we click the "discounts save & continue" button
    Then we click the "discounts final save & continue" button

    # Remove the second vehicle
    Then we click the "edit vehicles" button
    Then we click the "remove second vehicle" button
    Then we click the "vehicle's final save & continue" button
    Then we click the "edit drivers" button
    Then we click the "remove second driver" button
    Then we click the "driver's final save & continue" button

    # Summary page
    Then we click the "show my quotes" button
    Then we assert there are "class" "carrier-info" objects on the page
    Then we have verified that we were able to create multiple drivers and vehicles and delete a driver and a vehicle successfully