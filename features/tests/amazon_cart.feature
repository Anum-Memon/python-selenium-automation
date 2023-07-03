# Created by f_anu at 6/23/2023
Feature: Amazon cart test

  Scenario: Users can see sign in page
    Given open amazon main page
    When click cart
    Then verify Your Amazon Cart is empty