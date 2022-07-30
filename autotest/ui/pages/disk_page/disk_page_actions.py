from autotest.ui.pages.asserts.assert_disk_page import DiskPageAssert
from autotest.auxiliary import string_generate
from autotest.ui.locators.loc_disk_page import DiskPageLocators
from autotest.ui.pages.auth_page.auth_page import AuthPageActions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class DiskPageActions(AuthPageActions, DiskPageAssert):

    def open_popup_create_disk(self):
        """Открытие всплывающего окна создания элементов"""
        self.special_search_element(*DiskPageLocators.CREATE_BUTTON_DISK).click()
        self.assert_open_popup_create_disk()

    def open_window_create_folder(self):
        """Открытие окна создания папки"""
        self.special_search_element(*DiskPageLocators.CREATE_FOLDER_BUTTON).click()
        self.assert_open_window_create_folder()

    def input_fill_folder_name(self):
        """Указание названия папки"""
        folder_name_input = self.special_search_element(*DiskPageLocators.NAME_INPUT, several_elements=True)[1]
        folder_name_input.send_keys(Keys.CONTROL + "a")
        folder_name_input.send_keys(Keys.BACKSPACE)
        text_folder_input = string_generate(10)
        folder_name_input.send_keys(text_folder_input)
        folder_name_value = folder_name_input.get_attribute('value')
        new_folder = self.assert_fill_folder_name_input(folder_name_value, text_folder_input)
        self.double_click_folder(folder_name_value, new_folder)

    def double_click_folder(self, folder_name, creates_folder):
        """Открытие созданной папки двойным кликом"""
        action = ActionChains(self.browser)
        action.double_click(creates_folder).perform()
        self.assert_double_click_folder(self.browser, folder_name)

    def open_create_file_window(self):
        """Открытие окна создания папки"""
        self.special_search_element(*DiskPageLocators.CREATE_FILE_BUTTON).click()
        self.assert_open_window_create_file()

    def fill_file_name_input(self):
        """Заполнение поля наименования файла"""
        file_name_input = self.special_search_element(*DiskPageLocators.NAME_INPUT, several_elements=True)[1]
        file_name_input.send_keys(Keys.CONTROL + "a")
        file_name_input.send_keys(Keys.BACKSPACE)
        text_file_input = string_generate(8)
        file_name_input.send_keys(text_file_input)
        file_name = file_name_input.get_attribute('value')
        self.assert_file_name_input(file_name, text_file_input)
        return file_name

    def save_file(self):
        """Сохранение файла"""
        file_name = self.fill_file_name_input()
        self.special_search_element(*DiskPageLocators.SAVE_DISK_BUTTON).click()
        self.browser.switch_to.window(self.browser.window_handles[2])
        iframe = self.special_search_element(*DiskPageLocators.IFRAME_LOC)
        self.browser.switch_to.frame(iframe)
        self.assert_create_file_name(file_name)
        self.close_file_tab(file_name)

    def close_file_tab(self, file_name):
        """Закрытие вкладки для проверки наличия созданного файла в списке"""
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.assert_close_file_tab(file_name)