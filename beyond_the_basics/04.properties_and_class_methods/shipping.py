"""Properties and class methods demo.

Example:
    Found in the main() function

Notes:    
    Class methods accepts the class object as the first formal 
    argument by convention using the abbreviated name cls since we
    can't use the the fully spelled keyword 'class' as an argument 
    name.

    Class methods as constructors: this technique allows to spur multiple
    functions which behave similarly to its constructors but with 
    different behaviors without having to resort to contorsions within
    the __init__ method to interpret different forms of argument lists.

"""
import iso6346

class ShippingContainer:
    """Shipping container object.
    
    Attributes:
        owner_code (str): container owner's code.
        contents (str, list): container's content, it could be a 
            series of items.
        bic (str): International Container Bureau (BIC) serial number.
    """
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1964  # next available serial number

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6))

    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result
    
    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        """Create a shipping container instance without any content.
        
        Args:
            owner_code (str): container owner's code.
        
        Returns:
            ShippingContainer instance with no contents.

        Note:
            class methods as constructor.
        """
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        """Create a shipping container with multiple items as content.
        
        Args:
            owner_code (str): container owner's code.
        
        Returns:
            ShippingContainer instance with list of items as contents.

        Note:
            class methods as constructor.
        """
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)


    def __init__(self, owner_code, length_ft, contents):
        """Initialize the ShippingContainer.
        
        Args:
            owner_code (str): container owner's code.
            contents (str, list): container contents in the form of
                a single item (str), or multiple items (list).
        """
        self.contents = contents
        self.length_ft = length_ft
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial()
        )

    @property
    def volume_ft3(self):
        return (ShippingContainer.HEIGHT_FT * 
                ShippingContainer.WIDTH_FT * 
                self.length_ft)

class RefrigeratedShippingContainer(ShippingContainer):
    """Refirgerated shipping container object.

    Example of static methods with inheritance.
    """

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    @staticmethod
    def _c_to_f(celsius):
        return round(celsius * 9/5 + 32, 2)

    @staticmethod
    def _f_to_c(fahrenheit):
        return round((fahrenheit - 32) * 5/9, 2)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category="R")

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)
    
    @fahrenheit.setter
    def fahreneheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    @property
    def volume_ft3(self):
        """Refrigerated container volume."""
        return (super().volume_ft3
                - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3)

def main():
    """Examples of properties and class methods.
    """
    c1 = ShippingContainer("YML", 20, "coffee")
    print(f"Container bic Number: {c1.bic} Cargo: {c1.contents}")

    c2 = ShippingContainer("MAE", 40, "bananas")
    print(f"Container bic Number: {c2.bic} Cargo: {c2.contents}")

    # using class methods as constructors: empty container
    c3 = ShippingContainer.create_empty("YML", length_ft=20)
    print(f"Container bic Number: {c3.bic} Cargo:"
          f" {'Empty' if c3.contents == None else c3.contents}")

    # using class methods as constructors: multiple items container
    c4 = ShippingContainer.create_with_items("MAE", 40, 
                                             ["food", "textiles", "medicines"])
    print(f"Container bic Number: {c4.bic} Cargo:"
          f" {'Empty' if c4.contents == None else c4.contents}"
          f"\n   It measures {c4.volume_ft3} cubic feet.")

    # refrigerated container inherited from the ShippingContainer
    r1 = RefrigeratedShippingContainer.create_with_items("MAE", 20, 
                                                         ["sardines", "tuna", 
                                                         "cod"],
                                                         celsius=2.0)

    print(f"Container bic Number: {r1.bic} Cargo: {r1.contents}")

    # refrigerated container inherited from the ShippingContainer
    r2 = RefrigeratedShippingContainer.create_with_items("ESC", 40, 
                                                         ["beef", "porc"], 
                                                         celsius=-18)
    print(f"Container bic Number: {r2.bic} Cargo: {r2.contents}"
          f"\n   The temperature of the container is {r2.celsius} Celsius / "
          f"{r2.fahreneheit} Fahrenheit."
          f"\n   It measures {r2.volume_ft3} cubic feet.")
    # r2.celsius = 5  # not allowed


if __name__ == "__main__":
    main()

