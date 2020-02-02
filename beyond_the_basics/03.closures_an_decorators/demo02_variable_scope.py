"""Variable scope example."""
g = "global"
def outer(p="parameter"):
    l = "local"
    def inner():
        print(g, p, l)
    inner()

if __name__ == "__main__":
    outer()
