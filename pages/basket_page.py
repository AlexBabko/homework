from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators

class BasketPage(BasePage):
    def go_to_basket(self):
        # assert self.is_element_present(*BasePageLocators.BASKET), "BASKET_BUTTON is not presented"
        basket_button1 = self.browser.find_element(*BasePageLocators.BASKET)
        basket_button1.click()
    def check_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.CARD), "Basket is not empty"
        assert self.is_not_element_present(*BasePageLocators.BASKET_WITH_ITEMS), "BASKET_WITH_ITEMS!!!"