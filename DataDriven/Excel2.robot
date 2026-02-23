* Settings *
Library    SeleniumLibrary
Library    DataDriver    file=ddtLogindata.xlsx

Test Template    Login Test
Test Setup       Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
Suite Teardown   Close Browser

* Test Cases *
Login with valid data

* Keywords *
Login Test
    [Arguments]    ${username}    ${password}
    Wait Until Element Is Visible    xpath://input[@name='username']    10s
    Input Text    xpath://input[@name='username']    ${username}
    Input Text    xpath://input[@name='password']    ${password}
    Click Button    xpath://button[@type='submit']

    Wait Until Element Is Visible    xpath://h6[text()='Dashboard']    15s
    Element Should Be Visible        xpath://h6[text()='Dashboard']

    Sleep    5s