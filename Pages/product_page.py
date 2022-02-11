from .base_page import BasePage
from .locators import BasketPageLocators


class PageBasket(BasePage):
    def add_goods_to_basket(self):
        btn = self.browser.find_element(*BasketPageLocators.ADD_BASKET)
        btn.click()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*BasketPageLocators.ADD_BASKET), "Add to basket button isn't presented"

    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*BasketPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        # Это можно было бы сделать с помощью split() и сравнения строк,
        # Но не вижу необходимости усложнять код
        assert product_name == message, "No product name in the message"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*BasketPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price == message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*BasketPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"
