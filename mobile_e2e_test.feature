# Created by ryankavanaugh at 4/20/18
Feature: End to end test for Mobile Healthcheck

  Scenario: Mobile end to end healthcheck
    Given I navigate to the zebra on mobile
    Then I enter zip code "97210"
    Then I enter "2017" as the car "year"
    Then I enter "Audi" as the car "make"
    Then I enter "A4" as the car "model"
    Then I enter "2.0T Premium 4dr Sedan" as the car "body type"
    Then I click continue

    Then we select "low miles" for "mileage"
    Then we select the "male" button for "gender"
    Then we enter "05/22/1980" for "birthday"
    Then we click the "birthday button"

    Then we select "uninsured" for "insured"
    Then we enter "Elton" for "first name"
    Then we enter "Redfields" for "last name"
    Then we click the "name button"

    Then we select the "good credit" button for "credit"
    Then we select "bachelors" for "education"
    Then we select the "own a home" button for "home ownership"
    Then we enter "2267 NW Glisan Street" for "address"
    Then we click the continue button on the address page
    Then we select "minimum" for "coverage"
    Then we select the "married" button for "relationship status"
    Then we select the "no additional drivers" button for "drivers"
    Then we select the "no additional vehicles" button for "vehicles"
    Then we select the "no tickets" button for "tickets"

    Then we enter "8888888888" for "phone number"
    Then we enter "abc@thezebra.com" for "email"
    Then we click the "get quotes button"
#    Then we click the get quotes button
    Then we verify rates are on the page