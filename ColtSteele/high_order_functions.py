
def be_polite(function):
    def wrapper():
        print("What a pleasure to meet you")
        function()
        print("Have a lovely day")

    return wrapper


def greet():
    print("My name is Tony Perez")


greeting = be_polite(greet)  # passing a function to be_polite
greeting()
