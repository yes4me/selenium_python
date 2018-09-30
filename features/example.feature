Feature: Testing Python module behave

  Background: some requirement of this test
    Given some setup condition

  @basic-test
  Scenario: Run a simple test
    Given we have behave installed
    When we implement 5 tests
    Then behave will test them for us!

  @multipleinputs-test
  Scenario Outline: Add guinea pigs
    Given the basket has "<initial>" guinea pigs
    When "<more>" guinea pigs are added to the basket
    Then the basket contains "<total>" guinea pigs

    Examples: Guinea pigs Counts
      | initial | more | total |
      |    0    |   1  |   1   |
      |    1    |   2  |   3   |
      |    5    |   4  |   9   |

  @selenium-test
  Scenario: Run a simple test pm google.com
    Given user goes to http://www.google.com
    When user searches "123"
    Then user closes browser
