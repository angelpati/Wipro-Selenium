*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://practice.automationtesting.in/
*** Test Cases ***
Verify login scenerio with valid credentials
        Open Browser        ${url}      firefox
        #maximize the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        #wait till the element is loaded
        Wait Until Element Is Visible    xpath://img[@alt='Shop Selenium Books']

        Select Frame    xpath://img[@title='Selenium Ruby']
        Sleep    2s
        Click Element    xpath://li[@class='post-160 product type-product status-publish has-post-thumbnail product_cat-selenium product_tag-ruby product_tag-selenium has-post-title no-post-date has-post-category has-post-tag has-post-comment has-post-author first instock downloadable taxable shipping-taxable purchasable product-type-simple']//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'][normalize-space()='Add to basket']
        Sleep    2s

