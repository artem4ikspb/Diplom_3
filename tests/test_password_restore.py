import allure

from data.urls import Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_restore_page import PasswordRestorePage


@allure.feature("Тест восстановления пароля")
class TestPasswordRestore:

    @allure.title("Переход на страницу сброса пароля")
    def test_navigate_to_password_recovery_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.click_login_button()
        page = LoginPage(browser)
        page.go_to_restore_password_link()
        assert page.current_url() == Urls.RESTORE_PASSWORD_URl, f"{page.current_url()}< URL Не совпадает с ожидаемым"

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_enter_email_and_click_restore_button(self, browser):
        page = MainPage(browser)
        page.open()
        page.click_login_button()
        page = LoginPage(browser)
        page.go_to_restore_password_link()
        page = PasswordRestorePage(browser)
        page.enter_email_and_confirm()
        assert page.current_url() == Urls.RESET_PASSWORD_URL, f"{page.current_url()}< URL Не совпадает с ожидаемым"

    @allure.title("Нажатие на кнопку показать/скрыть пароль")
    def test_click_show_password_highlights_input_field(self, browser):
        page = MainPage(browser)
        page.open()
        page.click_login_button()
        page = LoginPage(browser)
        page.go_to_restore_password_link()
        page = PasswordRestorePage(browser)
        page.enter_email_and_confirm()
        page.click_shows_password_icon()
        assert page.check_is_password_field_active(), "Поле не 'пароль' не активно"

