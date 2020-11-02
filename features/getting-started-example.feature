Feature: Getting Started Example

  | As a Rust application developer,
  | I want an example of getting started with the library,
  | so I can quickly start integrating the library into my application.

  Scenario: Demo application prints hello
    When the demo application is run
    Then "Hello World!" is displayed

  Scenario: Demo application customizes output
    Given a command line argument of 'Bob'
    And a command line argument of 'Smith'
    When the demo application is run
    Then "Hello Bob Smith!" is displayed
