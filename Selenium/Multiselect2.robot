*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/check-box.php
*** Test Cases ***
Verify multiselect check boxes
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window
        ${elements}=        Get WebElements    xpath://input[starts-with(@id,'c_bs_')]
        FOR    ${element}    IN    @{elements}
            Click Element    ${element}
            Sleep    1s

        END
        Close Browser