class BeautySalonSystem:

    salon_name = "Glow Beauty Studio"

    def __init__(self):

        self.customer = ""

        # Default services
        self.services = {
            "Nail Art": {"price": 1200, "slots": 5},
            "Bridal Makeup": {"price": 8000, "slots": 2},
            "Hair Styling": {"price": 1500, "slots": 6}
        }

        self.cart = {}

        # Admin credentials
        self.admin_username = "admin"
        self.admin_password = "1234"

    def set_customer(self):
        self.customer = input("Enter customer name: ")
        print("Welcome", self.customer)

    def show_services(self):

        print("\nAvailable Services:")
        for name, details in self.services.items():
            print(f"{name} | Price: {details['price']} | Slots: {details['slots']}")


    def book_service(self):

        service = input("Enter service name: ")

        if service in self.services:

            if self.services[service]["slots"] > 0:

                price = self.services[service]["price"]

                self.cart[service] = {"price": price}

                self.services[service]["slots"] -= 1

                print("Booking successful!")

            else:
                print("No slots available")

        else:
            print("Service not found")

    def view_cart(self):

        if not self.cart:
            print("No bookings")
            return

        print("\nYour Bookings:")
        for name, details in self.cart.items():
            print(name, "| Price:", details["price"])

    def generate_bill(self):

        if not self.cart:
            print("Cart empty")
            return

        print("\n===== BILL =====")
        total = 0

        for name, details in self.cart.items():
            print(name, "|", details["price"])
            total += details["price"]

        print("Total Amount:", total)
        print("================")

        self.cart = {}

    def admin_login(self):

        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        if username == self.admin_username and password == self.admin_password:
            print("Admin login successful")
            self.admin_menu()
        else:
            print("Wrong credentials")

    def admin_menu(self):

        while True:

            print("\n=== ADMIN MENU ===")
            print("1. Add New Service")
            print("2. View Services")
            print("3. Back")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_service()

            elif choice == "2":
                self.show_services()

            elif choice == "3":
                break

            else:
                print("Invalid choice")


    def add_service(self):

        name = input("Enter new service name: ")
        price = int(input("Enter price: "))
        slots = int(input("Enter slots: "))

        self.services[name] = {
            "price": price,
            "slots": slots
        }

        print("Service added successfully!")


system = BeautySalonSystem()

system.set_customer()

while True:

    print("\n===== MENU =====")
    print("1. Show Services")
    print("2. Book Service")
    print("3. View Bookings")
    print("4. Generate Bill")
    print("5. Admin Login")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.show_services()

    elif choice == "2":
        system.book_service()

    elif choice == "3":
        system.view_cart()

    elif choice == "4":
        system.generate_bill()

    elif choice == "5":
        system.admin_login()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice")