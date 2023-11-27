def triangle(hauteur):
    for i in range(hauteur - 1):

        for j in range(hauteur -i -1):
            print(" ", end="")
        print("/", end="")

        for j in range(2 * i):
            print(" ", end="")
        print("\\")
    print("/", end="")
    for i in range(2 * (hauteur -1)):
        print("_", end="")
    print("\\")

hauteur = int(input("Hauteur du triangle: "))
triangle(hauteur)
print(triangle)

 