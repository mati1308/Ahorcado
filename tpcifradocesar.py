def cifrado_cesar(palabra, desplazamiento, letras):
    resultado = ""
    for letra in palabra:
        if letra.lower() in letras:
            indice = (letras.index(letra.lower()) + desplazamiento) % len(letras)
            resultado += letras[indice]
        else:
            resultado += letra
    return resultado

# Lista de letras específica
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Solicitar entrada al usuario
palabra_usuario = input("Ingrese una palabra: ")
desplazamiento_usuario = int(input("Ingrese un desplazamiento numérico (+ o -): "))

# Aplicar cifrado César
palabra_cifrada = cifrado_cesar(palabra_usuario, desplazamiento_usuario, letras)

# Mostrar resultado
print("Palabra original:", palabra_usuario)
print("Palabra cifrada:", palabra_cifrada)
