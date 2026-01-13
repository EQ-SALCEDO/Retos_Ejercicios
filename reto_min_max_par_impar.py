# Pedir los números
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

# Determinar el máximo
if n1 >= n2 and n1 >= n3:
    maximo = n1
elif n2 >= n1 and n2 >= n3:
    maximo = n2
else:
    maximo = n3

# Determinar el mínimo
if n1 <= n2 and n1 <= n3:
    minimo = n1
elif n2 <= n1 and n2 <= n3:
    minimo = n2
else:
    minimo = n3

# Mostrar máximo y mínimo
print("El número máximo es:", maximo)
print("El número mínimo es:", minimo)

# Función para saber si es par o impar
def par_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"

# Mostrar par o impar
print("El número", n1, "es", par_impar(n1))
print("El número", n2, "es", par_impar(n2))
print("El número", n3, "es", par_impar(n3))
