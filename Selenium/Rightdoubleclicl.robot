*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections
*** Variables ***
${url}      https://www.amazon.in/
*** Test Cases ***
Verify radio buttons
        Open Browser    ${url}      firefox
        Maximize Browser Window
        Sleep    3s
        Wait Until Element Is Visible    xpath://a[normalize-space()='Sell']
        Open Context Menu    link=Sell
        Sleep   2s
        Double Click Element    xpath://a[normalize-space()='Mobiles']

        Sleep    3s
        Close Browser