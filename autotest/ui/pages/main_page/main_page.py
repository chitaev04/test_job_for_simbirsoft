from autotest.ui.const.messages.assert_messages import auth_page_not_open, check_full_page_load
from autotest.ui.locators.loc_auth_page import AuthPageLocators
from autotest.ui.locators.loc_main_page import MainPageLocators
from autotest.ui.pages.base_class import BaseClass
from autotest.ui.const.URL import *


class MainPage(BaseClass):

    def open_auth_page(self):
        """Открытие страницы авторизации"""
        self.open_login_page()
        self.special_search_element(*MainPageLocators.AUTH_BUTTON).click()
        assert URL_AUTH == self.browser.current_url, auth_page_not_open
        assert self.special_search_element(*AuthPageLocators.TITLE_AUTH_PAGE), check_full_page_load
