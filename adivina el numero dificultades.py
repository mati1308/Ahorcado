import random

numero_secreto = random.randint(1, 20)

intentos = 5

dificultad = input("Seleccione una dificultad (facil/dificil): ").lower()

if dificultad == "facil":
    rango_maximo = 20
    intentos_maximos = 5
elif dificultad == "dificil":
    rango_maximo = 50
    intentos_maximos = 7
else:
    print("Dificultad no válida")

numero_secreto = random.randint(1, rango_maximo)

print("El rango de números es de 1 a " + str(rango_maximo) + " y tienes " + str(intentos_maximos) + " intentos.")    

for intento in range(1, intentos_maximos + 1):
    numero = input("Por favor, ingrese un número: ")
    numero = int(numero)
    print("Intento " + str(intento) + ": " + str(numero))


    if numero == numero_secreto:
        print("Has adivinado el número secreto " + str(numero_secreto) + " en el intento " + str(intentos_maximos))
        break
    elif numero < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
else:
    print("No adivinaste el número secreto " + str(numero_secreto) + " en " + str(intentos_maximos) + " intentos.")
