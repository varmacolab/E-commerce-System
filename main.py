import hashlib
import json
import os

class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self):
        new_user = User(
            user_id=len(users) + 1,
            name=input("Enter your name: "),
            email=input("Enter your email: "),
            password=self._hash_password(input("Create a password: "))
        )
        users.append(new_user)
        self._save_users_to_file()
        print("Registration successful!")

    def login(self):
        email = input("Enter your email: ")
        password = self._hash_password(input("Enter your password: "))

        user = next((user for user in users if user.email == email), None)

        if user and user.password == password:
            print(f"Welcome, {user.name}!")
            return user
        else:
            print("Invalid email or password. Please try again.")
            return None

    def view_profile(self):
        print(f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}")

    def _save_users_to_file(self):
        with open("users.json", "w") as file:
            user_data = [{"user_id": user.user_id, "name": user.name, "email": user.email, "password": user.password} for user in users]
            json.dump(user_data, file)

    @staticmethod
    def load_users_from_file():
        users = []
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                user_data = json.load(file)
                users = [User(user["user_id"], user["name"], user["email"], user["password"]) for user in user_data]
        return users


class Product:
    def __init__(self, product_id, name, description, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def display_details(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price}")

    def _save_products_to_file(self):
        with open("products.json", "w") as file:
            product_data = [{"product_id": product.product_id, "name": product.name, "description": product.description, "price": product.price, "stock_quantity": product.stock_quantity} for product in products]
            json.dump(product_data, file)

    @staticmethod
    def load_products_from_file():
        products = []
        if os.path.exists("products.json"):
            with open("products.json", "r") as file:
                product_data = json.load(file)
                products = [Product(product["product_id"], product["name"], product["description"], product["price"], product["stock_quantity"]) for product in product_data]
        return products


class Cart:
    def __init__(self, user):
        self.user = user
        self.products = []
        self.total_price = 0

    def add_to_cart(self, product, quantity=1):
        # Implement add to cart logic
        self.products.append((product, quantity))
        self.total_price += product.price * quantity

    def remove_from_cart(self, product):
        # Implement remove from cart logic
        for item in self.products:
            if item[0] == product:
                self.total_price -= item[0].price * item[1]
                self.products.remove(item)

    def view_cart(self):
        print(f"Cart for {self.user.name}:")
        for product, quantity in self.products:
            print(f"{product.name} x{quantity}")
        print(f"Total Price: ${self.total_price}")

    def checkout(self):
        # Implement checkout logic
        order = Order(len(orders) + 1, self.user, self.products, self.total_price)
        order.process_order()
        orders.append(order)
        self.products = []
        self.total_price = 0


class Order:
    def __init__(self, order_id, user, products, total_price, order_status="Pending"):
        self.order_id = order_id
        self.user = user
        self.products = products
        self.total_price = total_price
        self.order_status = order_status

    def process_order(self):
        # Implement order processing logic
        print(f"Order {self.order_id} processed for {self.user.name}. Total: ${self.total_price}. Status: {self.order_status}")

class Payment:
    def __init__(self, order, payment_method, payment_status="Pending"):
        self.order = order
        self.payment_method = payment_method
        self.payment_status = payment_status

    def process_payment(self):
        # Implement payment processing logic
        print(f"Payment processed for Order {self.order.order_id}. Method: {self.payment_method}. Status: {self.payment_status}")

class DiscountCoupon:
    def __init__(self, coupon_code, discount_percentage):
        self.coupon_code = coupon_code
        self.discount_percentage = discount_percentage

class Admin(User):
    def __init__(self, admin_id, name, email, password):
        super().__init__(admin_id, name, email, password)

    def add_product(self, product):
        # Implement add product logic
        products.append(product)

    def remove_product(self, product):
        # Implement remove product logic
        products.remove(product)

    def view_orders(self):
        # Implement view orders logic
        for order in orders:
            print(f"Order ID: {order.order_id}, User: {order.user.name}, Total: ${order.total_price}, Status: {order.order_status}")

    def apply_discount(self, order, discount_coupon):
        # Implement apply discount logic
        discount_amount = (discount_coupon.discount_percentage / 100) * order.total_price
        order.total_price -= discount_amount
        print(f"Discount of ${discount_amount} applied to Order {order.order_id}")



users = User.load_users_from_file()
products = Product.load_products_from_file()
orders = []

user1 = User(1, "John Doe", "john@example.com", "password123")
product1 = Product(101, "Laptop", "High-performance laptop", 999.99, 50)
cart = Cart(user1)
cart.add_to_cart(product1, 2)
cart.view_cart()
cart.checkout()

order1 = Order(1, user1, cart.products, cart.total_price)
payment1 = Payment(order1, "Credit Card")
order1.process_order()
payment1.process_payment()

admin1 = Admin(101, "Admin User", "admin@example.com", "adminpassword")
admin1.add_product(product1)
admin1.view_orders()
discount_coupon = DiscountCoupon("DISCOUNT123", 10)
admin1.apply_discount(order1, discount_coupon)