from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "error"
        assert True
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "ID_LOGIN-USERNAME is not presented"
        assert True
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "ID_LOGIN-PASSWORD is not presented"
        assert True
    def login_one(self):
        # реализуйте проверку, что есть форма регистрации на странице
        login1 = self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME)
        login1.click()
    def register_new_user(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        email = str(time.time()) + "@fakemail.org"
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL) 
        registration_email.send_keys("email")
        registration_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        registration_password1.send_keys("alex23sdfsfdfedf")
        registration_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        registration_password2.send_keys("alex23sdfsfdfedf")
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_submit.click()