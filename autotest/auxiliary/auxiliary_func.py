import os
import random
import string

from autotest.ui.const.URL import URL
from autotest.ui.locators.loc_disk_page import DiskPageLocators
from autotest.ui.locators.loc_main_page import MainPageLocators


def logout_from_disk_page(driver):
    """Выход из текущей сессии пользователя"""
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(*DiskPageLocators.USER_MENU).click()
    driver.find_element(*DiskPageLocators.LOGOUT_USER_MENU).click()
    assert URL == driver.current_url, "Ошибка открытия главной страницы"
    assert driver.find_element(*MainPageLocators.AUTH_BUTTON), "Один из элементов главной страницы не отобразился"


def string_generate(length):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def dir_file():
    dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(os.path.sep, dir, "doc.txt")
    return path


def open_text_file():
    text_upl_file = open(dir_file(), 'r')
    read_text_file = text_upl_file.read()
    return read_text_file