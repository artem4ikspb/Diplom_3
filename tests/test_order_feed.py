import allure
from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage
from pages.order_page_feed import OrderFeedPage


@allure.feature("Проверка ленты заказов»")
class TestOrderFeed:

    @allure.title("Проверка всплывающего окна с деталями")
    def test_get_order_in_popup(self, browser):
        page = MainPage(browser)
        page.open()
        page.click_orders_feed_button()
        page = OrderFeedPage(browser)
        page.select_last_order()
        assert page.is_order_modal_appear(), "Окно с деталями не появилось"

    @allure.title("Заказы из история есть на странице в ленте заказов")
    def test_user_order_in_feed(self, browser, create_order):
        order_number = f"#0{create_order}"
        page = MainPage(browser)
        page.open()
        page.click_orders_feed_button()
        page = OrderFeedPage(browser)
        assert page.find_order_in_order_list(order_number=order_number), f"Заказ {order_number}, не найден"

    @allure.title("Проверка общего счетчика заказов")
    def test_total_orders_count(self, browser, login_user):
        page = MainPage(browser)
        page.open()
        page.click_orders_feed_button()
        page = OrderFeedPage(browser)
        total_orders = page.get_total_orders_number()
        page.click_constructor_button()
        page = ConstructorPage(browser)
        page.create_an_order()
        page.click_orders_feed_button()
        page = OrderFeedPage(browser)
        new_total_orders = page.get_total_orders_number()
        assert new_total_orders > total_orders, "Общее кол-во заказов не изменилось"

    @allure.title("Проверка работы счетчика заказов на сегодня")
    def test_check_work_daily_order_count(self, browser, login_user):
        page = MainPage(browser)
        page.open()
        page.click_orders_feed_button()
        page = OrderFeedPage(browser)
        total_orders = page.get_daily_orders_number()
        page.click_constructor_button()
        page = ConstructorPage(browser)
        page.create_an_order()
        page.click_orders_feed_button()
        page = OrderFeedPage(browser)
        new_total_orders = page.get_daily_orders_number()
        assert new_total_orders > total_orders, "Количество заказов на сегодня не изменилось"

    @allure.title("Оформление заказа и его номера 'В работе'")
    def test_create_order_and_check_number_in_work_list(self, browser, login_user):
        page = ConstructorPage(browser)
        order_number = page.create_an_order()
        page.click_orders_feed_button()
        page = OrderFeedPage(browser)
        order_in_work = page.get_order_number_in_work_list()
        assert order_number > order_in_work, "Заказ в 'в работе' не найден"
