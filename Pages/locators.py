from selenium.webdriver.common.by import By
# хорошей практикой является выносить селектор во внешнюю переменную.
# Каждый класс будет соответствовать каждому классу PageObject:


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    # теперь каждый селектор — это пара: как искать и что искать.
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASS_FIELD = (By.ID, "id_registration-password1")
    CONFIRM_FIELD = (By.ID, "id_registration-password2")
    BUTTON_SUBMIT = (By.NAME, "registration_submit")


class BasketPageLocators:
    ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    GO_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > span > a")
    MESSAGE_BASKET_EMPTY = (By.XPATH, "//p[contains(text(), 'empty')]")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3")



#//p[contains(text(), "Ваша корзина пуста")]
