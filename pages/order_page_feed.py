import allure

from locators.order_feed_page_locators import OrderFeedPageLocators as OFPL
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    
    @allure.step('Get last order')
    def select_last_order(self):
        self.direct_click(OFPL.ORDER_IN_FEED_LINK)

    @allure.step('Check modal window visibility')
    def is_order_modal_appear(self):
        return self.wait_for_visible(OFPL.ORDER_MODAL_CONTENTS_TITLE)
    
    @allure.step("Find order in feed")
    def find_order_in_order_list(self, order_number):
        return self.wait_for_clickable(OFPL.get_order_in_order_feed(order_number))
    
    @allure.step("Go to Constructor button")
    def click_constructor_button(self):
        self.direct_click(OFPL.CONSTRUCTOR_BUTTON)

    @allure.step("Get total complited orders")
    def get_total_orders_number(self):
        self.wait_for_clickable(OFPL.COMPLETE_TOTAL_ORDERS_COUNT)
        return self.wait_for_visible(OFPL.COMPLETE_TOTAL_ORDERS_COUNT).text

    @allure.step("Get daily order count")
    def get_daily_orders_number(self):
        self.wait_for_clickable(OFPL.COMPLETE_DAILY_ORDERS_COUNT)
        return self.wait_for_visible(OFPL.COMPLETE_DAILY_ORDERS_COUNT).text

    @allure.step("Get count orders in work")
    def get_order_number_in_work_list(self):
        self.wait_for_clickable(OFPL.ORDER_NUMBER_IN_WORK)
        return self.wait_for_visible(OFPL.ORDER_NUMBER_IN_WORK).text
