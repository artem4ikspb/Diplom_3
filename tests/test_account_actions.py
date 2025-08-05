import allure

from data.urls import Urls
from pages.account_page import AccountPage
from pages.main_page import MainPage


@allure.feature("Test user account")
class TestPersonalAccount:

    @allure.title("Переход в Личный кабинет по клику на 'Личный кабинет'")
    def test_load_profile_from_main_page(self, browser, login_user):
        page = MainPage(browser)
        page.click_profile_button()
        assert page.current_url() == Urls.USER_ACCOUNT_URL

    @allure.title("Переход в раздел 'История заказов' из профиля")
    def test_load_order_history_from_profile(self, browser, login_user):
        page = MainPage(browser)
        page.click_profile_button()
        page = AccountPage(browser)
        page.click_order_history_menu()
        assert page.current_url() == Urls.USER_ACCOUNT_HISTORY_URL

    @allure.title("Выход из аккаунта через личный кабинет")
    def test_logout_from_profile_page(self, browser, login_user):
        page = MainPage(browser)
        page.click_profile_button()
        page = AccountPage(browser)
        page.logout_from_account()
        assert page.current_url() == Urls.LOGIN_PAGE_URL
