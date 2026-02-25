import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



class Test_Scroll:

    def test_scroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()
        time.sleep(2)
        #this is a global setting that applies to every eleemnt location call for the entire season
        driver.implicitly_wait(2)
        #explicit wait
        radio_btn=driver.find_element(By.XPATH,"")
        wait=WebDriverWait(driver,timeout=2)
        wait.until(lambda_:radio_btn.is_displayed())

        #custon wait or fluent wait
        errors= [NoSuchElementException,ElementNotInteractableException]
        wait=WebDriverWait(driver,timeout=2,poll_frequency=.2,ignored_exceptions=errors)
        wait.until(lambda_:radio_btn.send_keys("Displayed") or True)
        driver.close()
