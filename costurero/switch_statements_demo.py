"""How to implement a switch-case statement in Python

The Pythonic way to implement switch statement is to use the 
powerful dictionary mappings, also known as associative arrays, that 
provide simple one-to-one key-value mappings.

https://jaxenter.com/implement-switch-case-statement-python-138315.html
"""

def switch_demo(argument):
    """Dictionary named switcher to store all the switch-like cases.
    
    When you pass an argument to the switch_demo function, it is looked
    up against the switcher dictionary mapping. If a match is found, 
    the associated value is printed, else a default string 
    (‘Invalid Month’) is printed. The default string helps implement the
    ‘default case’ of a switch statement.
    """
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(argument, "Invalid month")

def one():
    return "January"
 
def two():
    return "February"
 
def three():
    return "March"
 
def four():
    return "April"
 
def five():
    return "May"
 
def six():
    return "June"
 
def seven():
    return "July"
 
def eight():
    return "August"
 
def nine():
    return "September"
 
def ten():
    return "October"
 
def eleven():
    return "November"
 
def twelve():
    return "December"
 
 
def numbers_to_months(argument):
    """Dictionary mapping for functions.

    The values of a Python dictionary can be of any data type. So you 
    don’t have to confine yourself to using constants (integers, strings),
    you can also use function names and lambdas as values.
    """
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    return func()


class Switcher(object):
    def numbers_to_months(self, argument):
        """Dispatch method.
        
        if you’re calling methods on objects, you can even use a 
        dispatch method to dynamically determine which function 
        needs to be called during runtime.
        """
        method_name = 'month_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid month")
        # Call the method as we return it
        return method()
 
    def month_1(self):
        return "January"
 
    def month_2(self):
        return "February"
 
    def month_3(self):
        return "March"

 
def pone():
    return "Ozzie Smith"
    
def pone_2():
    return "Richie Ashburn"
 
def ptwo():
    return "Derek Jetter"
 
def ptwo_2():
    return "Nellie Fox"
    
def pthree():
    return "Babe Ruth"
 
def pthree_2():
    return "Dale Murphy"
    
def pfour():
    return "Lou Gehrig"
 
def pfour_2():
    return "Mel Ott"
    
 
switcher = {
        1: pone,
        2: ptwo,
        3: pthree,
        4: pfour
    }
 
 
def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "No player with that number")
    # Execute the function
    return func()

def main():
    print("*** Using switch function")
    print(f"The 8th month of the year is {switch_demo(8)}")
    print(f"The 13th month of the year is {switch_demo(13)}")

    print("*** Using switch function returning a function")
    print(f"The 7th month of the year is {numbers_to_months(7)}")

    print("*** Using a switch class dispatching a method")
    sw = Switcher()
    print(f"{sw.numbers_to_months(3)}")

    print("*** Easily change your very switch statement on the fly")
    print("Best baseball players wearing the first four numbers:")
    for k in switcher:
        print(f"{k}. {numbers_to_strings(k)}")

    print("No way! the best baseball players wearing the first four numbers are :")
    switcher[1] = pone_2
    switcher[2] = ptwo_2
    switcher[3] = pthree_2
    switcher[4] = pfour_2
    
    for k in switcher:
        print(f"{k}. {numbers_to_strings(k)}")
    

if __name__ == "__main__":
    main()