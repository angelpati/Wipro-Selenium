import time

import pytest
from pages.loggin import LoginPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage
from pages.overview import OverviewPage
from utilities.excel import get_excel_data
from utilities.logger import get_logger

logger = get_logger()

file_path = r"C:\Users\ANGEL PATI\Desktop\SeleniumPom\testdata\exceldata.xlsx"
test_data = get_excel_data(file_path)


class TestSauceDemo:

    @pytest.mark.parametrize("username,password", test_data)
    def test_complete_order_flow(self, driver, username, password):

        logger.info("Starting SauceDemo Test")

        login = LoginPage(driver)
        login.login(username, password)



        cart = CartPage(driver)
        cart.verify_products()
        cart.click_checkout()


        checkout = CheckoutPage(driver)
        checkout.enter_details("Deepak Kumar", "Prabhat", "811317")
        overview = OverviewPage(driver)
        overview.finish_order()


        assert overview.verify_success()
        logger.info("Order completed successfully")