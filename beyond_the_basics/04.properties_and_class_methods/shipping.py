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
    def create_empty(cls, owner_code):
        """Create a shipping container instance without any content.
        
        Args:
            owner_code (str): container owner's code.
        
        Returns:
            ShippingContainer instance with no contents.

        Note:
            class methods as constructor.
        """
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        """Create a shipping container with multiple items as content.
        
        Args:
            owner_code (str): container owner's code.
        
        Returns:
            ShippingContainer instance with list of items as contents.

        Note:
            class methods as constructor.
        """
        return cls(owner_code, contents=list(items))


    def __init__(self, owner_code, contents):
        """Initialize the ShippingContainer.
        
        Args:
            owner_code (str): container owner's code.
            contents (str, list): container contents in the form of
                a single item (str), or multiple items (list).
        """
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial()
        )

def main():
    """Examples of properties and class methods.
    """
    c1 = ShippingContainer("YML", "coffee")
    print(f"Container bic Number: {c1.bic} Cargo: {c1.contents}")

    c2 = ShippingContainer("MAE", "bananas")
    print(f"Container bic Number: {c2.bic} Cargo: {c2.contents}")

    # using class methods as constructors: empty container
    c3 = ShippingContainer.create_empty("YML")
    print(f"Container bic Number: {c3.bic} Cargo:"
          f" {'Empty' if c3.contents == None else c3.contents}")

    # using class methods as constructors: multiple items container
    c4 = ShippingContainer.create_with_items("MAE", 
                                             ["food", "textiles", "medicines"])
    print(f"Container bic Number: {c4.bic} Cargo:"
          f" {'Empty' if c4.contents == None else c4.contents}")

if __name__ == "__main__":
    main()

