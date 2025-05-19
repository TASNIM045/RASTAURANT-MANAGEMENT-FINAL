from abc import ABC

class User(ABC):
    def __init__(self, name, email, address):
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
        print("Item Removed!")

    def show_menu(self):
        print("******* Menu ********")
        if not self.menu_item:
            print("No items in the menu.")
        for item in self.menu_item:
            print(f"Item: {item['name']} ---- Price: ${item['price']}")

    def add_customer(self, name, email, address):
        customer = Customer(name, email, address)
        self.customer.append(customer)
        print("Customer Added!")

    def remove_customer(self, name):
        for cust in self.customer:
            if cust.name == name:
                self.customer.remove(cust)
                print(f"{cust.name} removed successfully.")
                return
        print("Customer not found.")

    def show_customers(self):
        print("******* Customers ********")
        if not self.customer:
            print("No customers found.")
        for cust in self.customer:
            print(f"Name: {cust.name}, Email: {cust.email}, Address: {cust.address}")

class Restaurent:
    def __init__(self, name):
        self.name = name

admin = Admin('Tasnim Rahman', 'tasnim01@gmail.com', 'Dhaka')

print("\n\n")
print("************* Welcome To The Restaurant *************")
print("1. Admin Login")
print("2. Customer Login")
print("3. Exit")

while True:
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        x = input("Enter Password: ")
        if x == '1221':
            while True:
                print("\n")
                print("1. Add Item")
                print("2. Remove Item")
                print("3. Add Customer")
                print("4. Remove Customer")
                print("5. View Menu")
                print("6. View Customers")
                print("7. Exit")
                num = int(input("Enter Your Choice: "))

                if num == 1:
                    item = input("Enter the item name: ")
                    price = int(input("Enter the item price: "))
                    admin.add_item(item, price)
                elif num == 2:
                    item = input("Enter the item name: ")
                    admin.remove_item(item)
                elif num == 3:
                    name = input("Enter Name: ")
                    email = input("Enter Email: ")
                    address = input("Enter Address: ")
                    admin.add_customer(name, email, address)
                elif num == 4:
                    name = input("Enter Name to remove: ")
                    admin.remove_customer(name)
                elif num == 5:
                    admin.show_menu()
                elif num == 6:
                    admin.show_customers()
                elif num == 7:
                    print("\nReturning to main menu...\n")
                    print("************* Welcome To The Restaurant *************")
                    print("1. Admin Login")
                    print("2. Customer Login")
                    print("3. Exit")
                    break
                else:
                    print("Invalid Choice!!")
        else:
            print("Incorrect Password!!!")
    elif choice == 2:
        print("Customer login feature not implemented yet.")
    elif choice == 3:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid Choice")
