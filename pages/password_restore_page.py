import allure

from locators.password_restore_page_locators import PasswordRestorePageLocators as PRPL
from pages.base_page import BasePage
from utils.generators import Generator


class PasswordRestorePage(BasePage):

    @allure.step("Ввод email и подтверждение восстановления пароля")
    def enter_email_and_confirm(self):
        self.direct_click(PRPL.EMAIL_FIELD)
        self.send_keys(PRPL.EMAIL_FIELD, Generator.generate_email())
        self.direct_click(PRPL.RESTORE_PASSWORD_BUTTON)
        self.wait_for_presence(PRPL.NEW_PASSWORD_CONFIRM_BUTTON)

    @allure.step("Нажатие на иконку отображения пароля")
    def click_shows_password_icon(self):
        self.click_on_element(PRPL.SHOW_PASSWORD_TOGGLE)

    @allure.step("Проверка, что поле пароля активно")
    def check_is_password_field_active(self):
        return self.check_displaying_of_element(PRPL.PASSWORD_FIELD_IS_ACTIVE)
