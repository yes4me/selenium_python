Feature: Showing off behave

  @basic-test
  Scenario: Run a simple test
    Given we have behave installed
    When we implement 5 tests
    Then behave will test them for us!

  @selenium-test
  Scenario: Run a simple test pm google.com
    Given user goes to http://www.google.com
    When user searches "123"
    Then user closes browser
