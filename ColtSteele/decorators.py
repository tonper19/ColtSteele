"""
decorators.py


"""


def be_polite(function):
    # *args and **kwargs allows to put as many parameters as needed
    def wrapper(*args, **kwargs):
        print(function(*args, **kwargs))

    return wrapper


@be_polite
def ignore_greet():
    return "..."


@be_polite
def greet(name):
    return f"My name is {name}"


@be_polite
def homie_greet(homie_greeting, name):
    return f"{homie_greeting} {name}"


if __name__ == "__main__":
    # different number of parameters calling the decorated be_polite function
    greet("Tony Perez")
    homie_greet("Yo! wassup, I'm ", "Will Smith")
    ignore_greet()
