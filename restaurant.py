from abc import ABC

class User(ABC):
    def __init__(self,name,email,address):
        self.name = name
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
    


class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.password = "1221"
        self.menu_item = []
        self.customer = []

    def add_item(self, item, price):
        self.menu_item.append({"name": item, "price": price})
        print("Item Added!")

    def remove_item(self, item_name):
        self.menu_item = [item for item in self.menu_item if item["name"] != item_name]
        print("Item Removed")

    def show_menu(self):
        print("******* Menu ********")
        for item in self.menu_item:
            print(f"Item: {item['name']} ---- Price: ${item['price']}")

    def add_customer(self, customer):
        self.customer.append(customer)
        print("Added!")

    def remove_customer(self, customer):
        if customer in self.customer:
            self.customer.remove(customer)
            print(f"{customer} removed successfully.")
        else:
            print(f"{customer} not found in customer list.")

    def show_customers(self):
        print("******* Customers ********")
        for cust in self.customer:
            print(f"Customer: {cust}")




class Restaurent:
    def __init__(self,name):
        self.name = name




admin = Admin('Tasnim Rahman','tasnim01@gamil.com','Dhaka')




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
            while(True):
                print("\n")
                print("1. Add Item")
                print("2. Remove Item")
                print("3. Add Customer")
                print("4. Remove Customer")
                print("5. View Menu")
                print("6. View Customer")
                print("7. Exit")
                num = int(input("Enter Your Choice : "))

                if num == 1:
                    item = input("Enter the item name : ")
                    price = int(input("Enter the item price : "))
                    admin.add_item(item,price)
                elif num == 2:
                    item = input("Enter the item name : ")
                    admin.remove_item(item)
                elif num == 3:
                    name = input("Enter Name : ")
                    email = input("Enter Email : ")
                    address = input("Enter Address : ")
                    customer = Customer(name,email,address)
                    admin.add_customer(customer)
                elif num == 4:
                    name = input("Enter Name : ")
                    email = input("Enter Email : ")
                    address = input("Enter Address : ")
                    customer = Customer(name,email,address)
                    admin.remove_customer(customer)
                elif num == 5:
                    admin.show_menu()
                elif num == 6:
                    admin.show_customers()
                elif num == 7:
                    break
                else:
                    price("Invalid Choice!!")
        else:
            print("Encorrect Password!!!")
    elif choice == 2:
        print("customer....")
    elif choice == 3:
        break
    else:
        print("Invalid Choice")