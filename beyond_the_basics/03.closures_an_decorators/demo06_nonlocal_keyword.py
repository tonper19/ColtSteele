"""Variable scope and the nonlocal keyword demo"""
message = "global"

def enclosing():
    message = "enclosing"

    def local():
        # non local message
        message = "local"

        def locallocal():
            nonlocal message
            message = "locallocal"

        locallocal()
        print(f"local message: {message}")

    print(f"enclosing message: {message}")
    local()
    print(f"enclosing message: {message}")

print(f"global message: {message}")
enclosing()
print(f"global message: {message}")
