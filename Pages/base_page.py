import time
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """базовую страницу, от которой будут унаследованы все остальные классы.
    В ней мы опишем вспомогательные методы для работы с драйвером."""
    def __init__(self, browser, url):# , timeout=10
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout) # неявного ожидания

    def open(self):
        """ткрывать нужную страницу в браузере, используя метод get()."""
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        # *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
        login_link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_not_element_present(self, how, what, timeout=4):
        """метод, который проверяет, что элемент не появляется на странице в течение заданного времени:
        упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый. """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Если мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с функцией until_not, в зависимости от того, какой результат мы ожидаем:
         будет ждать до тех пор, пока элемент не исчезнет."""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        """как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
        для всех проверок, что элемент действительно присутствует на странице,
        мы можем использовать этот метод."""
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(3)
        # try:
        #     WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        #     alert = self.browser.switch_to.alert
        #     alert_text = alert.text
        #     print(f"Your code: {alert_text}")
        #     alert.accept()
        # except (NoAlertPresentException, TimeoutException):
        #     print("No second alert presented")
