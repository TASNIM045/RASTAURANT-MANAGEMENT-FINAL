from abc import ABC

class User(ABC):
    def __init__(self,name,email,address):
        self.name = name
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)


class Adimin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.password = "1221"

    def add_item(self,item):
        pass
    def remove_item(self,item):
        pass
    def add_customar(self,customer):
        pass
    def remove_customer(self,customer):
        pass


class Restaurent:
    def __init__(self,name):
        self.name = name