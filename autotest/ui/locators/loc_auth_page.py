from selenium.webdriver.common.by import By


class AuthPageLocators:
    """Компоненты страницы авторизации"""

    TITLE_AUTH_PAGE = (By.CSS_SELECTOR, '[class="passp-add-account-page-title"]')
    LOGIN_INPUT = (By.CSS_SELECTOR, '[name="login"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[id="passp:sign-in"]')
    INPUT_PASSWORD_MESSAGE = (By.CSS_SELECTOR, '[for="passp-field-passwd"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="passwd"]')
