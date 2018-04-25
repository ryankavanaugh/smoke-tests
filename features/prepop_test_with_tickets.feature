# Created by ryankavanaugh at 4/25/18
@prepop
@tickets

Feature: Test with Prepop API with a single driver that includes tickets and confirms the Prepop info bridges over to the funnel

  Scenario: Test with Prepop API with a single driver that does not include tickets and confirms the Prepop info bridges over to the funnel
    Given we post "Laura Johnson Json" to the Prepop API
    Then we navigate to the API response link
    Then we go to the drivers primary page

  #  Scenario: Verify the Prepop data correctly moved into the funnel starting with the Start page
    Then we check "No, I don't" has populated the "insurance" section
('we check that "{}" has been selected with the "{}" button')