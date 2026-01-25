"""
Reto: Operaciones Avanzadas con Listas

Objetivo:
Pedir números al usuario hasta que ingrese 0, almacenarlos en una lista
y realizar diferentes operaciones sobre ella.
"""

# ---------- PARTE 1: Captura de números ----------

numeros = []

while True:
    num = int(input("Ingresa un número (0 para terminar): "))
    if num == 0:
        break
    numeros.append(num)

print("\nLista completa:", numeros)

# ---------- PARTE 2: Números en posiciones pares ----------

print("\nNúmeros en posiciones pares:")
for i in range(0, len(numeros), 2):
    print(numeros[i])

# ---------- PARTE 3: Lista en orden inverso ----------

print("\nLista en orden inverso:")
print(numeros[::-1])

# ---------- PARTE 4: Dividir la lista en dos mitades ----------

mitad = len(numeros) // 2
primera_mitad = numeros[:mitad]
segunda_mitad = numeros[mitad:]

print("\nPrimera mitad:", primera_mitad)
print("Segunda mitad:", segunda_mitad)

# ---------- PARTE 5: Elementos internos de la primera mitad ----------

print("\nElementos internos de la primera mitad:")
if len(primera_mitad) > 2:
    print(primera_mitad[1:-1])
else:
    print("No hay suficientes elementos para mostrar.")

# ---------- PARTE 6: Máximo y mínimo de la segunda mitad ----------

if segunda_mitad:
    print("\nMáximo de la segunda mitad:", max(segunda_mitad))
    print("Mínimo de la segunda mitad:", min(segunda_mitad))
else:
    print("\nLa segunda mitad está vacía.")
