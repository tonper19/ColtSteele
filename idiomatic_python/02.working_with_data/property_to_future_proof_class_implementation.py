class Product():
    TAX_RATE = 0.21

    def __init__(self, name, price):
        self.name = name 
        self._price = price

    @property
    def price(self):
        # now if we need to change how price is calculated, we can do it 
        # here (or in the "setter" and __init__)
        return self._price * TAX_RATE

    @price.setter
    def price(self, value):
        # The "setter" function must have the same name as the property
        self._price = value
