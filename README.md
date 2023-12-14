# Project: E-Commerce System

## Classes:

### User:

Attributes: User ID, Name, Email, Password
Methods: Register, Login, View Profile

### Product:

Attributes: Product ID, Name, Description, Price, Stock Quantity
Methods: Display product details

### Cart:

Attributes: User, List of Products, Total Price
Methods: Add product to cart, Remove product from cart, View cart, Checkout

### Order:

Attributes: Order ID, User, List of Products, Total Price, Order Status (e.g., Pending, Shipped)

### Payment:

Attributes: Order, Payment Method, Payment Status (e.g., Paid, Pending)

### DiscountCoupon:

Attributes: Coupon Code, Discount Percentage

### Admin:

Attributes: Admin ID, Name, Email, Password
Methods: Add Product, Remove Product, View Orders, Apply Discount

## OOP Concepts Covered:

### Encapsulation:

- Use private attributes and methods.
- Provide getter and setter methods.

### Inheritance:

- Derive Admin class from User class.

### Polymorphism:

- Implement polymorphic methods such as `display_details()` for both Product and User classes.

### Abstraction:

- Abstract common functionalities into methods (e.g., `add_to_cart`, `process_order`) in the Cart and Order classes.

### Association:

- Establish relationships between classes, such as the association between Cart, Product, and User.

### Composition:

- Utilize composition to create an Order class that contains instances of Product, User, and Payment classes.

## Documentation:

### `User` Class:

#### Methods:

1. **`__init__(self, user_id, name, email, password)`**
   - *Description*: Initializes a new User instance.
   - *Parameters*:
     - `user_id`: Unique identifier for the user.
     - `name`: Name of the user.
     - `email`: Email address of the user.
     - `password`: Password for the user (hashed for security).

2. **`_hash_password(self, password)`**
   - *Description*: Hashes the given password using the SHA-256 algorithm.
   - *Parameters*:
     - `password`: Plain text password.
   - *Returns*: Hashed password.

3. **`register(self)`**
   - *Description*: Registers a new user by collecting information interactively from the user and appending the user to the list of users. The user data is then saved to a file.
   - *Parameters*: None.
   - *Returns*: None.

4. **`login(self)`**
   - *Description*: Allows a user to log in by entering their email and password. Validates the credentials against the stored hashed password.
   - *Parameters*: None.
   - *Returns*: The logged-in user instance or None if login fails.

5. **`view_profile(self)`**
   - *Description*: Displays the user's profile information.
   - *Parameters*: None.
   - *Returns*: None.

6. **`_save_users_to_file(self)`**
   - *Description*: Saves the list of users to a JSON file (`users.json`).
   - *Parameters*: None.
   - *Returns*: None.

7. **`load_users_from_file()`**
   - *Description*: Loads the list of users from the JSON file (`users.json`) during program startup.
   - *Parameters*: None.
   - *Returns*: List of User instances.

### `Product` Class:

#### Methods:

1. **`__init__(self, product_id, name, description, price, stock_quantity)`**
   - *Description*: Initializes a new Product instance.
   - *Parameters*:
     - `product_id`: Unique identifier for the product.
     - `name`: Name of the product.
     - `description`: Description of the product.
     - `price`: Price of the product.
     - `stock_quantity`: Quantity of the product in stock.

2. **`display_details(self)`**
   - *Description*: Displays details of the product.
   - *Parameters*: None.
   - *Returns*: None.

3. **`_save_products_to_file(self)`**
   - *Description*: Saves the list of products to a JSON file (`products.json`).
   - *Parameters*: None.
   - *Returns*: None.

4. **`load_products_from_file()`**
   - *Description*: Loads the list of products from the JSON file (`products.json`) during program startup.
   - *Parameters*: None.
   - *Returns*: List of Product instances.

### `Cart` Class:

#### Methods:

1. **`__init__(self, user)`**
   - *Description*: Initializes a new Cart instance for a specific user.
   - *Parameters*:
     - `user`: User instance associated with the cart.

2. **`add_to_cart(self, product, quantity=1)`**
   - *Description*: Adds a specified quantity of a product to the cart.
   - *Parameters*:
     - `product`: Product instance to be added.
     - `quantity`: Quantity of the product to be added (default is 1).
   - *Returns*: None.

3. **`remove_from_cart(self, product)`**
   - *Description*: Removes a product from the cart.
   - *Parameters*:
     - `product`: Product instance to be removed.
   - *Returns*: None.

4. **`view_cart(self)`**
   - *Description*: Displays the contents of the cart, including products and total price.
   - *Parameters*: None.
   - *Returns*: None.

5. **`checkout(self)`**
   - *Description*: Processes the checkout by creating an Order instance and appending it to the list of orders. Clears the cart.
   - *Parameters*: None.
   - *Returns*: None.

### `Order` Class:

#### Methods:

1. **`__init__(self, order_id, user, products, total_price, order_status="Pending")`**
   - *Description*: Initializes a new Order instance.
   - *Parameters*:
     - `order_id`: Unique identifier for the order.
     - `user`: User instance placing the order.
     - `products`: List of product instances in the order.
     - `total_price`: Total price of the order.
     - `order_status`: Status of the order (default is "Pending").

2. **`process_order(self)`**
   - *Description*: Processes the order, displaying information about the order.
   - *Parameters*: None.
   - *Returns*: None.

### `Payment` Class:

#### Methods:

1. **`__init__(self, order, payment_method, payment_status="Pending")`**
   - *Description*: Initializes a new Payment instance.
   - *Parameters*:
     - `order`: Order instance associated with the payment.
     - `payment_method`: Method of payment.
     - `payment_status`: Status of the payment (default is "Pending").

2. **`process_payment(self)`**
   - *Description*: Processes the payment, displaying information about the payment.
   - *Parameters*: None.
   - *Returns*: None.

### `DiscountCoupon` Class:

#### Methods:

1. **`__init__(self, coupon_code, discount_percentage)`**
   - *Description*: Initializes a new DiscountCoupon instance.
   - *Parameters*:
     - `coupon_code`: Code for the discount coupon.
     - `discount_percentage`: Percentage of discount offered by the coupon.

### `Admin` Class:

#### Methods:

1. **`__init__(self, admin_id, name, email, password)`**
   - *Description*: Initializes a new Admin instance, inheriting from the User class.
   - *Parameters*:
     - `admin_id`: Unique identifier for the admin.
     - `name`: Name of the admin.
     - `email`: Email address of the admin.
     - `password`: Password for the admin (hashed for security).

2. **`add_product(self, product)`**
   - *Description*: Adds a product to the list of products.
   - *Parameters*:
     - `product`: Product instance to be added.
   - *Returns*: None.

3. **`remove_product(self, product)`**
   - *Description*: Removes a product from the list of products.
   - *Parameters*:
     - `product`: Product instance to be removed.
   - *Returns*: None.

4. **`view_orders(self)`**
   - *Description*: Displays information about all orders.
   - *Parameters*: None.
   - *Returns*: None.

5. **`apply_discount(self, order, discount_coupon)`**
   - *Description*: Applies a discount to a specific order.
   - *Parameters*:
     - `order`: Order instance to which the discount is applied.
     - `discount_coupon`: Discount coupon to be applied.
