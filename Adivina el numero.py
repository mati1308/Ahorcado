import random

numero_secreto = random.randint(1, 20)

intentos = 5

for intento in range(1, intentos + 1):
    numero = input("Por favor, ingrese un número: ")
    numero = int(numero)
    print("Intento " + str(intento) + ": " + str(numero))


    if numero == numero_secreto:
        print("Has adivinado el número secreto " + str(numero_secreto) + " en el intento " + str(intento))
        break
    elif numero < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
else:
    print("No adivinaste el número secreto " + str(numero_secreto) + " en " + str(intentos) + " intentos.")
