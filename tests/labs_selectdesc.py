import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

class Test_MultiSelectRadio:
    def test_dropdown(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.maximize_window()
        driver.get("https://trytestingthis.netlify.app/")
        time.sleep(2)
        # select class is used for drop downs
        dropdown = driver.find_element(By.XPATH, "//input[@type="checkbox"]")
        # select class is used for drop downs
        sel = Select(dropdown)
        # select by visible text or label
        sel.select_by_visible_text("Option 1")
        time.sleep(2)
        sel.select_by_value("Option2")
        time.sleep(2)
        sel.select_by_index(3)
        time.sleep(2)


