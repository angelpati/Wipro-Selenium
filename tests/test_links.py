import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

DOWNLOAD_DIR="C://Users//ANGEL PATI//Downloads"
class Test_downlaod:
    def test_dw(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        links= driver.find_elements(By.TAG_NAME,"a")
        count=len(links)
        print(count)

        for link in links:
            print(link.text)
        time.sleep(2)
        driver.close()
