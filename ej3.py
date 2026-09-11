# --- 1. DEFINICIÓN DE VARIABLES ---
# Lunes (4 cupos)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Martes (3 cupos)
martes1 = ""
martes2 = ""
martes3 = ""

# --- 2. INGRESO Y VALIDACIÓN DEL OPERADOR ---
operador = input("Ingrese el nombre del operador: ")

while not operador.isalpha():
    print("Error: El nombre del operador debe contener únicamente letras (sin espacios ni números).")
    operador = input("Ingrese el nombre del operador: ")

print(f"\n¡Bienvenido/a {operador}!")

# --- 3. MENÚ PRINCIPAL ---
opcion = ""
while opcion != "5":
    print("\n====== AGENDA DE TURNOS ======")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("\nIngrese una opción (1-5): ")

    # --- OPCIÓN 1: RESERVAR TURNO ---
    if opcion == "1":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        if dia not in ["1", "2"]:
            print("Error: Día inválido.")
            continue
        
        paciente = input("Ingrese nombre del paciente: ")
        while not paciente.isalpha():
            print("Error: El nombre del paciente debe contener solo letras.")
            paciente = input("Ingrese nombre del paciente: ")

        if dia == "1":  # LUNES
            if paciente in (lunes1, lunes2, lunes3, lunes4):
                print("Error: El paciente ya tiene un turno reservado para este día.")
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno reservado en Lunes (Turno 1) para {paciente}.")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno reservado en Lunes (Turno 2) para {paciente}.")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno reservado en Lunes (Turno 3) para {paciente}.")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno reservado en Lunes (Turno 4) para {paciente}.")
            else:
                print("Error: No quedan turnos disponibles para el día Lunes.")

        elif dia == "2":  # MARTES
            if paciente in (martes1, martes2, martes3):
                print("Error: El paciente ya tiene un turno reservado para este día.")
            elif martes1 == "":
                martes1 = paciente
                print(f"Turno reservado en Martes (Turno 1) para {paciente}.")
            elif martes2 == "":
                martes2 = paciente
                print(f"Turno reservado en Martes (Turno 2) para {paciente}.")
            elif martes3 == "":
                martes3 = paciente
                print(f"Turno reservado en Martes (Turno 3) para {paciente}.")
            else:
                print("Error: No quedan turnos disponibles para el día Martes.")

    # --- OPCIÓN 2: CANCELAR TURNO ---
    elif opcion == "2":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        if dia not in ["1", "2"]:
            print("Error: Día inválido.")
            continue

        paciente = input("Ingrese el nombre del paciente a cancelar: ")

        if dia == "1":
            if paciente == lunes1 and lunes1 != "":
                lunes1 = ""
                print(f"Turno de {paciente} en Lunes fue cancelado.")
            elif paciente == lunes2 and lunes2 != "":
                lunes2 = ""
                print(f"Turno de {paciente} en Lunes fue cancelado.")
            elif paciente == lunes3 and lunes3 != "":
                lunes3 = ""
                print(f"Turno de {paciente} en Lunes fue cancelado.")
            elif paciente == lunes4 and lunes4 != "":
                lunes4 = ""
                print(f"Turno de {paciente} en Lunes fue cancelado.")
            else:
                print("Error: No se encontró la reserva para ese paciente en Lunes.")

        elif dia == "2":
            if paciente == martes1 and martes1 != "":
                martes1 = ""
                print(f"Turno de {paciente} en Martes fue cancelado.")
            elif paciente == martes2 and martes2 != "":
                martes2 = ""
                print(f"Turno de {paciente} en Martes fue cancelado.")
            elif paciente == martes3 and martes3 != "":
                martes3 = ""
                print(f"Turno de {paciente} en Martes fue cancelado.")
            else:
                print("Error: No se encontró la reserva para ese paciente en Martes.")

    # --- OPCIÓN 3: VER AGENDA DEL DÍA ---
    elif opcion == "3":
        dia = input("Elegir día a consultar (1=Lunes, 2=Martes): ")
        if dia == "1":
            print("\n--- AGENDA LUNES ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '[Disponible]'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '[Disponible]'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '[Disponible]'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '[Disponible]'}")
        elif dia == "2":
            print("\n--- AGENDA MARTES ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '[Disponible]'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '[Disponible]'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '[Disponible]'}")
        else:
            print("Error: Día inválido.")

    # --- OPCIÓN 4: VER RESUMEN GENERAL ---
    elif opcion == "4":
        # Contamos cupos ocupados
        ocupados_lunes = (lunes1 != "") + (lunes2 != "") + (lunes3 != "") + (lunes4 != "")
        ocupados_martes = (martes1 != "") + (martes2 != "") + (martes3 != "")
        
        print("\n--- RESUMEN GENERAL ---")
        print(f"Lunes:  {ocupados_lunes}/4 turnos ocupados ({4 - ocupados_lunes} libres)")
        print(f"Martes: {ocupados_martes}/3 turnos ocupados ({3 - ocupados_martes} libres)")
        print(f"Total ocupados: {ocupados_lunes + ocupados_martes}/7")

    # --- OPCIÓN 5: CERRAR SISTEMA ---
    elif opcion == "5":
        print(f"\nSistema cerrado. ¡Hasta luego, {operador}!")

    else:
        print("Error: Opción inválida. Ingrese un número de 1 a 5.")