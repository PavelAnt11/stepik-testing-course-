from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        paswd = "ggfglovkvr636sf5"
        em = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        em.send_keys(email)
        ps = self.browser.find_element(*LoginPageLocators.PASS_FIELD)
        ps.send_keys(paswd)
        cf = self.browser.find_element(*LoginPageLocators.CONFIRM_FIELD)
        cf.send_keys(paswd)
        bt = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT)
        bt.click()
        time.sleep(15)

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url, "Error"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "register form is not presented"
