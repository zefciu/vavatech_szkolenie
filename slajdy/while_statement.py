a = 1
while a <= 256:
    print(a)
    a *= 2

while True:
    name = input("Podaj imię: ")
    if len(name) > 20:
        print("Imię za długie!")
        continue
    break

