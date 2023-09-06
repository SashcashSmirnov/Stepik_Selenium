from pages.base_page import BasePage
from pages.login_page import LoginPage
from .locators import MainPageLocators
from .locators import ProductPageLocators
import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_item_in_basket(self):
        add_product = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product.click()

    def check_name_of_added_product(self):
        added_product = self.browser.find_element(
            *ProductPageLocators.NAME_OF_PRODUCT).text
        print(added_product)
        basket_product = self.browser.find_element(
            *ProductPageLocators.NAME_OF_ADDED_PRODUCT).text
        print(basket_product)
        assert added_product == basket_product, "Name of added book in basket does not match"

    def check_price_of_added_product(self):
        added_product_price = self.browser.find_element(
            *ProductPageLocators.PRICE_OD_ADDED_BOOK).text
        print(added_product_price)
        basket_product_price = self.browser.find_element(
            *ProductPageLocators.PRICE_OD_ADDED_BOOK_IN_BASKET).text
        print(basket_product_price)
        assert added_product_price == basket_product_price, "Price of added book in basket does not match"
