# Created by f_anu at 6/19/2023
Feature: Amazon search tests

#  Scenario: Users can search on amazon
#    Given open amazon main page
#    When search for table
#    Then verify search results shown for "table"
#
#  Scenario: Users can search on amazon
#    Given open amazon main page
#    When search for coffee
#    Then verify search results shown for "coffe"

   Scenario Outline: User can search on Amazon
    Given Open amazon main page
    When Search for <search_word>
    Then Verify search results shown for <search_result>
    Examples:
    |search_word      |search_result    |
    |table            |"table"          |
    |coffee           |"coffee"         |
    |mug              |"mug"            |
    |dress            |"dress"          |


    Scenario: User can add a product to the cart
    Given Open amazon main page
    When Search for Tritan Farm to Table Pitcher
    And Click on the first product
    And Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

 Scenario: Verify that user can see product names and image
    Given open amazon main page
    When Search for table
    Then Verify that every product has a names and image