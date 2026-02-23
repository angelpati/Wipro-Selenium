*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://the-internet.herokuapp.com/javascript_alerts
*** Test Cases ***
Verify multiselect check boxes
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window

        Wait Until Element Is Visible    xpath=(//button)[1]
        Click Element    xpath=(//button)[1]
        #Infromational alert- accept is for ok button
        Handle Alert        action=ACCEPT       timeout=3
        Sleep    1s
        Click Element    xpath=(//button)[2]
        #confirmational alret- accept is for ok button dismiss is for cancel button
        Handle Alert        action=DISMISS      timeout=3
        Sleep    2s
        Click Element    xpath=(//button)[3]

        Input Text Into Alert    Hello
        Sleep    5s






        Close Browser