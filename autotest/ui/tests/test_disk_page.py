from autotest.ui.pages.base_class import BaseClass
from autotest.ui.pages.disk_page.disk_page import DiskPage
from autotest.ui.pages.auth_page.auth_page import AuthPage


class TestDiskPage:

    def test_create_file_disk(self, browser):
        """Тест создания файла раздела 'Яндекс.Диск'"""
        main_page = BaseClass(browser)
        main_page.open_login_page()
        auth_page = AuthPage(browser)
        auth_page.login()
        disk_page = DiskPage(browser)
        disk_page.open_disk_page()
        disk_page.create_folder_disk()
        disk_page.create_file_disk()

    def test_upload_file_disk(self, browser):
        """Тест загрузки файла раздела 'Яндекс.Диск'"""
        main_page = BaseClass(browser)
        main_page.open_login_page()
        auth_page = AuthPage(browser)
        auth_page.login()
        disk_page = DiskPage(browser)
        disk_page.open_disk_page()
        disk_page.create_folder_disk()
        disk_page.upload_file_disk()