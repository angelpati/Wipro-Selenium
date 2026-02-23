*** Settings ***
#setting we add the external library deatils, resources, set up and tear down commands
Library          SeleniumLibrary

****Test Cases***
Verify login with valid credentials
        Log To Console    Enter username
        Log To Console    Enter password
        Log To Console    click on the login button
        Log To Console    user is on the home page