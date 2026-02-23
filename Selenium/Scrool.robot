*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections
*** Variables ***
${url}      https://www.amazon.in/
*** Test Cases ***
Verify radio buttons
        Open Browser    ${url}      chrome
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        Scroll Element Into View    link=Sell on Amazon
        Sleep    3s
        Click Element    link=Sell on Amazon

        Sleep   2s
        Title Should Be    Amazon.in:   Selling on Amazon - Start Selling Now
        Double Click Element    xpath://a[normalize-space()='Mobiles']

        Sleep    3s
        Close Browser