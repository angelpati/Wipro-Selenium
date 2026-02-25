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
        driver.get("https://www.facebook.com/")

        time.sleep(3)


        actions = ActionChains(driver)
        email=driver.find_element(By.XPATH, "//input[@name='email']")
        seriesofactions=actions.move_to_element(email).key_down(Keys.SHIFT).send_keys("hello")
        seriesofactions.perform()
        # CTRL + A (Select All)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

        # CTRL + C (Copy)
        actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

        # Click password field
        password = driver.find_element(By.XPATH, "//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w x6s0dn4 x1k70j0n xzueoph xzboxd6 x14l7nz5']//div[@class='xjhjgkd x1s9qjmn x71vvrb x7gj0x1 x167l43f x11lwdb5 xfxe0gy x1szzd0g xh2argp x13fuv20 x18b5jzi x1q0q8m5 x1t7ytsu x178xt8z x1lun4ml xso031l xpilrb4 x9f619 x78zum5 xdt5ytf xl56j7k x1l0fimt x6ikm8r x10wlt62 x8fpamh x1plnv5r xf7dkkf xv54qhq x1n2onr6 xh8yej3 x1ja2u2z xggcdpo xzxmhi2 x1bhcc0k x1poa18a']")

        # CTRL + V (Paste)
        actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

        actions.click(email).key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
        time.sleep(4)
        password = driver.find_element(By.XPATH, "//input[@name='pass']")
        actions.click(password).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(4)
        driver.close()

        time.sleep(4)



        driver.close()