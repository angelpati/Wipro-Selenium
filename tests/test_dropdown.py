import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager



time.sleep(4)
class Test_MultiSelectRadio:
    def test_dropdown(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.maximize_window()
        driver.get("https://demoqa.com/select-menu")
        time.sleep(2)


        dropdown = driver.find_element(By.CLASS_NAME, "css-hlgwow")
        # select class is used for drop downs
        sel = Select(dropdown)
        # select by visible text or label
        sel.select_by_visible_text("Group 1, Option 1")
        time.sleep(2)
        sel.select_by_value("Group 1, Option2")
        time.sleep(2)
        sel.select_by_index(3)
        time.sleep(2)
        sel.select_by_index(4)

        time.sleep(2)
        sel.select_by_index(5)
        time.sleep(2)
        driver.quit()

