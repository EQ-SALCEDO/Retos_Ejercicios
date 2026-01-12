# Pedir número al usuario
N = int(input("Ingresa un número entero entre 10 y 20: "))

# Validar rango
if N < 10 or N > 20:
    print("Error: el número debe estar entre 10 y 20.")
else:
    # Mostrar números del 1 al N
    print("\nNúmeros del 1 al", N)
    for i in range(1, N + 1):
        print(i)

    # Mostrar números del 30 al N en orden inverso
    print("\nNúmeros del 30 al", N, "en orden inverso")
    for i in range(30, N - 1, -1):
        print(i)
