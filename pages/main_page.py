
import allure

from locators.main_page_locators import MainPageLocators as MPL
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @allure.step("Click button 'Войти в аккаунт'")
    def click_login_button(self):
        self.direct_click(MPL.LOGIN_BUTTON)

    @allure.step("Click button 'Войти в Личный кабинет'")
    def click_profile_button(self):
        self.direct_click(MPL.PROFILE_BUTTON)

    @allure.step("Вход в личный кабинет после авторизации")
    def go_to_profile_after_auth(self):
        self.direct_click(MPL.PROFILE_BUTTON)

    @allure.step("Click to 'Конструктор'")
    def click_constructor_button(self):
        self.direct_click(MPL.CONSTRUCTOR_BUTTON)

    @allure.step("Click to 'Лента Заказов'")
    def click_orders_feed_button(self):
        self.direct_click(MPL.ORDER_FEED_BUTTON)

