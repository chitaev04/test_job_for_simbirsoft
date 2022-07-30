from autotest.ui.const.login import USERNAME, PASSWORD
from autotest.ui.const.messages.assert_messages import bad_fill_auth, bad_fill_password, login_panel_not_displayed
from autotest.ui.const.URL import URL
from autotest.ui.locators.loc_auth_page import AuthPageLocators
from autotest.ui.locators.loc_main_page import MainPageLocators
from autotest.ui.pages.base_class import BaseClass


class AuthPageAssert(BaseClass):

    @staticmethod
    def assert_login_input(login_input):
        login_input_value = login_input.get_attribute('value')
        assert USERNAME == login_input_value, bad_fill_auth

    @staticmethod
    def assert_password_input(password_input):
        password_input_value = password_input.get_attribute('value')
        assert PASSWORD == password_input_value, bad_fill_password

    def assert_click_login_button(self, check_password_fill):
        if check_password_fill:
            self.special_search_element(*AuthPageLocators.INPUT_PASSWORD_MESSAGE)
        else:
            self.special_search_element(*MainPageLocators.USERNAME_DESK_CARD)
            assert URL == self.browser.current_url, login_panel_not_displayed
