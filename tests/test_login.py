import time
from lib2to3.pgen2 import driver
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Sprint_3.helpers.custom_wait import *

from Sprint_3.locators import *


def test_login_from_main_page(browser):
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
    # Проверка успешного входа
    assert url_should_have(browser, "https://stellarburgers.nomoreparties.site/", timeout=3)

def test_login_from_account_page(browser):
    browser.get("https://stellarburgers.nomoreparties.site/")

    # Нажатие на кнопку "Личный кабинет"
    account_button = browser.find_element(*MainPageLocators.ACCOUNT_BUTTON)
    account_button.click()

    # Ввод email и пароля
    email_input = browser.find_element(*RegistrationPageLocators.EMAIL_INPUT)
    email_input.send_keys("eliz_toujilina_10_123@ya.ru")

    password_input = browser.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
    password_input.send_keys("hello111")

    # Нажатие на кнопку "Войти"
    login_button = browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
    login_button.click()
    time.sleep(1)
    # Проверка успешного входа
    account_button.click()
    assert url_should_have(browser, "https://stellarburgers.nomoreparties.site/account/profile")

def test_click_login_in_btn_in_register_page(browser):
    browser.get("https://stellarburgers.nomoreparties.site/")

    # Нажатие на кнопку "Войти в аккаунт"
    sign_in_button = browser.find_element(*MainPageLocators.SIGN_IN_BUTTON)
    sign_in_button.click()

    # Нажатие на кнопку "Зарегистрироваться"
    registration_button = browser.find_element(*MainPageLocators.REGISTRATION_BUTTON)
    registration_button.click()
    login_link = browser.find_element(*RegistrationPageLocators.LOGIN_LINK)
    login_link.click()

    assert url_should_have(browser, "https://stellarburgers.nomoreparties.site/login")


def test_login_from_password_recovery_page(browser):
    browser.get("https://stellarburgers.nomoreparties.site/")

    # Нажатие на кнопку "Войти в аккаунт"
    sign_in_button = browser.find_element(*MainPageLocators.SIGN_IN_BUTTON)
    sign_in_button.click()

    # Нажатие на кнопку "Забыли пароль?"
    forgot_password_button = browser.find_element(*MainPageLocators.FORGOT_PASSWORD_BUTTON)
    forgot_password_button.click()

    # Ввод email
    email_input = browser.find_element(*RegistrationPageLocators.EMAIL_INPUT)
    email_input.send_keys("eliz_toujilina_10_123@ya.ru")

    # Нажатие на кнопку "Войти"
    restor_button = browser.find_element(*RestorePass.RESTORE_BUTTON)
    restor_button.click()
    # Проверка успешного входа

    assert url_should_have(browser, 'https://stellarburgers.nomoreparties.site/reset-password')