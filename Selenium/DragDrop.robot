*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/
*** Test Cases ***
Verify multiselect check boxes
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window
        Wait Until Element Is Visible    id=dropdown-class-example
        @{labels}=      Get Selected List Labels    id=dropdown-class-example
        Log    @{labels}
        #select by label-visible text
        Select From List By Label    id=dropdown-class-example      Option3
        Sleep    1s
        Select From List By Label    id=dropdown-class-example      Option2
        Sleep    1s
        Select From List By Label    id=dropdown-class-example      Option1
        Sleep    1s


        Close Browser