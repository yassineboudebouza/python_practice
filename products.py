class Product :
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price 
        self.stock = stock 

    def restock(self ,quantity):
        if quantity >= 0 :
            self.stock += quantity
        else : 
            print("you cannot add a negative quantity")

    def reduce_stock(self , quantity):
        if quantity >= 0 and quantity <= self.stock  :
            self.stock -= quantity
        elif quantity < 0 :
            print("you cannot reduce a negative quantity")
        else :
            print("this quantity is not availlable in stock ")


class DigitalProduct(Product):

    def __init__(self, product_id, name, price, file_size_mb):
        super().__init__(product_id, name, price, stock="Unlimited")
        self.file_size_mb = file_size_mb

    def reduce_stock(self, quantity):
        print(f"the {self.name} is a digital product and has unlimited stock")
    