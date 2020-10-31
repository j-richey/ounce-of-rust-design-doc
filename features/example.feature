Feature: Withdraw Money from ATM

  A user with an account at a bank would like to withdraw money from an ATM.

  Provided he has a valid account and debit or credit card, he should be allowed
  to make the transaction. The ATM will tend the requested amount of money,
  return his card, and subtract amount of the withdrawal from the user's account.

  Scenario: Scenario 1
    Given preconditions
    When actions
    Then results

  Scenario Outline: A user withdraws money from an ATM
    Given <Name> has a valid Credit or Debit card
    And their account balance is <OriginalBalance>
    When they insert their card
    And withdraw <WithdrawalAmount>
    Then the ATM should return <WithdrawalAmount>
    And their account balance is <NewBalance>

    Examples:
      | Name   | OriginalBalance | WithdrawalAmount | NewBalance |
      | Eric   | 100             | 45               | 55         |
      | Gaurav | 100             | 40               | 60         |
      | Ed     | 1000            | 200              | 800        |
