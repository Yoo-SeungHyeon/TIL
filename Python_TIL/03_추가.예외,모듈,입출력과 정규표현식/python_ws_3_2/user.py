# 왜 되다가 안되다가 하는걸까?

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_data(self):
        print(f'Name: {self.name}, Email: {self.email}')

