# Created by ryankavanaugh at 3/23/18
@all
@frontend
@zfront
@paidlanding

Feature: Verifying a valid zip code is required on the paid landing page to proceed through the funnel

  Scenario: Verifying a valid zip code is required on the paid landing page to proceed through the funnel
    Given we navigate to the Zebra paid landing page
    Then we click the paid landing page button that contains the text "Compare Now"
    Then we enter "78704" in the "zipcode" landing page field
    Then we click submit on the "zipcode" field
    Then we switch to the current tab
    Then we assert "Yes, I have insurance" is on the page

