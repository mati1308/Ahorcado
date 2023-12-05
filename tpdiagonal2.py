#declare una matriz 4x4. relice una funcion que devuelva la suma de la diagonal
#principal y otra que devuelva la multiplicacion
#hacer otras 2 funciones que devuelvan suma y multiplicacion de la contradiagonal.
#declarar en lista de listas
#utilizar un for anidado para recorrer la matriz
matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [8, 10, 11, 12], [13, 14, 15, 16]]

def DiagonalPrincipal(matriz):
    resultado = 0
    for i in range(4):
        resultado += matriz[i][i]
    return resultado

def DiagonalPrincipalMult(matriz):
    resultado = 1
    for i in range(4):
        resultado *= matriz[i][i]
    return resultado

def Contradiagonal(matriz):
    resultado = 0
    for i in range(4):
        resultado += matriz[i][3 - i]
    return resultado

def ContradiagonalMult(matriz):
    resultado = 1
    for i in range(4):
        resultado *= matriz[i][3 - i]
    return resultado

print("Suma Diagonal Principal:", DiagonalPrincipal(matriz))
print("Multiplicación Diagonal Principal:", DiagonalPrincipalMult(matriz))
print("Suma Contradiagonal:", Contradiagonal(matriz))
print("Multiplicación Contradiagonal:", ContradiagonalMult(matriz))
