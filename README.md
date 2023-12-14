E-Commerce System
OOP Concepts Covered:
Encapsulation:
Use private attributes and methods.
Provide getter and setter methods.
Inheritance:
Derive Admin class from User class.
Polymorphism:
Implement polymorphic methods such as display_details() for both Product and User classes.
Abstraction:
Abstract common functionalities into methods (e.g., add_to_cart, process_order) in the Cart and Order classes.
Association:
Establish relationships between classes, such as the association between Cart, Product, and User.
Composition:
Utilize composition to create an Order class that contains instances of Product, User, and Payment classes.
Documentation:
User Class:
Methods:
__init__(self, user_id, name, email, password)

Initializes a new User instance.
Parameters:
user_id: Unique identifier for the user.
name: Name of the user.
email: Email address of the user.
password: Password for the user (hashed for security).
_hash_password(self, password)

Hashes the given password using the SHA-256 algorithm.
Parameters:
password: Plain text password.
Returns: Hashed password.
register(self)

Registers a new user by collecting information interactively from the user and appending the user to the list of users. The user data is then saved to a file.
No Parameters.
Returns: None.
login(self)

Allows a user to log in by entering their email and password. Validates the credentials against the stored hashed password.
No Parameters.
Returns: The logged-in user instance or None if login fails.
view_profile(self)

Displays the user's profile information.
No Parameters.
Returns: None.
_save_users_to_file(self)

Saves the list of users to a JSON file (users.json).
No Parameters.
Returns: None.
load_users_from_file()

Loads the list of users from the JSON file (users.json) during program startup.
No Parameters.
Returns: List of User instances.
Product Class:
Methods:
__init__(self, product_id, name, description, price, stock_quantity)

Initializes a new Product instance.
Parameters:
product_id: Unique identifier for the product.
name: Name of the product.
description: Description of the product.
price: Price of the product.
stock_quantity: Quantity of the product in stock.
display_details(self)

Displays details of the product.
No Parameters.
Returns: None.
_save_products_to_file(self)

Saves the list of products to a JSON file (products.json).
No Parameters.
Returns: None.
load_products_from_file()

Loads the list of products from the JSON file (products.json) during program startup.
No Parameters.
Returns: List of Product instances.
Cart Class:
Methods:
__init__(self, user)

Initializes a new Cart instance for a specific user.
Parameters:
user: User instance associated with the cart.
add_to_cart(self, product, quantity=1)

Adds a specified quantity of a product to the cart.
Parameters:
product: Product instance to be added.
quantity: Quantity of the product to be added (default is 1).
Returns: None.
remove_from_cart(self, product)

Removes a product from the cart.
Parameters:
product: Product instance to be removed.
Returns: None.
view_cart(self)

Displays the contents of the cart, including products and total price.
No Parameters.
Returns: None.
checkout(self)

Processes the checkout by creating an Order instance and appending it to the list of orders. Clears the cart.
No Parameters.
Returns: None.
Order Class:
Methods:
__init__(self, order_id, user, products, total_price, order_status="Pending")

Initializes a new Order instance.
Parameters:
order_id: Unique identifier for the order.
user: User instance placing the order.
products: List of product instances in the order.
total_price: Total price of the order.
order_status: Status of the order (default is "Pending").
process_order(self)

Processes the order, displaying information about the order.
No Parameters.
Returns: None.
Payment Class:
Methods:
__init__(self, order, payment_method, payment_status="Pending")

Initializes a new Payment instance.
Parameters:
order: Order instance associated with the payment.
payment_method: Method of payment.
payment_status: Status of the payment (default is "Pending").
process_payment(self)

Processes
