import random

estudiantes = ["Matias", "Jorge", "Federico", "Sabrina", "Sofia"]

orden = random.sample(estudiantes, len(estudiantes))

print("Orden de exposición:")
for i, estudiante in enumerate(orden, start=1):
    print(str(i) + ". " + estudiante)
