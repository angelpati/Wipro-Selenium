from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    # Locators
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_details(self, firstname, lastname, zipcode):
        self.driver.find_element(*self.first_name).send_keys(firstname)
        self.driver.find_element(*self.last_name).send_keys(lastname)
        self.driver.find_element(*self.postal_code).send_keys(zipcode)
        self.driver.find_element(*self.continue_btn).click()
