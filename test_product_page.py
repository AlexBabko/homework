import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage


# ----------------------------------------------------------------------------------------------------------------
@pytest.mark.need_review
class TestUser():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/"
        page = ProductPage(browser, link)
        page.open()
        page.register_new_user()
        time.sleep(1)

    def test_user_can_add_product_to_basket(self, setup, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        time.sleep(1)
        page.should_be_success_message()
        page.should_be_authorized_user()
        time.sleep(1)


@pytest.mark.need_review
class TestGuest():
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        time.sleep(1)
        page.should_be_success_message()
        time.sleep(1)

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        time.sleep(1)
        page.should_be_success_message()
        time.sleep(1)

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login()
