"""
Reto: Detección de Palíndromos

Objetivo:
Determinar si una palabra, frase o número es palíndromo.
Se ignoran mayúsculas, espacios y signos de puntuación.
También se evalúa una lista de palabras o números.
"""

import string

def es_palindromo(texto):
    """
    Determina si un texto o número es palíndromo.
    Retorna True si lo es, False si no.
    """

    # Convertir a string y pasar a minúsculas
    texto = str(texto).lower()

    # Eliminar espacios y signos de puntuación
    texto_limpio = ""
    for caracter in texto:
        if caracter.isalnum():  # letras y números
            texto_limpio += caracter

    # Comparar con su versión invertida
    return texto_limpio == texto_limpio[::-1]


# ---------- PARTE 1: Evaluar un solo texto ----------

entrada = input("Ingresa una palabra, frase o número: ")

if es_palindromo(entrada):
    print("→ Es palíndromo")
else:
    print("→ No es palíndromo")


# ---------- PARTE 2: Evaluar una lista ----------

cantidad = int(input("\n¿Cuántos elementos deseas evaluar?: "))
elementos = []

for i in range(cantidad):
    valor = input(f"Ingrese el elemento {i + 1}: ")
    elementos.append(valor)

print("\nResultados:")

for elemento in elementos:
    if es_palindromo(elemento):
        print(f"{elemento} → True (Palíndromo)")
    else:
        print(f"{elemento} → False")

