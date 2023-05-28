import pytest
from selenium import webdriver


@pytest.fixture # фикстура драйвера
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()
