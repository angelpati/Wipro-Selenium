import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class Test_Scroll:

    def test_scroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        alert = driver.find_element(By.XPATH,"//a[normalize-space()='alert.jpeg']")
        alert.click()

        #verify file download
        file_path= r"C:\Users\ANGEL PATI\Downloads"
        file_name="alert.jpeg"
        full_path = os.path.join(file_path, file_name)
        assert os.path.exists(full_path)

        time.sleep(3)
