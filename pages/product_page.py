from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()


    def should_be_message_about_adding_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING_PRODUCT), "Message about adding product is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, "Incorrect product added"


    def should_be_message_about_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_BASKET_TOTAL), "Message about basket total is not presented"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, "Basket total doesn't match product price"