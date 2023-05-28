from selenium.webdriver.common.by import By

class MainPageLocators:
    SIGN_IN_BUTTON = (By.XPATH, '//*[contains(text(), "Войти в аккаунт")]') # кнопка "Войти в аккаунт"
    ACCOUNT_BUTTON = (By.XPATH,'//p[text()="Личный Кабинет"]/..') # кнопка "Личный кабинет"
    REGISTRATION_BUTTON = (By.XPATH, '//*[contains(text(), "Зарегистрироваться")]') # кнопка "Зарегистрироваться"
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[text()="Восстановить пароль"]') # кнопка "Восстановить пароль"
    LOGO = (By.XPATH, '//a[@class="logo"]') # кнопка лого
    PROFILE_ICON = (By.XPATH, '//div[contains(@class, "profile-button")]') # кнопка профиль

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, '//input[@name="name"]') # поле имя
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # поле почта
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]') # поле пароль
    REGISTER_BUTTON = (By.XPATH,'//button[contains(text(), "Зарегистрироваться")]') # поле "Зарегистрироваться"
    ERROR_MESSAGE = (By.XPATH, '//div[@class="input__container"]//p') # сообщение об ошибке
    LOGIN_LINK = (By.XPATH, '//a[text()="Войти"]')  # Ссылка войти

class RestorePass:
    RESTORE_BUTTON = (By.XPATH, '//button[text()="Восстановить"]') # кнопка "Восстановить"

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]') # поле почта
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]') # поле пароль
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]') # кнопка "Войти"

class AccountPageLocators:
    LOGOUT_BUTTON = (By.XPATH, '//*[contains(text(), "Выход")]') # кнопка "Выход"

class BurgerBuilderPageLocators:
    BUNS_SECTION = (By.XPATH, '//span[text()="Булки"]/..') # вкладка "Булки"
    SAUCES_SECTION = (By.XPATH,'//span[text()="Соусы"]/..') # вкладка "Соусы"
    FILLINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]/..') # вкладка "Начинки"