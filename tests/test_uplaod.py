import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class Test_Scroll:

    def test_scroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()
        time.sleep(2)

        browse=driver.find_element(By.XPATH,"//input[@id='file-upload']")
        browse.send_keys("C://Users//ANGEL PATI//Desktop//photo.jpg")
        time.sleep(2)
        upload=driver.find_element(By.XPATH,"//input[@id='file-submit']")
        upload.click()
        fileuplaod=driver.find_element(By.XPATH,"//h3[normalize-space()='File Uploaded!']")
        assert fileuplaod.text=="File Uploaded!"

        time.sleep(3)
