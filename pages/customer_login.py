from selenium.webdriver.support.wait import WebDriverWait
from utils import project_ec
from pages.base_page import BasePage
from pages.locators import login_locators as loc

class CustomerLogin(BasePage):
    page_url = '/customer/account/login'

    def fill_login_form(self, login, password):
        email_filed = self.find(loc.email_field_loc)
        password_filed = self.find(loc.password_field_loc)
        button = self.find(loc.button_loc)
        email_filed.send_keys(login)
        password_filed.send_keys(password)
        button.click()

    def check_error_alert_text_is(self, text):
        WebDriverWait(self.driver, 2).until(project_ec.text_is_not_empty_in_element(loc.error_locator))

        error_alert = self.driver.find_element(*loc.error_locator)
        assert error_alert.text == text
