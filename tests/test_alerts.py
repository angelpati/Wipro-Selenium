import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

class Hello:
    def test_alerts(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(2)
        #switch the control to alert
        simplealt=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
        simplealt.click()
        alt=driver.switch_to.alert
        alt.accept() #click to accept button

        #confirmation alerts
        #switch the control to alret
        confalt=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")
        confalt.click()
        alt=driver.switch_to.alert
        alt.dismiss() #click to cancel button

        #prompt alerts
        promptalt=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
        promptalt.click()
        alt=driver.switch_to.alert
        alerttext=alt.text
        print(alerttext)
        alt.send_keys("test hello")
        alt.accept()
        time.sleep(2)
        driver.close()



