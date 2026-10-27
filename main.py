from products import Product, DigitalProduct
from cart import Cart
from users import Customer, VIPCustomer

# 1. إنشاء منتجات عادية ورقمية
phone = Product(product_id=1, name="Smartphone", price=50000, stock=5)
laptop = Product(product_id=2, name="Laptop", price=120000, stock=2)
python_course = DigitalProduct(product_id=3, name="Python Masterclass", price=4500, file_size_mb=1024)

# 2. إنشاء زبون عادي وتجربة السلة والشراء
print("--- TEST REGULAR CUSTOMER ---")
customer1 = Customer(username="Ahmed", email="ahmed@email.com")

# إضافة منتجات للسلة
customer1.cart.add_product(phone, 2)
customer1.cart.add_product(python_course, 1)

# إتمام الشراء (Checkout)
customer1.checkout()


# 3. إنشاء زبون VIP وتجربة السلة مع الخصم
print("\n--- TEST VIP CUSTOMER ---")
customer2 = VIPCustomer(username="Karim", email="karim@email.com", discount_rate=0.2) # خصم 20%

# إضافة منتجات للسلة
customer2.cart.add_product(laptop, 1)
customer2.cart.add_product(python_course, 2)

# إتمام الشراء مع الخصم
customer2.checkout()