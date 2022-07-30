from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from autotest.ui.locators.loc_main_page import MainPageLocators

from autotest.ui.const.URL import *


class BaseClass:

    def __init__(self, browser, url=URL, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_login_page(self):
        """Открытие страницы авторизации"""
        self.browser.get(self.url)
        assert URL == self.browser.current_url, "Ошибка открытия страницы авторизации}"
        assert self.special_search_element(
            *MainPageLocators.AUTH_BUTTON), "Один из элементов страницы авторизации не отобразился"

    def special_search_element(self, locator, element_name, several_elements=False):
        """Универсальный поиск элементов"""
        if several_elements:
            try:
                self.browser.find_elements(locator, element_name)
            except NoSuchElementException:
                print(f'\nЭлементы {element_name} не найдены!')
                return False
            return self.browser.find_elements(locator, element_name)
        else:
            try:
                self.browser.find_element(locator, element_name)
            except NoSuchElementException:
                print(f'\nЭлемент {element_name} не найден!')
                return False
            return self.browser.find_element(locator, element_name)

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print(f'\nЭлемент {what} не найден!')
            return False
        return True
