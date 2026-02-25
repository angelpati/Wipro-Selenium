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
        driver.find_element(By.XPATH, "//input[@value='Register']").click()
        driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
        time.sleep(2)

        driver.find_element(By.NAME, "FirstName").send_keys("ANGEL")
        driver.find_element(By.NAME, "LastName").send_keys("PATI")
        driver.find_element(By.NAME, "Email").send_keys("angelpati242@gmail.com")
        time.sleep(2)
        driver.find_element(By.NAME, "Password").send_keys("ANGE123ag@")
        driver.find_element(By.NAME, "ConfirmPassword").send_keys("ANGE123ag@")
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[2]//div[1]//div[2]//div[3]//div[2]//input[1]").click()
        driver.find_element(By.NAME, "recipint-name").send_keys("ANGE123ag@")
        driver.find_element(By.NAME, "Password").send_keys("ANGE123ag@")
        driver.find_element(By.NAME, "Password").send_keys("ANGE123ag@")
        driver.find_element(By.NAME, "Password").send_keys("ANGE123ag@")
        driver.find_element(By.XPATH, "//div[6]//div[1]//div[2]//div[3]//div[2]//input[1]").click()
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()



