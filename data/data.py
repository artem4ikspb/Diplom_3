import allure
from utils.generators import Generator


class Payloads:

    @staticmethod
    @allure.step("Создание данных пользователя")
    def generate_user_data():
        return {
            "email": Generator.generate_email(),
            "password": Generator.generate_password(),
            "name": Generator.generate_name(),
        }