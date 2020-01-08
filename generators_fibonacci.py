def fibonacci():
    """Generates an infinite sequence of Fibonacci numbers on demand"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci()

counter = 0
for x in f:
    # print(x, " ", end="")
    print(x)
    counter += 1
    if (counter > 100):
        break
print()
