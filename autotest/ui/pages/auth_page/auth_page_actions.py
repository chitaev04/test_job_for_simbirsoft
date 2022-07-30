from autotest.ui.pages.asserts.assert_auth import AuthPageAssert
from autotest.ui.locators.loc_auth_page import AuthPageLocators
from autotest.ui.pages.main_page.main_page import MainPage
from autotest.ui.const.login import USERNAME, PASSWORD


class AuthPageActions(MainPage, AuthPageAssert):

    def fill_login_input(self):
        """Заполнения поля 'Логин или email'"""
        login_input = self.special_search_element(*AuthPageLocators.LOGIN_INPUT)
        login_input.send_keys(USERNAME)
        self.assert_login_input(login_input)

    def click_login_button(self, check_password_fill=False):
        """Нажатие на кнопку 'Войти'"""
        login_button = self.special_search_element(*AuthPageLocators.LOGIN_BUTTON)
        login_button.click()
        self.assert_click_login_button(check_password_fill)

    def fill_password_input(self):
        """Заполнение поля пароля"""
        password_input = self.special_search_element(*AuthPageLocators.PASSWORD_INPUT)
        password_input.send_keys(PASSWORD)
        self.assert_password_input(password_input)


