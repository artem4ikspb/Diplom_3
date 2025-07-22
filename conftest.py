import pytest

from selenium import webdriver
from data.data import Payloads
from utils.api_client import APIClient
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


@pytest.fixture(params=["Chrome", "Firefox"])
def browser(request):
    if request.param == "Chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    yield browser
    browser.quit()


@pytest.fixture
def create_user():
    data = Payloads.generate_user_data()
    _, response = APIClient.create_user(data)
    yield response, data
    APIClient.delete_user(headers={"Authorization": response["accessToken"]})


@pytest.fixture
def login_user(browser, create_user):
    _, data = create_user
    page = MainPage(browser)
    page.open()
    page.press_profile_button()
    page = LoginPage(browser)
    page.login_in_profile(email= data["email"], password= data["password"])


@pytest.fixture
def create_order(browser, login_user):
    page = ConstructorPage(browser)
    return page.create_an_order()