import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager



time.sleep(4)
class Test_Multi:
    def test_website(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)
        driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()


        time.sleep(2)

        #add to cart
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()

        time.sleep(2)
        driver.find_element(By.ID, "first-name").send_keys("Angel")
        time.sleep(2)
        driver.find_element(By.ID, "last-name").send_keys("Pati")
        time.sleep(1)
        driver.find_element(By.ID, "postal-code").send_keys("110077")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='finish']").click()

        time.sleep(2)

        assert "Swag Labs" in driver.title
        driver.quit()