import random
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Sprint_3.locators import *
import string
from Sprint_3.helpers.custom_wait import *


@pytest.fixture
def get_email():
    letter = string.ascii_letters
    email = ''
    for _ in range(8):
        email += random.choice(letter)
    return email + '@yandex.ru'


BASE_URL = "https://stellarburgers.nomoreparties.site/"


def test_successful_registration(browser: webdriver, get_email):
    browser.get(BASE_URL)

    # Нажатие на кнопку "Войти в аккаунт"
    sign_in_button = browser.find_element(*MainPageLocators.SIGN_IN_BUTTON)
    sign_in_button.click()

    # Нажатие на кнопку "Зарегистрироваться"
    registration_button = browser.find_element(*MainPageLocators.REGISTRATION_BUTTON)
    registration_button.click()

    # Ввод имени, email и пароля
    name_input = browser.find_element(*RegistrationPageLocators.NAME_INPUT)
    name_input.send_keys("Элизабет")

    email_input = browser.find_element(*RegistrationPageLocators.EMAIL_INPUT)
    email_input.send_keys(get_email)

    password_input = browser.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
    password_input.send_keys("hello111")

    # Нажатие на кнопку "Зарегистрироваться"
    register_button = browser.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
    register_button.click()
    # Проверка успешной регистрации
    assert url_should_have(browser, "https://stellarburgers.nomoreparties.site/login")
    login_button = browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
    assert login_button.is_displayed()


def test_invalid_password(browser):
    browser.get(BASE_URL)

    # Нажатие на кнопку "Войти в аккаунт"
    sign_in_button = browser.find_element(*MainPageLocators.SIGN_IN_BUTTON)
    sign_in_button.click()

    # Нажатие на кнопку "Зарегистрироваться"
    registration_button = browser.find_element(*MainPageLocators.REGISTRATION_BUTTON)
    registration_button.click()

    # Ввод некорректного пароля
    password_input = browser.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
    password_input.send_keys("123")

    # Нажатие на кнопку "Зарегистрироваться"
    register_button = browser.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
    register_button.click()

    # Проверка ошибки некорректного пароля
    error_message = browser.find_element(*RegistrationPageLocators.ERROR_MESSAGE)
    assert error_message.text == 'Некорректный пароль'