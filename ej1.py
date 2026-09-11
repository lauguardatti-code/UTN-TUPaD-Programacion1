nombre = input("Ingrese el nombre: ")

while nombre == "" or not nombre.isalpha():
    print("Error: el nombre debe contener solo letras y no puede estar vacío.")
    nombre = input("Ingrese el nombre: ")

cantidad = input("Ingrese la cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: la cantidad debe ser un número entero positivo.")
    cantidad = input("Ingrese la cantidad de productos: ")
cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0

for i in range(cantidad):
    print(f"\nProducto {i + 1}")

    precio = input("Ingrese el precio: ")

    while not precio.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio = input("Ingrese el precio: ")

    precio = int(precio)
    descuento = input("¿Tiene descuento? (S/N): ")

    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Error: ingrese S o N.")
        descuento = input("¿Tiene descuento? (S/N): ")

    total_sin_descuentos += precio

    if descuento.lower() == "s":
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuentos += precio_con_descuento

ahorro_total = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

print("\n----- RESUMEN DE COMPRA -----")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
