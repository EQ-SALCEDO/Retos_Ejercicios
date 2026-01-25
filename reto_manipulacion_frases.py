"""
Reto: Manipulación de Frases

Objetivo:
Pedir una frase al usuario y realizar distintas operaciones:
- Mostrar palabras en posiciones pares
- Mostrar la frase invertida
- Dividir la frase en dos mitades y mostrar cada una
"""

# Pedir la frase al usuario
frase = input("Ingresa una frase: ")

# Convertir la frase en una lista de palabras
palabras = frase.split()

# 1. Mostrar palabras en posiciones pares (índices pares)
print("\nPalabras en posiciones pares:")
for i in range(0, len(palabras), 2):
    print(palabras[i])

# 2. Mostrar la frase invertida
frase_invertida = frase[::-1]
print("\nFrase invertida:")
print(frase_invertida)

# 3. Dividir la frase en dos mitades
mitad = len(frase) // 2
primera_mitad = frase[:mitad]
segunda_mitad = frase[mitad:]

print("\nFrase dividida en dos mitades:")
print("Primera mitad:", primera_mitad)
print("Segunda mitad:", segunda_mitad)
