import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class Test_Scroll:

    def test_scroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/login")

        time.sleep(2)

        driver.find_element(By.NAME, "Email").send_keys("angelpati242@gmail.com")
        driver.find_element(By.NAME, "Password").send_keys("ANGE123ag@")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='RememberMe']").click()
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        time.sleep(2)

        driver.close()