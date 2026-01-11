# Pedir datos al usuario
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros (ej. 1.85): "))

# Convertir altura
metros = int(altura)
centimetros = int((altura - metros) * 100)

# Mostrar resultado
print(f"El usuario {nombre} tiene {edad} años de edad y mide {metros} metro(s) y {centimetros} centímetros.")
