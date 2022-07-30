from autotest.ui.pages.auth_page.auth_page_actions import AuthPageActions


class AuthPage(AuthPageActions):

    def login(self):
        """Авторизация"""
        self.open_auth_page()
        self.fill_login_input()
        self.click_login_button(check_password_fill=True)
        self.fill_password_input()
        self.click_login_button()

