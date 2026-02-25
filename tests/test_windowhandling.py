import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Test_Windows:

    def test_windows(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/windows")
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)

        # Click link
        clickhere = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Click Here']"))
        )
        time.sleep(3)
        clickhere.click()

        # Wait until new window appears
        wait.until(EC.number_of_windows_to_be(2))

        windows = driver.window_handles

        # Switch to child window
        driver.switch_to.window(windows[1])

        # Wait for text in new window
        text = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'New Window')]"))
        )
        time.sleep(3)

        print("Child Window Text:", text.text)

        # Close child window
        driver.close()

        # Switch back to parent window
        driver.switch_to.window(windows[0])

        # Verify element still visible in parent
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Click Here']"))
        )
        time.sleep(3)

        print("Back to Parent Window")

        driver.quit()