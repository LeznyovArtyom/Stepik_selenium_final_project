from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET)

    
    def should_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET)