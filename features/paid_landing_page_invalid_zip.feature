# Created by ryankavanaugh at 3/23/18
@all
@frontend
@zfront
@plinvalid

Feature: Verifying an invalid zip code cannot be entered on paid landing page

  Scenario: Verifying an invalid zip code cannot be entered on paid landing page
    Given we navigate to the Zebra paid landing page
    Then we click the button that contains the text "Compare Now"
    Then we assert that a valid "zipcode" is required to move onto the funnel
    Then we enter "78706" in the "zipcode" landing page field
    Then we click submit on the "zipcode" field
    Then we assert that a valid "zipcode" is required to move onto the funnel
    Then we clear the "zipcode" field
    Then we enter "78704" in the "zipcode" landing page field
    Then we click submit on the "zipcode" field
    Then we switch to the current tab
    Then we assert "Yes, I have insurance" is on the page
    Then we have verified a correct zip code is required to move onto the funnel from the paid landing page
