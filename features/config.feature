Feature: Config command
    Scenario: Running the config command with a UI screen
        Given the environment variable EINK_RADIATOR_SCREEN_TYPE is set to ui
        When running the config command
        Then the command completes successfully
        And the screen configuration for a UI screen is printed

    Scenario: Running the config command with an Inky wHAT Red screen
        Given the environment variable EINK_RADIATOR_SCREEN_TYPE is set to inkywhat-red
        When running the config command
        Then the command completes successfully
        And the screen configuration for an Inky wHAT Red screen is printed
