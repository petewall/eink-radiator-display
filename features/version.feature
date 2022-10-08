Feature: Version command
    Scenario: Running the version command
        When running the version command
        Then command completes successfully
        And the version number is printed
