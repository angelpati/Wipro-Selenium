*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://jqueryui.com/datepicker/
*** Test Cases ***
Verify radio buttons
        Open Browser    ${url}      firefox
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        Select Frame    xpath://iframe[@class='demo-frame']
        Sleep    2s
        Click Element    xpath://input[@id='datepicker']
        Sleep    2s
        Click Element    xpath://a[normalize-space()='24']
        Sleep    3s



        Close Browser