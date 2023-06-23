# Created by f_anu at 6/19/2023
Feature:Amazon sign in tests

  Scenario: Users can see sign in page
    Given open amazon main page
    When click orders
    Then verify sign in page opens