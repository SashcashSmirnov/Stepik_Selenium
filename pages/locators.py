from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PSWD = (By.NAME, "login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')

    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PSWD = (By.NAME, "registration-password1")
    REGISTER_PSWD_CONFIRM = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button[value="Add to basket"]')
    NAME_OF_PRODUCT = (By.XPATH, "//div/h1")

    # NAME_OF_PRODUCT = (
    #     By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"]:nth-child(1)')
    NAME_OF_ADDED_PRODUCT = (By.XPATH, '//div/div/div/div/strong')
    PRICE_OD_ADDED_BOOK = (By.XPATH, '//div/div/div/div/article/div/div/p')
    PRICE_OD_ADDED_BOOK_IN_BASKET = (
        By.XPATH, '//div/div/div/div/div/p/strong')
