import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys



class Test_Scroll:

    def test_scroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://jqueryui.com/datepicker/")

        time.sleep(3)
        driver.implicitly_wait(10)
        #fame= driver.find_element(By.XPATH,"//iframe[@class='demo-frame']
        driver.switch_to.frame(0)
        dateicker=driver.find_element(By.XPATH,"//input[@id='datepicker']")
        dateicker.click()
        driver.close()