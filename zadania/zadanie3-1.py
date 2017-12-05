# 1. Napisz funkcję, która wczyta liczbę całkowitą z klawiatury, powtarzając
# prompt do skutku jeśli użytkownik podał wartość, która nie jest liczbą.
# W przeciwnym wypadku
# zwraca obiekt typu `int`
# 2. Napisz funkcję, która pobiera dowolną liczbę argumentów i liczy ich
# średnią. Jeśli użytkownik nie poda żadnego argumentu -- rzuca TypeError


def input_int(prompt):
    while True:
        s = input(prompt)
        if not s:
            return None
        try:
            return int(s)
        except ValueError:
            print('Nieprawidłowa wartość')


def mean(*args):
    if not len(args):
        raise TypeError('Potrzebny przynajmniej jeden argument')
    return sum(args) / len(args)


if __name__ == '__main__':
    args = []
    while True:
        arg = input_int('Podaj liczbę: ')
        if arg is None:
            break
        args.append(arg)
    print(mean(*args))
