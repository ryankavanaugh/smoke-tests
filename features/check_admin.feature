# Created by ryankavanaugh at 4/11/18
@all
@admin

Feature: #Enter feature name here
  # Enter feature description here

  Scenario: Check admin panel to find new lead
    Then we open up the admin panel
    Then we login to the admin panel
    Then we navigate to the admin core lead page
    Then we print out the admin info