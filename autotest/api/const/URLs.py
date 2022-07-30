MAIN_PAGE_URL = "http://yandex.ru"
PASSPORT_YANDEX = "https://passport.yandex.ru"
DISK_YANDEX = "https://disk.yandex.ru/models"
URL_FOLDER = "https://cloud-api.yandex.net/v1/disk/resources"
AUTH_PAGE_URL = f"{PASSPORT_YANDEX}/auth?origin=home_yandexid&retpath=https%3A%2F%2Fyandex.ru&backpath=https%3A%2F%2Fyandex.ru"
START_LOGIN_URL = f"{PASSPORT_YANDEX}/registration-validations/auth/multi_step/start"
COMMIT_PASSWORD_URL = f"{PASSPORT_YANDEX}/registration-validations/auth/multi_step/commit_password"
URL_ACCOUNTS = f"{PASSPORT_YANDEX}/registration-validations/auth/accounts"
URL_LOGOUT = f"{PASSPORT_YANDEX}/passport?mode=embeddedauth&action=logout&yu=1808144151658770411&uid=1665048185&origin=&retpath=https%3A%2F%2Fdisk.yandex.ru%2Fclient%2Fdisk&"
URL_CREATE_FOLDER = f"{DISK_YANDEX}/?_m=do-resource-create-folder"
URL_DELETE_FOLDER = f"{DISK_YANDEX}/?_m=do-resource-delete"

CHECK_FOLDER_NAME = "https://cloud-api.yandex.net/v1/disk/resources?path="

