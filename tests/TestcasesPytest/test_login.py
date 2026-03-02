import time
import pytest
from pages.loggin import LoginPage
from utilities.logger import get_logger
from utilities.excel import get_excel_data
test_data = get_excel_data("C:/Users/ANGEL PATI/Desktop/SeleniumPom/testdata/login_data.xlsx", "Sheet1")

logger=get_logger()
class TestLogin:
    def test_valid_login(self,driver):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        logger.info("Opening application")
        time.sleep(3)
        #create the object of login page
        lp=LoginPage(driver)
        logger.info("Entering the credentials")
        lp.login("Admin","admin123")

        time.sleep(2)
        assert "OrangeHRM" in driver.title

    def test_invalid_login(self,driver):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        #create the object og login_page
        lp=LoginPage(driver)
        lp.login("Admin","wrongpassword")
        time.sleep(2)
        assert "Invalid credentials" in lp.get_error_message()


# test data stored in excel sheet
@pytest.mark.parametrize("username, password", test_data)
def test_login_excel(self,driver, username, password):
    logger.info("Opening application")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(3)
    # create the object of login_page
    lp = LoginPage(driver)
    lp.login(username, password)

    if password == "admin123":
        assert "OrangeHRM" in driver.title
    else:
        assert "Invalid credentials" in lp.get_error_message()


