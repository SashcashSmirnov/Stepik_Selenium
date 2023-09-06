
import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_login_url() is True, 'Not login url'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM) is True, 'Login form does not exist'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM) is True, 'Registration form does not exist'
