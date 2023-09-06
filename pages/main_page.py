from pages.base_page import BasePage
from pages.login_page import LoginPage

import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators
from .locators import ProductPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK), "Login link is not presented"
