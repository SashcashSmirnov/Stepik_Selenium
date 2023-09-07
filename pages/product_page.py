from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_in_basket(self):
        add_product = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product.click()

    def check_name_of_added_product(self):
        added_product = self.browser.find_element(
            *ProductPageLocators.NAME_OF_PRODUCT).text
        basket_product = self.browser.find_element(
            *ProductPageLocators.NAME_OF_ADDED_PRODUCT).text
        assert added_product == basket_product, "Name of added book in basket does not match"

    def check_price_of_added_product(self):
        added_product_price = self.browser.find_element(
            *ProductPageLocators.PRICE_OF_ADDED_BOOK).text
        basket_product_price = self.browser.find_element(
            *ProductPageLocators.PRICE_OF_ADDED_BOOK_IN_BASKET).text
        assert added_product_price == basket_product_price, "Price of added book in basket does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should not disappear"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear"
