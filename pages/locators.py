from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset .basket-items")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD1_INPUT = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD2_INPUT = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_ABOUT_ADDING_PRODUCT = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner > strong")
    MESSAGE_ABOUT_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages div:nth-child(3)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_page .product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > .alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")