
import allure

from locators.main_page_locators import MainPageLocators as MPL
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @allure.step("Click button 'Войти в аккаунт'")
    def press_login_button(self):
        self.click(MPL.LOGIN_BUTTON)

    @allure.step("Click button 'Войти в Личный кабинет'")
    def press_profile_button(self):
        self.forse_click(MPL.PROFILE_BUTTON)

    @allure.step("Go to profile")
    def go_to_profile(self):
        self.forse_click(MPL.PROFILE_BUTTON)

    @allure.step("Click to 'Конструктор'")
    def go_to_constructor_button(self):
        self.click(MPL.CONSTRUCTOR_BUTTON)

    @allure.step("Click to 'Лента Заказов'")
    def go_to_orders_feed_button(self):
        self.forse_click(MPL.ORDER_FEED_BUTTON)
