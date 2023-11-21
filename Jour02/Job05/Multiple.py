#1 a 100
for nombre in range(1, 101):
    #  multiples de trois et cinq
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    # Vérifier multiples de trois
    elif nombre % 3 == 0:
        print("Fizz")
    # Vérifier multiples de cinq
    elif nombre % 5 == 0:
        print("Buzz")
    # Afficher le nombre pour les autres
    else:
        print(nombre)
    