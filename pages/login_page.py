from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert 'login' in login_url, "Login url is incorrect"

    def should_be_login_form(self):
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "Login form is not presented"

    def should_be_register_form(self):
        register_form = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert register_form, "Register form is not presented"