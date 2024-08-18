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


    def register_new_user(self, email, password):
        registration_email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        registration_password1_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1_INPUT)
        registration_password2_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2_INPUT)

        registration_email_input.send_keys(email)
        registration_password1_input.send_keys(password)
        registration_password2_input.send_keys(password)

        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()