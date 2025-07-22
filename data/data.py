import allure
from utils.generators import Generator


class Payloads:

    @staticmethod
    @allure.step("Create user data")
    def generate_user_data():
        return {
            "email": Generator.generate_email(),
            "password": Generator.generate_password(),
            "name": Generator.generate_name(),
        }