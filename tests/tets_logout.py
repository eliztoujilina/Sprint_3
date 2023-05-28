from time import sleep
from Sprint_3.locators import *


def test_log_out(browser):
    browser.get("https://stellarburgers.nomoreparties.site/")

    # Нажатие на кнопку "Войти в аккаунт"
    sign_in_button = browser.find_element(*MainPageLocators.SIGN_IN_BUTTON)
    sign_in_button.click()

    # Ввод email и пароля
    email_input = browser.find_element(*RegistrationPageLocators.EMAIL_INPUT)
    email_input.send_keys("eliz_toujilina_10_123@ya.ru")

    password_input = browser.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
    password_input.send_keys("hello111")

    # Нажатие на кнопку "Войти"
    login_button = browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
    login_button.click()
    sleep(1)
    account_btn = browser.find_element(*MainPageLocators.ACCOUNT_BUTTON)
    account_btn.click()
    sleep(2)
    logout_btn = browser.find_element(*AccountPageLocators.LOGOUT_BUTTON)
    logout_btn.click()
    sleep(2)
    assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"
