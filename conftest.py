import pytest

from data.data import Payloads
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils.api_client import APIClient


@pytest.fixture(params=["Chrome", "Firefox"])
def browser(request):
    if request.param == "Chrome":
        browser_options = ChromeOptions()
        browser_options.add_argument("--headless")
        browser_options.add_argument('--disable-default-apps')
        browser_options.add_argument("--disable-extensions")
        browser_options.add_argument('--window-size=1280, 1024')
        browser = webdriver.Chrome(options=browser_options)
    else:
        browser_options = FirefoxOptions()
        browser_options.add_argument("--headless")
        browser_options.add_argument('--disable-default-apps')
        browser_options.add_argument("--disable-extensions")
        browser_options.add_argument('--window-size=1280, 1024')
        browser = webdriver.Firefox(options=browser_options)
    # browser.set_window_size(1280, 1024)
    yield browser
    browser.quit()


@pytest.fixture
def create_user():
    data = Payloads.generate_user_data()
    code, response = APIClient.create_user(data)
    yield response, data
    APIClient.delete_user(headers={"Authorization": response["accessToken"]})


@pytest.fixture
def login_user(browser, create_user):
    code, data = create_user
    page = MainPage(browser)
    page.open()
    page.click_profile_button()
    page = LoginPage(browser)
    page.login_profile(email= data["email"], password= data["password"])


@pytest.fixture
def create_order(browser, login_user):
    page = ConstructorPage(browser)
    return page.create_an_order()