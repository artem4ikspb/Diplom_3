import allure
from locators.account_page_locators import AccountPageLocators as APL
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step("Click order history")
    def click_order_history_menu(self):
        self.wait_for_visible(APL.ORDER_HISTORY_LINK)
        self.direct_click(APL.ORDER_HISTORY_LINK)

    @allure.title("Click logout")
    def logout_from_account(self):
        self.direct_click(APL.LOGOUT_BUTTON)
        self.wait_for_invisibility(APL.LOGOUT_BUTTON)
