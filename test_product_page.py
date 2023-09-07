import random
import time
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.locators import BasePageLocators
from pages.basket_page import BasketPage


# class TestAddItemToBasket():
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param(
#                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(self, browser, link):

#     browser.get(link)
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_item_in_basket()
#     page.solve_quiz_and_get_code()
#     page.check_name_of_added_product()
#     page.check_price_of_added_product()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_item_in_basket()
#     time.sleep(2)
#     page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

# def test_guest_cant_see_success_message(self, browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

# def test_message_disappeared_after_adding_product_to_basket(self, browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_item_in_basket()
#     time.sleep(2)
#     page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

# @pytest.mark.xfail(reason='must failed')
# def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_item_in_basket()
#     assert page.is_not_element_present(
#         *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

# def test_guest_cant_see_success_message(self, browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     assert page.is_not_element_present(
#         *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

# @pytest.mark.xfail(reason='must failed')
# def test_message_disappeared_after_adding_product_to_basket(self, browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_item_in_basket()
#     assert page.is_disappeared(
#         *ProductPageLocators.SUCCESS_MESSAGE), 'Success message isnt disappeared'

# def test_guest_should_see_login_link_on_product_page(self, browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(self, browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()

# def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
#     link = "https://selenium1py.pythonanywhere.com/en-gb/"
#     page = BasketPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     time.sleep(1)
#     page.basket_should_be_empty()
#     page.text_basket_is_empty_should_be_present()

# def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
#     link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
#     page = BasketPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     time.sleep(1)
#     page.basket_should_be_empty()
#     page.text_basket_is_empty_should_be_present()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email=str(
            time.time()) + "@fakemail.org", password=random.randint(111111111, 999999999))
        time.sleep(2)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
        page = ProductPage(browser, link)
        page.open()
        page.add_item_in_basket()
        page.check_name_of_added_product()
        page.check_price_of_added_product()

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_item_in_basket()
        time.sleep(2)
        page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
