from abc import ABC

class User(ABC):
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone