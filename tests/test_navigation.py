import pytest
from selenium import webdriver
from Sprint_3.locators import *


def test_go_to_account_page(browser):
    browser.get("https://stellarburgers.nomoreparties.site/")

    # Нажатие на кнопку "Личный кабинет"
    account_button = browser.find_element(*MainPageLocators.ACCOUNT_BUTTON)
    account_button.click()

    # Проверка перехода на страницу личного кабинета
    assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_go_to_buns_section(browser):
    browser.get("https://stellarburgers.nomoreparties.site/")

    # Нажатие на ссылку "Булки"
    buns_link = browser.find_element(*BurgerBuilderPageLocators.BUNS_SECTION)

    # Проверка перехода на страницу раздела "Булки"
    assert 'tab_tab_type_current__2BEPc' in buns_link.get_attribute('class')

def test_go_to_sauces_section(browser):
    browser.get("https://stellarburgers.nomoreparties.site/")

    # Нажатие на ссылку "Соусы"
    sauces_link = browser.find_element(*BurgerBuilderPageLocators.SAUCES_SECTION)
    sauces_link.click()

    # Проверка перехода на страницу раздела "Соусы"
    assert 'tab_tab_type_current__2BEPc' in sauces_link.get_attribute('class')


def test_go_to_fillings_section(browser):
    browser.get("https://stellarburgers.nomoreparties.site/")

    # Нажатие на ссылку "Начинки"
    fillings_link = browser.find_element(*BurgerBuilderPageLocators.FILLINGS_SECTION)
    fillings_link.click()
    assert 'tab_tab_type_current__2BEPc' in fillings_link.get_attribute('class')