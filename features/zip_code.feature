# Created by ryankavanaugh at 3/6/18
@all
@frontend
@zfront
@zip

Feature: Homepage zip code feature

  Scenario: Verifying a valid zip code is required on the home page to proceed to the funnel
    Given we navigate to the Zebra
    Then we enter "77777" into the zip code field
    Then we assert that a valid "zipcode" is required to move onto the funnel
    Then we clear the zipcode text
    When we enter "zip code" "97229" and click submit
    Then we will be on the "Start" page
    And we have verified that the zip code feature works properly by taking the user to the start page




