*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/check-box.php
*** Test Cases ***
Verify login scenerio with valid credentials
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window
        #wait till the element is loaded
        Wait Until Element Is Visible    xpath://input[@id='c_bs_1']
        #enter the text in the username foeld
        Wait Until Element Is Visible    xpath://input[@id='c_bs_2']

        #click login button
        Click Element    xpath://input[@id='c_bs_1']

        Click Element    xpath://input[@id='c_bs_2']

        #close browser
        Close Browser