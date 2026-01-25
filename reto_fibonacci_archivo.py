"""
Reto: Sucesión de Fibonacci

Objetivo:
Mostrar los N primeros números de la sucesión de Fibonacci
y guardarlos en un archivo llamado fibonacci.txt
"""

# Solicitar cuántos números de Fibonacci se desean
n = int(input("¿Cuántos números de Fibonacci deseas generar?: "))

# Lista para almacenar la sucesión
fibonacci = []

# Generar la sucesión
a, b = 0, 1

for i in range(n):
    fibonacci.append(a)
    a, b = b, a + b

# Mostrar por pantalla
print("\nSucesión de Fibonacci:")
print(fibonacci)

# Guardar en el archivo fibonacci.txt
with open("fibonacci.txt", "w") as archivo:
    for num in fibonacci:
        archivo.write(str(num) + ",")

print("\nLa sucesión se ha guardado en el archivo 'fibonacci.txt'")
