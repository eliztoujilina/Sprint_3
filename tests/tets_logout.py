from time import sleep
from Sprint_3.locators import *
from helpers.custom_wait import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    # Нажатие на кнопки "Войти" и "Выйти"
    login_button = browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
    login_button.click()
    locator = '//p[text()="Личный Кабинет"]/..'
    account_btn = WebDriverWait(driver=browser, timeout=5).until(EC.presence_of_element_located((MainPageLocators.ACCOUNT_BUTTON)))
    account_btn.click()
    logout_btn = WebDriverWait(driver=browser, timeout=5).until(EC.presence_of_element_located((AccountPageLocators.LOGOUT_BUTTON)))
    logout_btn.click()
    assert url_should_have(browser, "https://stellarburgers.nomoreparties.site/login")
