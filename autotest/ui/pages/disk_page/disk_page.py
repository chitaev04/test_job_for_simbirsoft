from autotest.ui.locators.loc_main_page import MainPageLocators
from autotest.ui.pages.disk_page.disk_page_actions import DiskPageActions
from autotest.ui.pages.disk_page.upload_files import DiskPageUpload


class DiskPage(DiskPageActions, DiskPageUpload):

    def open_disk_page(self):
        """Открытие окна 'Диск'"""
        self.special_search_element(*MainPageLocators.DISK_BUTTON).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.assert_open_disk_page()

    def create_folder_disk(self):
        """Создание папки"""
        self.open_popup_create_disk()
        self.open_window_create_folder()
        self.input_fill_folder_name()

    def create_file_disk(self):
        """Создание файла"""
        self.open_popup_create_disk()
        self.open_create_file_window()
        self.save_file()

    def upload_file_disk(self):
        """Выгрузка файла в систему"""
        self.upload_file()


