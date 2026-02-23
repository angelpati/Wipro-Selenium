*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/
*** Test Cases ***
Verify multiselect check boxes
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window
        ${elements}=        Get WebElements    xpath://input[@type='checkbox']
        FOR    ${element}    IN    @{elements}
            Click Element    ${element}
            Sleep    1s
             
        END
        Close Browser