*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/
*** Test Cases ***
Verify login scenerio with valid credentials
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window
        #wait till the element is loaded
        Wait Until Element Is Visible    xpath://input[@value='radio1']

        #click login button
        Click Element    xpath://input[@value='radio1']
        #validate that the user is on the home page

        #close browser
        Close Browser