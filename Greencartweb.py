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
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        time.sleep(2)
        driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='ADD TO CART'])[4]").click()
        driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='ADD TO CART'])[3]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='ADD TO CART'])[6]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='ADD TO CART'])[12]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()


        dropdown = driver.find_element(By.TAG_NAME, "select")
        # select class is used for drop downs
        sel = Select(dropdown)
        # select by visible text or label
        sel.select_by_visible_text("India")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()