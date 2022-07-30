from selenium.webdriver import ActionChains

from autotest.ui.pages.asserts.assert_disk_page import DiskPageAssert
from autotest.auxiliary import dir_file
from autotest.ui.locators.loc_disk_page import DiskPageLocators


class DiskPageUpload(DiskPageAssert):
    def upload_file(self):
        """Выгрузка файла"""
        new_txt = self.upload_txt_file()
        self.open_upload_file_tab(new_txt)

    def open_upload_file_tab(self, new_txt):
        """Открытие вкладки с загруженным файлом"""
        action = ActionChains(self.browser)
        action.double_click(new_txt).perform()
        self.browser.switch_to.window(self.browser.window_handles[2])
        self.assert_open_upload_file()

    def upload_txt_file(self):
        """Загрузка файла"""
        upload_input = self.special_search_element(*DiskPageLocators.UPLOAD_FILE_INPUT)
        upload_input.send_keys(dir_file())
        self.is_element_present(*DiskPageLocators.LOAD_COMPLETE)
        new_txt = self.assert_upload_file()
        return new_txt
