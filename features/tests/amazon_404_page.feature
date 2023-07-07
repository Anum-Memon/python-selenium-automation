# Created by f_anu at 7/6/2023
Feature: Tests for 404 page

  Scenario: User is able to navigate to amazon
    Given Open Amazon product B07NF5WGQ1111 page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close Blog
    And Return to original window
