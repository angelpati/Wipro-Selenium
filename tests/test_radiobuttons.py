import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class Test_MultiSelectRadio:

    def test_multiradio(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@value='radio2']").click()

        time.sleep(2)

        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

        for box in checkboxes:
            box.click()

        time.sleep(3)

        driver.close()