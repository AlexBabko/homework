import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasePage

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])                                           
                                  #  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])          
   

#@pytest.mark.login_guest
class TestLoginFromMainPage():
 def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser, link)
    page.open()
    #page.should_be_login_link()
    page.go_to_basket()
    page.check_basket_is_empty()
    time.sleep(1)
 def test_guest_should_see_login_link(self, browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()