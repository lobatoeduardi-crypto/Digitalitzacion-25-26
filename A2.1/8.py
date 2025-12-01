# Comprobación de pertenencia

list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

# Pedimos un número al usuario
numero = int(input("Introduce un número: "))

# Comprobamos si está en la lista
if numero in list_num:
    print("El número", numero, "está en la lista.")
else:
    print("El número", numero, "no está en la lista.")
