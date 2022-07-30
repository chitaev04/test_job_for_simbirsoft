from selenium.webdriver.common.by import By


class DiskPageLocators:
    """Компоненты страницы 'Диск'"""

    DISK_TITLE = (By.CSS_SELECTOR, '[class="listing-heading__title-inner"]')
    CREATE_BUTTON_DISK = (By.CSS_SELECTOR, '[class="Button2 Button2_view_raised Button2_size_m Button2_width_max"]')
    CREATE_POPUP_NAME = (By.CSS_SELECTOR, '[class="create-resource-popup-with-anchor__title"]')
    CREATE_FOLDER_BUTTON = (By.CSS_SELECTOR, '[aria-label="Папку"]')
    CREATE_FILE_BUTTON = (By.CSS_SELECTOR, '[aria-label="Текстовый документ"]')
    USER_MENU = (By.CSS_SELECTOR, '[class="avatar__image  avatar__image-server0"]')
    LOGOUT_USER_MENU = (By.CSS_SELECTOR, '[aria-label="Выйти"]')
    CREATE_TITLE = (By.CSS_SELECTOR, '[class="dialog__title"]')
    DIALOG_WRAP_FOLDER = (By.CSS_SELECTOR, '[class="dialog__wrap"]')
    CELL_BLOCK = (By.CSS_SELECTOR, '[class="Modal-Cell Modal-Cell_align_middle"]')
    FOLDER_TITLE = (By.CSS_SELECTOR, '[class="listing-heading__title listing-heading__title_interactive"]')
    TEXT_FROM_UPLOAD_FILE = (By.XPATH, '//div[@class="b1"]')
    NAME_INPUT = (By.CSS_SELECTOR, '[class="Textinput-Control"]')
    SAVE_DISK_BUTTON = (By.CSS_SELECTOR, '[class="Button2 Button2_view_action Button2_size_m confirmation-dialog__button'
                        ' confirmation-dialog__button_submit "]')
    FILE_DOC_TITLE = (By.CSS_SELECTOR, '[id="title-doc-name"]')
    UPLOAD_FILE_INPUT = (By.CSS_SELECTOR, '[class="upload-button__attach"]')
    IFRAME_LOC = (By.XPATH, '//iframe')
    NEW_UPLOAD_FILE = (By.XPATH, '//span[text()="doc.txt"]')
    LOAD_COMPLETE = (By.XPATH, '//button[@aria-label="Поделиться"]')
