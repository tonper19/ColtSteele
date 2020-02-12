class Product():
    TAX_RATE = 0.21

    def __init__(self, name, price):
        self.name = name 
        self._price = price

    @property
    def price(self):
        # now if we need to change how price is calculated, we can do it 
        # here (or in the "setter" and __init__)
        return self._price + self._price * Product.TAX_RATE

    @price.setter
    def price(self, value):
        # The "setter" function must have the same name as the property
        self._price = value


def main():
    p = Product("Macbook", 4200)
    print(f"The price of {p.name} is {p.price}")

if __name__ == "__main__":
    main()