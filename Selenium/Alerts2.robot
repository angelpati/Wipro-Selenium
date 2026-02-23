* Settings *
Library    SeleniumLibrary

* Variables *
${url}    https://www.tutorialspoint.com/selenium/practice/alerts.php

* Test Cases *
Handle Tutorialspoint Alerts
    Open Browser    ${url}    chrome
    Maximize Browser Window

    # Click simple alert and accept
    Click Element    xpath=//button[text()='Alert']
    Handle Alert    action=ACCEPT    timeout=5s

    # Click delayed alert and accept
    Click Element    xpath=(//button[text()='Click Me'])[1]
    Handle Alert    action=ACCEPT    timeout=10s
    Sleep    3s

    # Click confirm alert and dismiss
    Click Element    xpath=(//button[text()='Click Me'])[2]
    Handle Alert    action=DISMISS    timeout=5s
    Sleep    3s

    # Click prompt alert, enter text and accept
    Click Element    xpath=(//button[text()='Click Me'])[3]
    Input Text Into Alert    Angel
    Handle Alert    action=ACCEPT    timeout=5s
    Sleep    3s

    Close Browser