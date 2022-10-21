Feature: Display command
    Scenario: Running the display command
        Given the environment variable EINK_RADIATOR_SCREEN_TYPE is set to null
        When running the display command with the save arg
        Then the command completes successfully
        And a quantized version of the image is displayed

    Scenario: Running the display command with a missing file
        Given the environment variable EINK_RADIATOR_SCREEN_TYPE is set to null
        When running the display command with a missing file
        Then the command returns an error
        And prints that the image file was not found
