import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from .locators import BasePageLocators


class ProductPage(BasePage):
        def add_product_to_basket(self):
         add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
         #price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
         #name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
         add_button.click()
        def compare_prices(self):
         total = self.browser.find_element(*ProductPageLocators.TOTAL)
         total_basket = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET)
         assert total.text == total_basket.text, "not equal"
         print('total.text',total.text,'total_basket.text',total_basket.text)
        def compare_names(self):
         add_to_basket_name_product = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_NAME_PRODUCT)
         name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
         assert name_product.text == add_to_basket_name_product.text, "not equal"
         print('name_product.text',name_product.text,'add_to_basket_name_product.text',add_to_basket_name_product.text)
        def should_be_success_message(self):
         assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_NAME_PRODUCT), "Success message is not presented, but should not be"
        def should_not_be_success_message(self):
         assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_NAME_PRODUCT), "Success message is presented, but should not be"
        def should_not_be_success_message_disappeared(self):
         assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_NAME_PRODUCT), "Success message is presented, but should not be"
        def register_new_user(self):
         email = str(time.time()) + "@fakemail.org"
         login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
         login_link.click()
         registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
         registration_email.send_keys(email)
         registration_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
         registration_password1.send_keys("alex23sdfsfdfedf")
         registration_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
         registration_password2.send_keys("alex23sdfsfdfedf")
         registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
         registration_submit.click()
         assert self.is_element_present(*LoginPageLocators.ICON), "ICON is not displayed"
        def go_to_login(self):
            #assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "LOGIN_LINK is not presented"
            basket_button4 = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
            basket_button4.click()

