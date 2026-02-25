import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class Test_Scroll:

    def test_scroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.amazon.in/")

        time.sleep(3)

        amz=driver.find_element(By.XPATH, "//a[normalize-space()='Amazon Pay on Merchants']")
        driver.execute_script("arguments[0].scrollIntoView();",amz)
        time.sleep(2)
        amz.click()
        #scroll up
        driver.execute_script("window.scrollBy(0,-1000)")
        time.sleep(2)
        #scroll down
        driver.execute_script("window.scrollBy(0,5000)")

        driver.close()