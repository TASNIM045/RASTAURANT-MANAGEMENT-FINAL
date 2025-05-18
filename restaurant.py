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




print("\n\n")
print("*************Wellcome To The Restaurant*************")
print("1. Admin Login")
print("2. Customer Login")
print("3.Exit")

while(True):
    choice = int(input("Enter You Choice : "))
    if choice == 1:
        x = input("Enter Password : ")
        if x=='1221':
            print("Adim....")
    elif choice == 2:
        print("customer....")
    elif choice == 3:
        break
    else:
        print("Invalid Choice")