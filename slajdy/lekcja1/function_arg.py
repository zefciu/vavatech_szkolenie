def factorial(n):
    """Zwraca silnię danej liczby"""
    result = 1
    for i in range(n+1):
        result *= i
    return result
