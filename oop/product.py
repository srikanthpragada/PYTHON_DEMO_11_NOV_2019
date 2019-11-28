class Product:
    # constructor
    def __init__(self, name, price=0):
        # Object attributes
        self.name = name
        self.price = price  # Private attribute
        self.qoh = 0

    def print_details(self):
        print("Name  : ", self.name)
        print("Price : ", self.price)

    def __str__(self):
        return  f"{self.name} - {self.price}"


if __name__ == '__main__':
    # Create objects
    p1 = Product("Dell Laptop", 50000)
    p1.print_details()

    p2 = Product("iPhone 11")
    p2.print_details()
