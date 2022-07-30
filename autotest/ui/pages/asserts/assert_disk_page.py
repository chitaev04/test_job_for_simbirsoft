from selenium.webdriver.common.by import By
from autotest.auxiliary.auxiliary_func import open_text_file
from autotest.ui.const.URL import URL_DISK_SOURCE, URL_DISK
from autotest.ui.const.messages.assert_messages import popup_folder_create_not_displayed, specify_folder_name, \
    popup_folder_not_open, disk_page_not_open, title_main_page_not_displayed, folder_names_not_fill, folder_not_create, \
    specify_doc_name, popup_create_doc_not_displayed, window_doc_not_displayed, file_in_list_missing, \
    incorrect_folder_name, creates_folder_not_open, field_folders_name_not_fill, file_not_load, texts_assert_error
from autotest.ui.locators.loc_disk_page import DiskPageLocators
from autotest.ui.pages.base_class import BaseClass


class DiskPageAssert(BaseClass):

    def assert_open_popup_create_disk(self):
        create_popup = self.special_search_element(*DiskPageLocators.CREATE_POPUP_NAME)
        assert create_popup, popup_folder_create_not_displayed

    def assert_open_window_create_folder(self):
        create_folder_title = self.special_search_element(*DiskPageLocators.CREATE_TITLE)
        create_folder_title_text = create_folder_title.get_attribute("textContent")
        assert create_folder_title_text == specify_folder_name, popup_folder_not_open

    def assert_open_disk_page(self):
        disk_page_title = self.special_search_element(*DiskPageLocators.DISK_TITLE)
        assert URL_DISK_SOURCE == self.browser.current_url, disk_page_not_open
        assert disk_page_title, title_main_page_not_displayed

    def assert_fill_folder_name_input(self, folder_name_value, text_folder_input):
        self.special_search_element(*DiskPageLocators.SAVE_DISK_BUTTON).click()
        new_folder_loc = f'[aria-label="{folder_name_value}"]'
        new_folder = self.browser.find_element(By.CSS_SELECTOR, new_folder_loc)
        assert text_folder_input == folder_name_value, folder_names_not_fill
        assert new_folder, folder_not_create
        return new_folder

    def assert_open_window_create_file(self):
        create_folder_title_text = self.special_search_element(*DiskPageLocators.CREATE_TITLE).text
        assert create_folder_title_text == specify_doc_name, popup_create_doc_not_displayed

    def assert_create_file_name(self, text_file_input):
        new_file = self.special_search_element(*DiskPageLocators.FILE_DOC_TITLE)
        new_file_text = new_file.text
        assert new_file_text == f"{text_file_input}.docx", window_doc_not_displayed

    def assert_close_file_tab(self, file_name_value):
        new_file = self.browser.find_element(By.CSS_SELECTOR, f'[aria-label="{file_name_value}.docx"]')
        assert new_file, file_in_list_missing

    def assert_double_click_folder(self, browser, folder_name):
        folder_title_text = self.special_search_element(*DiskPageLocators.FOLDER_TITLE).get_attribute('title')
        new_url = f"{URL_DISK}/{folder_name}"
        assert folder_title_text == folder_name, incorrect_folder_name
        assert new_url == browser.current_url, creates_folder_not_open

    @staticmethod
    def assert_file_name_input(file_name_value, text_file_input):
        assert text_file_input == file_name_value, field_folders_name_not_fill

    def assert_upload_file(self):
        new_txt = self.special_search_element(*DiskPageLocators.NEW_UPLOAD_FILE)
        assert new_txt, file_not_load
        return new_txt

    def assert_open_upload_file(self):
        upload_file_text = self.special_search_element(*DiskPageLocators.TEXT_FROM_UPLOAD_FILE).text
        text_from_upload_file = open_text_file()
        assert upload_file_text == text_from_upload_file, texts_assert_error
