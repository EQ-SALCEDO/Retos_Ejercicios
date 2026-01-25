"""
Reto: Lista sin repetidos

Objetivo:
Crear una función que reciba una lista y devuelva otra lista
eliminando los elementos repetidos, conservando el orden original.
"""

def lista_sin_repetidos(lista):
    """
    Recibe una lista y devuelve una nueva lista sin elementos repetidos.
    """
    resultado = []

    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)

    return resultado


# Ejemplo de uso
numeros = [1, 2, 3, 2, 4, 1, 5]
print("Lista original:", numeros)
print("Lista sin repetidos:", lista_sin_repetidos(numeros))

