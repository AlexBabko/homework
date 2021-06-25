import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    _step = browser.find_element_by_class_name("btn-add-to-basket")
    time.sleep(30)
    try:
        _step = browser.find_element_by_class_name("btn-add-to-basket")
        return True
    except NoSuchElementException:
        print('Error')
        return False
