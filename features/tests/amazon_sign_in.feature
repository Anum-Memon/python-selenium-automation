# Created by f_anu at 6/19/2023
Feature:Amazon sign in tests

  Scenario: Users can see sign in page
    Given open amazon main page
    When click orders
    Then verify sign in page opens

  Scenario: Sign In page can be opened from SignIn popup
   Given Open amazon main page
   When Click on button from SignIn popup
   Then Verify Sign In page opens