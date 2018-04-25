# Created by ryankavanaugh at 3/23/18
@zfront

Feature: Attribution test that verifies desired source, desired medium, and desired channel id in cookie info upon hitting the Start Page

  Scenario: Attribution test that verifies desired source, desired medium, and desired channel id in cookie info upon hitting the Start Page
    Given we navigate to the zebra attribution page
    Then we enter "78704" in the "zipcode" landing page field
    Then we click submit on the "zipcode" field
    Then we assert "Yes, I have insurance" is on the page
    Then we verify attribution with cookie info validation