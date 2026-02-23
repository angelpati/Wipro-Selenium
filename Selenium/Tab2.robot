* Settings *
Library    SeleniumLibrary

* Variables *
${url}    https://rahulshettyacademy.com/AutomationPractice/

* Test Cases *
Verify Multiple Windows
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s
    Click Element    link=Open Tab
    @{windows}=     Get Window Handles
    Log To Console    ${windows}
    @{titles}=      Get Window Handles
    Log To Console    ${titles}
    Switch Window       title=QAClick Academy


    Element Text Should Be    xpath://a[@href='https://www.qaclickacademy.com']//img[@alt='Logo']    QAClick Academy
    Sleep    2s

    Switch Window    MAIN
    Sleep    2s

    Close Browser