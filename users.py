from cart import Cart


class Customer:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.cart = Cart()

    def checkout(self):
        print(f"Customer: {self.username}")
        self.cart.show_cart()


class VIPCustomer(Customer):

    def __init__(self, username, email, discount_rate):
        super().__init__(username, email)
        self.discount_rate = discount_rate

    def checkout(self):
        print(f"VIP Customer: {self.username}")
        self.cart.show_cart()
        total = self.cart.calculate_total()
        discounted_total = total * (1 - self.discount_rate)
        print(f"Discount: {int(self.discount_rate * 100)}%")
        print(f"Final Price after discount: {discounted_total} DA\n")