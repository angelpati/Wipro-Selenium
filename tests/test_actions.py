import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class Test_Scroll:

    def test_scroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.amazon.in/")

        time.sleep(3)


        actions = ActionChains(driver)
        bestsellers=driver.find_element(By.XPATH, "//a[normalize-space()='Bestsellers']")
        #double click using actions class
        actions.double_click(bestsellers).perform()
        time.sleep(2)
        driver.back()
        time.sleep(2)

        mobiles=driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")
        actions.context_click(mobiles).perform()
        time.sleep(2)

        driver.back()

        #move to element
        primes=driver.find_element(By.XPATH,"//span[normalize-space()='Prime']")
        actions.move_to_element(primes).perform()


        #click and hold
        fresh= driver.find_element(By.XPATH,"//div[@id='nav-flyout-groceries']//div[contains(@class,'nav-flyout-buffer-top')]")
        actions.click_and_hold(fresh).perform()


        driver.close()