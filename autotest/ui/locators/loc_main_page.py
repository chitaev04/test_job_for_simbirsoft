from selenium.webdriver.common.by import By


class MainPageLocators:
    """Компоненты главной страницы"""

    AUTH_BUTTON = (By.CSS_SELECTOR,
                   '[class="home-link desk-notif-card__login-new-item desk-notif-card__login-new-item_enter home-link_'
                   'black_yes home-link_hover_inherit"]')
    USERNAME_DESK_CARD = (By.CSS_SELECTOR, '[class="username desk-notif-card__user-name "]')
    DISK_BUTTON = (By.CSS_SELECTOR, '[class="home-link home-link_black_yes"]')
