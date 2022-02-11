from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def go_to_basket_page(self):
        btn = self.browser.find_element(*BasketPageLocators.GO_TO_BASKET)
        btn.click()

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Товар в корзине"

    def should_be_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), "Basket  is not empty"
