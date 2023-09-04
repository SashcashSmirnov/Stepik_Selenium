import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage


def test_guest_can_see_login_page(browser):

    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):

    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    page.open()                      # открываем страницу
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()
