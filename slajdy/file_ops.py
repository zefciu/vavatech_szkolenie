# Otwarcie pliku do odczytu
with open('filename', 'r', encoding='utf-8') as f:
# Iteracja po liniach
    for i, line in enumerate(f):
        print('{:03} - {}'.format(i, line), end='')

# Otwarcie pliku do zapisu
with open('filename2', 'w') as f:
    print('Hello!', file=f)
