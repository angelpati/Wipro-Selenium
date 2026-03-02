from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver


    backpack_add = (By.ID, "add-to-cart-sauce-labs-backpack")
    bike_light_add = (By.ID, "add-to-cart-sauce-labs-bike-light")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    checkout = (By.ID, "checkout")

    def verify_products(self):
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Bike Light']")
        self.driver.find_element(*self.cart_icon).click()


    def click_checkout(self):
        self.driver.find_element(*self.checkout).click()