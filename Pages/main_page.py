from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    """класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка."""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     # *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
    #     login_link.click()
    #     #return LoginPage(browser=self.browser, url=self.browser.current_url) # При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы с браузером, а в качестве url передаем текущий адрес.
    #
    # # def should_be_login_link(self):
    # #     """ метод, который будет проверять наличие ссылки."""
    # #     self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
    #
    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"