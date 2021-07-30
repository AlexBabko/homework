from selenium.webdriver.common.by import By
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, 'span.btn-group > a.btn.btn-default')
    CARD = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET = (By.CSS_SELECTOR, 'span.btn-group > a.btn.btn-default')
    BASKET_WITH_ITEMS = (By.CSS_SELECTOR, '[class="col-sm-6 h3"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')
    ICON = (By.CSS_SELECTOR, '.icon-user')
    LINK = (By.LINK_TEXT, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '[class="price_color"]')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    TOTAL_BASKET = (By.CSS_SELECTOR, '[class="price_color"]')
    TOTAL = (By.CSS_SELECTOR, '[class="alertinner "] p strong')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    ADD_TO_BASKET_NAME_PRODUCT = (By.CSS_SELECTOR, 'div.alertinner strong')