class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class OnlineShoppingSystem:
    def __init__(self):
        self.products = []
        self.total_income = 0
        self.admin_logged_in = False
        self.user_logged_in = False

    def admin_login(self):
        
        self.admin_logged_in = True

    def user_login(self):
        
        self.user_logged_in = True

    def display_menu(self):
        for i, product in enumerate(self.products):
            print(f"{i + 1}. {product.name} - ${product.price} - Available: {product.quantity}")

    def add_product(self, name, price, quantity):
        if self.admin_logged_in:
            self.products.append(Product(name, price, quantity))
            print("Product added successfully.")
        else:
            print("Admin login required.")

    def remove_product(self, index):
        if self.admin_logged_in:
            if 0 <= index < len(self.products):
                del self.products[index]
                print("Product removed successfully.")
            else:
                print("Invalid product index.")
        else:
            print("Admin login required.")

    def place_order(self, index, quantity):
        if self.user_logged_in:
            if 0 <= index < len(self.products):
                product = self.products[index]
                if product.quantity >= quantity:
                    total_price = product.price * quantity
                    self.total_income += total_price
                    product.quantity -= quantity
                    print(f"Order placed successfully. Total price: ${total_price}")
                else:
                    print("Insufficient quantity available.")
            else:
                print("Invalid product index.")
        else:
            print("User login required.")

    def logout(self):
        self.admin_logged_in = False
        self.user_logged_in = False
        print("Logged out successfully.")




shopping_system = OnlineShoppingSystem()


shopping_system.add_product("Laptop", 1000, 10)
shopping_system.add_product("Phone", 500, 20)
shopping_system.add_product("Headphones", 50, 30)


shopping_system.admin_login()


shopping_system.add_product("Tablet", 300, 15)


shopping_system.display_menu()


shopping_system.remove_product(2)


shopping_system.user_login()


shopping_system.place_order(0, 2)


shopping_system.display_menu()


shopping_system.logout()
