def fib():
    """Iteruje po liczbach ciągu Fibonacciego"""
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b
