import allure

from locators.login_page_locators import LoginPageLocators as LPL
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Click to reset password")
    def go_to_restore_password_link(self):
        self.click(LPL.RESTORE_PASSWORD_LINK)

    @allure.step("User Authorization")
    def login_profile(self, email, password):
        self.send_keys(LPL.EMAIL_FIELD, email)
        self.send_keys(LPL.PASSWORD_FIELD, password)
        self.forse_click(LPL.ENTER_BUTTON)
        self.wait_for_invisibility(LPL.ENTER_BUTTON)