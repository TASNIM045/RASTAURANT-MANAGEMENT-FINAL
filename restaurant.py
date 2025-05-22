from abc import ABC

class User(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.balance = 0
        self.orders = []

    def view_menu(self, menu):
        print("******* Menu ********")
        if not menu:
            print("No items in the menu.")
        for item in menu:
            print(f"{item['name']} - ${item['price']}")

    def add_funds(self, amount):
        self.balance += amount
        print(f"${amount} added to your balance. Current Balance: ${self.balance}")

    def check_balance(self):
        print(f"Current Balance: ${self.balance}")

    def place_order(self, menu):
        self.view_menu(menu)
        order = input("Enter item name to order: ")
        for item in menu:
            if item['name'].lower() == order.lower():
                if self.balance >= item['price']:
                    self.balance -= item['price']
                    self.orders.append(item)
                    print(f"Ordered {item['name']} for ${item['price']}. Remaining Balance: ${self.balance}")
                else:
                    print("Insufficient Balance.")
                return
        print("Item not found in menu.")

    def view_orders(self):
        if not self.orders:
            print("No past orders.")
        else:
            print("Past Orders:")
            for item in self.orders:
                print(f"{item['name']} - ${item['price']}")

class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.password = "1221"
        self.menu_item = []
        self.customers = []

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
            print(f"{item['name']} - ${item['price']}")

    def add_customer(self, name, email, address):
        customer = Customer(name, email, address)
        self.customers.append(customer)
        print("Customer Added!")

    def remove_customer(self, name):
        for cust in self.customers:
            if cust.name == name:
                self.customers.remove(cust)
                print(f"{cust.name} removed successfully.")
                return
        print("Customer not found.")

    def show_customers(self):
        print("******* Customers ********")
        if not self.customers:
            print("No customers found.")
        for cust in self.customers:
            print(f"{cust.name}, {cust.email}, {cust.address}")

    def get_customer(self, name):
        for cust in self.customers:
            if cust.name == name:
                return cust
        return None

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.admin = Admin('Tasnim Rahman', 'tasnim01@gmail.com', 'Dhaka')

    def run(self):
        print("\n************* Welcome To The Restaurant *************")
        while True:
            print("\n1. Admin Login")
            print("2. Customer Login")
            print("3. Exit")
            choice = input("Enter Your Choice: ")
            if choice == '1':
                password = input("Enter Admin Password: ")
                if password == self.admin.password:
                    while True:
                        print("\n1. Add Item")
                        print("2. Remove Item")
                        print("3. Add Customer")
                        print("4. Remove Customer")
                        print("5. View Menu")
                        print("6. View Customers")
                        print("7. Exit")
                        option = input("Enter Your Choice: ")
                        if option == '1':
                            name = input("Enter Item Name: ")
                            price = float(input("Enter Item Price: "))
                            self.admin.add_item(name, price)
                        elif option == '2':
                            name = input("Enter Item Name to Remove: ")
                            self.admin.remove_item(name)
                        elif option == '3':
                            name = input("Name: ")
                            email = input("Email: ")
                            address = input("Address: ")
                            self.admin.add_customer(name, email, address)
                        elif option == '4':
                            name = input("Enter Name to Remove: ")
                            self.admin.remove_customer(name)
                        elif option == '5':
                            self.admin.show_menu()
                        elif option == '6':
                            self.admin.show_customers()
                        elif option == '7':
                            break
                        else:
                            print("Invalid Option.")
                else:
                    print("Incorrect Password.")
            elif choice == '2':
                name = input("Enter Your Name: ")
                customer = self.admin.get_customer(name)
                if customer:
                    while True:
                        print("\n1. View Menu")
                        print("2. Check Balance")
                        print("3. Add Funds")
                        print("4. Place Order")
                        print("5. View Past Orders")
                        print("6. Exit")
                        option = input("Enter Your Choice: ")
                        if option == '1':
                            customer.view_menu(self.admin.menu_item)
                        elif option == '2':
                            customer.check_balance()
                        elif option == '3':
                            amount = float(input("Enter Amount to Add: "))
                            customer.add_funds(amount)
                        elif option == '4':
                            customer.place_order(self.admin.menu_item)
                        elif option == '5':
                            customer.view_orders()
                        elif option == '6':
                            break
                        else:
                            print("Invalid Option.")
                else:
                    print("Customer not found. Contact admin to create an account.")
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid Choice.")

restaurant = Restaurant("Foodie's Heaven")
restaurant.run()