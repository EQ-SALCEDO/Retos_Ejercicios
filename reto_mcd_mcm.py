"""
Reto: Cálculo de MCD y MCM

Objetivo:
Calcular el MCD y el MCM de dos números y de una lista de números.
"""

# ---------- FUNCIONES ----------

def mcd(a, b):
    """
    Calcula el Máximo Común Divisor usando el algoritmo de Euclides.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


def mcm(a, b):
    """
    Calcula el Mínimo Común Múltiplo usando el MCD.
    """
    return abs(a * b) // mcd(a, b)


# ---------- PARTE 1: DOS NÚMEROS ----------

n = int(input("Ingresa el primer número entero: "))
m = int(input("Ingresa el segundo número entero: "))

print("\nResultados con dos números:")
print("MCD:", mcd(n, m))
print("MCM:", mcm(n, m))


# ---------- PARTE 2: VARIOS NÚMEROS ----------

cantidad = int(input("\n¿Cuántos números deseas ingresar?: "))
numeros = []

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

# Calcular MCD y MCM de la lista
mcd_total = numeros[0]
mcm_total = numeros[0]

for num in numeros[1:]:
    mcd_total = mcd(mcd_total, num)
    mcm_total = mcm(mcm_total, num)

print("\nResultados con la lista:")
print("Números:", numeros)
print("MCD de todos:", mcd_total)
print("MCM de todos:", mcm_total)
