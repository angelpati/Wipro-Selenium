import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



time.sleep(4)
class Test_MultiSelectRadio:
    def test_multiradio(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")

        time.sleep(2)

        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        time.sleep(3)

        assert "OrangeHRM" in driver.title

        pim = driver.find_element(By.LINK_TEXT, "PIM")
        pim.click()

        time.sleep(3)
        # click on check box one by one
        checkbox_list = driver.find_elements(By.XPATH, "//i[@class = 'oxd-icon bi-check oxd-checkbox-input-icon']")
        count = len(checkbox_list)
        print(count)

        # Iterate the list
        for i in range(1, checkbox_list):
            time.sleep(2)
            i.click()

        # close only the  current browser session
        driver.close()








