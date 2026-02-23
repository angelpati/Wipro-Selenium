*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections
*** Variables ***
${url}      https://the-internet.herokuapp.com/drag_and_drop
*** Test Cases ***
Verify radio buttons
        Open Browser    ${url}      firefox
        Maximize Browser Window
        Sleep    3s
        Wait Until Element Is Visible    xpath://div[@id='column-a']
        Sleep   2s
        Drag And Drop    //div[@id='column-a']    //div[@id='column-b']
        
        Sleep    3s
        Close Browser