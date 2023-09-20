from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    BASKET_TEXT_EMPTY = (By.XPATH, '//div/div/div/div/p')
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items .row")
    ALERT = (By.CSS_SELECTOR, "div#content_inner p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


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
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'form[id="add_to_basket_form"]')
    NAME_OF_PRODUCT = (By.XPATH, "//div/h1")
    NAME_OF_ADDED_PRODUCT = (By.XPATH, '//div/div/div/div/strong')
    PRICE_OF_ADDED_BOOK = (By.XPATH, '//div/div/div/div/article/div/div/p')
    PRICE_OF_ADDED_BOOK_IN_BASKET = (
        By.XPATH, '//div/div/div/div/div/p/strong')
    ADD_TO_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
