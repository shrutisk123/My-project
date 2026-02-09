class BeautyStore:

    store_name = "Glow Beauty Store"

    def __init__(self):

        self.products = {
            "Lipstick": {"price": 499, "quantity": 10},
            "Face Wash": {"price": 299, "quantity": 15},
            "Perfume": {"price": 999, "quantity": 5},
            "Foundation": {"price": 799, "quantity": 8}
        }

        self.cart = {}

    def show_products(self):
        print("\nAvailable Products:")
        for name, details in self.products.items():
            print(name, "| Price:", details["price"], "| Qty:", details["quantity"])

    # Add item to cart
    def add_to_cart(self):
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))

        if name in self.products:
            if self.products[name]["quantity"] >= qty:

                price = self.products[name]["price"]
                self.cart[name] = {"price": price, "quantity": qty}

                self.products[name]["quantity"] -= qty
                print("Added to cart")

            else:
                print("Not enough stock")
        else:
            print("Product not found")

    # Generate bill
    def generate_bill(self):

        print("\n===== BILL =====")
        total = 0

        for name, details in self.cart.items():
            price = details["price"]
            qty = details["quantity"]
            subtotal = price * qty

            print(name, "|", price, "x", qty, "=", subtotal)
            total += subtotal

        print("Total Amount:", total)
        print("================")

        # clear cart after billing
        self.cart = {}


# Create object
store = BeautyStore()

# Menu
while True:
    print("\n==== Beauty Store Menu ====")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. Generate Bill")
    print("4. Exit")

    choice = input("Enter choice: ")


    if choice == "1":
        store.show_products()

    elif choice == "2":
        store.add_to_cart()

    elif choice == "3":
        store.generate_bill()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")