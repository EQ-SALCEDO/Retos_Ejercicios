"""
Reto: Cálculo de Factorial

Objetivo:
Calcular el factorial de un número entero N y también calcular
el factorial de todos los números dentro de una lista.
"""

# Función para calcular el factorial de un número
def factorial(n):
    """
    Calcula el factorial de un número entero positivo.
    Ejemplo: 5! = 5 x 4 x 3 x 2 x 1
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# ---------- PARTE 1: Factorial de un número ----------

n = int(input("Ingresa un número entero: "))

if n < 0:
    print("El factorial no está definido para números negativos.")
else:
    print(f"{n}! = {factorial(n)}")


# ---------- PARTE 2: Factorial de una lista de números ----------

cantidad = int(input("\n¿Cuántos números deseas ingresar?: "))
numeros = []

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

print("\nFactoriales de la lista:")

for num in numeros:
    if num < 0:
        print(f"{num}! → No definido")
    else:
        print(f"{num}! = {factorial(num)}")
