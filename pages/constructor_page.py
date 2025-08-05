import allure
from locators.constructor_page_locators import ConstructorPageLocators as CPL
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step("Click to BUN")
    def select_ingredient_bun(self):
        self.direct_click(CPL.INGREDIENT_BUN)

    @allure.step("Check modal window 'Детали ингредиента'")
    def check_details_modal_window_appear(self):
        return self.wait_for_presence(CPL.INGREDIENT_DETAILS_MODAL_TITLE)

    @allure.step("Close modal window 'Детали ингредиента'")
    def close_details_modal_window(self):
        self.click(CPL.MODAL_CLOSE_BUTTON)
        return self.wait_for_invisibility(CPL.INGREDIENT_DETAILS_MODAL_TITLE)

    @allure.step("Add BUN to the cart")
    def add_bun_to_order_cart(self):
        source_elem = self.find(CPL.INGREDIENT_BUN)
        target_elem = self.find(CPL.ORDER_CART)
        self.drag_and_drop_element(source_elem, target_elem)

    @allure.step("Check count of ingredients")
    def count_number_of_ingredients(self):
        return self.find(CPL.INGREDIENT_COUNTER).text

    @allure.step("Create order")
    def create_an_order(self):
        self.wait_for_clickable(CPL.INGREDIENT_BUN)
        bun_elem = self.find(CPL.INGREDIENT_BUN)
        cart_elem = self.find(CPL.ORDER_CART)
        self.drag_and_drop_element(bun_elem, cart_elem)
        sause_elem = self.find(CPL.INGREDIENT_SAUCE)
        self.drag_and_drop_element(sause_elem, cart_elem)
        filling_elem = self.find(CPL.INGREDIENT_FILLING)
        self.drag_and_drop_element(filling_elem, cart_elem)
        self.direct_click(CPL.ORDER_CREATE_BUTTON)
        self.wait_for_clickable(CPL.ORDER_MODAL_FRAME)
        self.wait_for_invisibility(CPL.DEFAULT_ORDER_NUMBER)
        self.wait_for_visible(CPL.ORDER_IS_PREPARING_TEXT)
        order_number = self.wait_for_clickable(CPL.REAL_ORDER_NUMBER).text
        self.direct_click(CPL.CLOSE_ORDER_MENU_BUTTON)
        return order_number

    @allure.step("Check create order window")
    def is_order_confirmation_modal_appear(self):
        return self.wait_for_visible(CPL.ORDER_IS_PREPARING_TEXT)

    @allure.step("Click on button 'Лента Заказов'")
    def click_orders_feed_button(self):
        self.direct_click(CPL.ORDER_FEED_BUTTON)
