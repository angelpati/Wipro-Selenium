*** Settings ***

Resource         ./../Resources/Resource.robot
Library         SeleniumLibrary
Suite Setup         Open DB
Suite Teardown       Log    Close the Browser

*** Test Cases ***

#name of the testcase
Verify login with valid credentials
                Login
Verify Add to cart functionality
                Login
        Log     User selects the product
        Log   User adds the product to the cart
        Log     User verifies that t