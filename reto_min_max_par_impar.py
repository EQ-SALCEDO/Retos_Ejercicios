"""
Reto: Mínimo y Máximo con N números

Objetivo:
Permitir que el usuario ingrese una cantidad variable de números (N),
determinar cuál es el número mínimo y máximo, y mostrar si cada número
es par o impar.

Este ejercicio demuestra el uso de listas y funciones integradas de Python
como min() y max().
"""

# Solicitar al usuario cuántos números desea ingresar
cantidad = int(input("¿Cuántos números deseas ingresar?: "))

# Lista para almacenar los números
numeros = []

# Leer los números uno por uno
for i in range(cantidad):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

# Calcular el número mínimo y máximo usando funciones de Python
minimo = min(numeros)
maximo = max(numeros)

# Mostrar resultados
print("\nResultados:")
print("Números ingresados:", numeros)
print("Número mínimo:", minimo)
print("Número máximo:", maximo)

# Función para determinar si un número es par o impar
def par_impar(num):
    """
    Determina si un número es par o impar.
    Retorna una cadena con el resultado.
    """
    if num % 2 == 0:
        return "par"
    else:
        return "impar"

# Mostrar si cada número es par o impar
print("\nPar o impar:")
for num in numeros:
    print(f"El número {num} es {par_impar(num)}")
