from selenium.webdriver.common.by import By


class OverviewPage:

    def __init__(self, driver):
        self.driver = driver

    finish = (By.ID, "finish")

    def finish_order(self):
        self.driver.find_element(*self.finish).click()

    def verify_success(self):
        return self.driver.find_element(
            By.XPATH, "//h2[normalize-space()='Thank you for your order!']"
        )
