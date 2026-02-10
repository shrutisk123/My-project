class CafeSystem:

    cafe_name = "Chai & Chill Cafe"

    def __init__(self):
        
        self.menu ={
            "Burger": {"price": 120, "stock": 10},
            "Pizza": {"price": 250, "stock": 8},
            "Cold Coffee": {"price": 150, "stock": 12},
            "Pasta": {"price": 180, "stock": 7},
        }

        self.cart = {}

        self.admin_user = "admin"
        self.admin_pass = "1234"

    def show_menu(self):
        print("\n===== MENU =====")
        for item, details in self.menu.items():
            print(f"{item} | Price: {details['price']} | Stock: {details['stock']}")
            
    def order_item(self):
        item = input("Enter item name: ")
        qty = int(input("Enter quantity:"))

        if item in self.menu:

            if self.menu[item]["stock"] >= qty:
                price = self.menu[item]["price"]

                if item in self.cart:
                    self.cart[item]["qty"] += qty
                else:
                    self.cart[item] = {"price": price, "qty": qty}

                self.menu[item] ["stock"] -= qty
                
                print("Item added to cart")
            else:
                print("Not enough stock")
        else:
            print("Item not found")
        
    def view_cart(self):

        if not self.cart:
            print("Cart empty")
            return
        print("\nYour Order:")
        for item,details in self.cart.items():
            print(f"{item} | {details['price']} x {details['qty']}")


    def remove_item(self):

        item = input("Enter item to remove:")

        if item in self.cart:

            qty =self.cart[item]["Qty"]
            self.menu[item]["stock"] += qty

            del self.cart[item]
            print("Item removed")

        else:
            print("Item not in cart")

    def generate_bill(self):

        if not self.cart:
            print("No order placed")
            return
        print("\n===== BILL =====")

        total = 0

        for item, details in self.cart.items():
            subtotal = details["price"] * details["qty"]
            print(f"{item} | {details['price']} x {details['qty']} = {subtotal}")
            total += subtotal

        gst = total * 0.05
        final = total = gst

        print("Subtotal:", total)
        print("GST (5%):", gst)
        print("Final Amount:", final)
        print("==================")

        self.cart = {}

    def admin_login(self):

        user = input("Username: ")
        password = input("Password: ")

        if user == self.admin_user and password == self.admin_pass:
            print("Admin login success")
            self.admin_menu()
        else:
            print("Wrong credentials")

    def admin_menu(self):

        while True:

            print("\n=== ADMIN MENU ===")
            print("1. Add New Menu Item")
            print("2. View Menu")
            print("3. Back")

            choice = input("Enter choice:")

            if choice == "1":
                self.add_menu_item()

            elif choice == "2":
                self.show_menu()

            elif choice == "3":
                break

    def add_menu_item(self):

        name = input("Enter item name:")
        price = int(input("Enter price:"))
        stock = int(input("Enter stock"))

        self.menu[name] = {"price": price, "stock": stock}

        print("Item added successfully!")


cafe = CafeSystem()
while True:

    print("\n======= CAFE MENU =======")
    print("1. Show Menu")
    print("2. Order Item")
    print("3. View Cart")
    print("4. Remove Item")
    print("5. Generate Bill")
    print("6. Admin Login") 
    print("7. Exit")

    choice = input("Enter choice: ")
    
    if choice == "1":
        cafe.show_menu()

    elif choice == "2":
        cafe.order_item()

    elif choice == "3":
        cafe.view_cart()

    elif choice == "4":
        cafe.remove_item()

    elif choice == "5":
        cafe.generate_bill()

    elif choice == "6":
        cafe.admin_login()

    elif choice == "6":
        cafe.admin_login()

    elif choice == "7":
        print("Thank you!")
        break 

    else:
        print("Invalid choice")
