# Created by ryankavanaugh at 4/2/18
@all
@drift

Feature: Testing the Drift API

  Scenario: Testing the Drift API
    Given we post single and multiple driver payloads to the Drift API
    Then we will receive and perform data validation on the reponses