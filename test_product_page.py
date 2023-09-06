import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.product_page import ProductPage


class TestAddItemToBasket():
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_item_in_basket()
        page.solve_quiz_and_get_code()
        page.check_name_of_added_product()
        page.check_price_of_added_product()
