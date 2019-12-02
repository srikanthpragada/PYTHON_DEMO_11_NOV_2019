class Product:
    # static attributes / class attributes
    taxrate = 0.15

    @staticmethod
    def set_taxrate(newtaxrate):
        Product.taxrate = newtaxrate

    # constructor
    def __init__(self, name, price=0):
        # Object attributes
        self.name = name
        self.price = price  # Private attribute
        self.qoh = 0

    def print_details(self):
        print("Name  : ", self.name)
        print("Price : ", self.price)

    def sell(self, qty):
        if self.qoh >= qty:
            self.qoh -= qty
        else:
            raise ValueError("Insufficient Quantity")

    def add(self, qty):
        self.qoh += qty

    def get_net_price(self):
        return self.price + self.price * Product.taxrate

    def set_price(self, newprice):
        self.price = newprice

    def __str__(self):
        return f"{self.name} - {self.price}"


if __name__ == '__main__':
    # Create objects
    p1 = Product("Dell Laptop", 50000)
    print(p1.get_net_price())
    Product.set_taxrate(0.20)
    print(p1.get_net_price())
    # p1.print_details()
    #
    # p2 = Product("iPhone 11")
    # p2.print_details()
