"""
Ejercicio: Números negativos y repetidos

Objetivo:
Pedir 10 números al usuario, almacenarlos en una lista y mostrar cada número
indicando si es NEGATIVO y/o REPETIDO dentro de la lista.
"""

# Lista para almacenar los números
numeros = []

# Pedir 10 números al usuario
for i in range(10):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

print("\nResultados:")

# Recorrer la lista y evaluar cada número
for num in numeros:
    mensajes = []

    # Verificar si es negativo
    if num < 0:
        mensajes.append("NEGATIVO")

    # Verificar si está repetido
    if numeros.count(num) > 1:
        mensajes.append("REPETIDO")

    # Mostrar resultado
    if mensajes:
        print(f"{num} → {' | '.join(mensajes)}")
    else:
        print(f"{num} → OK")
