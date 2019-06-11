try:
    n = int(s)
except ValueError:
    print('To nie liczba')

try:
    # Tu może pojawić się wyjątek
except TypWyjątku:
    # Wywoła się gdy pojawi się wyjątek
else:
    # Wywoła się, gdy nie było wyjątku
finally:
    # Wywoła się zawsze
