*** Settings ***
#setting we add the external library deatils, resources, set up and tear down commands
Library          SeleniumLibrary

****Test Cases***
Verify login with valid credentials 
        Log    Enter username
        Log    Enter password
        Log    click on the login button
        Log    user is on the home page
