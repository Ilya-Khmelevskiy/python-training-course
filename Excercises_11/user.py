import uuid


class User:
    def __init__(self, login, password, f_name, l_name):
        self.login = login
        self.password = password
        self.id = uuid.uuid4()
        self.address = ''
        self.city = ''
        self.company_name = ''
        self.current_status = 'available'
        self.email = ''
        self.first_name = f_name
        self.last_name = l_name

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greer_user(self):
        print(f"Hi {self.first_name}! How are you?")
