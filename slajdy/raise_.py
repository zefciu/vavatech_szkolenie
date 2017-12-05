if not isinstance(x, int):
    raise TypeError('x musi być int')

try:
    return a > b
except TypeError:
    print('Błędne typy')
    raise # wysyłamy wyjątek dalej
