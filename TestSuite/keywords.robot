*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Verify login with valid credentials
                    Login
Verify Add to cart functionality
            Login
        Log    User selects the product
        Log    User add the product to the cart
        Log    User verifies that the product with details is added to cart
*** Keywords ***
Login
        Log     Enter username
        Log    Enter password
        Log    click to login button
        Log    user is on the homepage
 