Feature: Version command
    Scenario: Running the version command
        When running the version command
        Then the command completes successfully
        And the version number is printed
