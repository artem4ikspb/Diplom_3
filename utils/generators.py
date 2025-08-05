from faker import Faker


class Generator:
    @staticmethod
    def generate_email():
        fake = Faker()
        return fake.email(domain='y.co')
    
    @staticmethod
    def generate_name():
        fake = Faker()
        return fake.name()
    
    @staticmethod
    def generate_password():
        fake = Faker()
        return fake.password()