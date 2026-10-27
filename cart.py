from products import Product, DigitalProduct


class Cart:

    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.stock == "Unlimited" or quantity <= product.stock:
            self.items.append((product, quantity))
            product.reduce_stock(quantity)
            print(f"Added {quantity} of {product.name} to cart.")
        else:
            print(
                f"Cannot add {product.name}. Only {product.stock} available."
            )

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
            return

        print("\n--- Cart Content ---")
        for product, quantity in self.items:
            print(f"- {product.name} | Qty: {quantity} | Price: {product.price}")
        print(f"Total: {self.calculate_total()} DA\n")