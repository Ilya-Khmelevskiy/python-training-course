from user import User
from privileges import Privileges


class Admin(User):
    def __init__(self, login, password, f_name, l_name):
        super().__init__(login, password, f_name, l_name)
        self.role = ['admin', 'user']
        self.privileges = Privileges(['qeqwe', 'wqeqweqwe', 'sdfsdfs'])
