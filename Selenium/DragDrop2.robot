*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php
*** Test Cases ***
Verify multiselect check boxes
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window
        Wait Until Element Is Visible    id=state
        Wait Until Element Is Visible    id=city
        @{labels}=      Get Selected List Labels    id=state
        Log    @{labels}
        @{labels}=      Get Selected List Labels    id=city
        Log    @{labels}
        #select by label-visible text
        Select From List By Label    id=state      Uttar Pradesh
        Sleep    1s
        Select From List By Label    id=city      Agra
        Sleep    1s



        Close Browser