# Created by f_anu at 6/19/2023
Feature: Amazon search tests

  Scenario: Users can search on amazon
    Given open amazon main page
    When search for table
    Then verify search results shown for "table"

  Scenario: Users can search on amazon
    Given open amazon main page
    When search for coffee
    Then verify search results shown for "coffe"