usuario_correcto = "alumno"
clave_correcta = "python123"

intentos_maximos = 3
intento_actual = 1
login_exitoso = False

# --- 1. LOGIN DE ACCESO ---
while intento_actual <= intentos_maximos and not login_exitoso:
    print(f"\nIntento {intento_actual}/{intentos_maximos}")
    usuario_ingresado = input("Ingrese el nombre de usuario: ")
    clave_ingresada = input("Ingrese la clave: ")

    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        print("Acceso concedido.")
        login_exitoso = True
    else:
        print("Error: credenciales inválidas.")
        intento_actual += 1

# --- 2. EVALUACIÓN Y MENÚ ---
if not login_exitoso:
    print("\nCuenta bloqueada.")
else:
    opcion = ""
    while opcion != "4":
        print("\n------ MENÚ PRINCIPAL ------")
        print("1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mostrar mensaje motivacional")
        print("4) Salir")

        opcion_ingresada = input("\nIngrese una opción (1-4): ")

        # Validar que sea un número y esté entre 1 y 4
        if not opcion_ingresada.isdigit() or int(opcion_ingresada) not in range(1, 5):
            print("Error: Opción inválida. Ingrese un número entre 1 y 4.")
            continue

        opcion = opcion_ingresada

        if opcion == "1":
            print("\nEstado: Inscripto")
        elif opcion == "2":
            nueva_clave = input("Ingrese la nueva clave: ")
            if len(nueva_clave) < 6:
                print("Error: La clave debe tener al menos 6 caracteres. Cambio rechazado.")
            else:
                confirmacion = input("Confirme la nueva clave: ")
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("¡Clave actualizada con éxito!")
                else:
                    print("Error: Las claves no coinciden. Cambio rechazado.")

        elif opcion == "3":
            print("\nFrase motivacional: ¡El éxito es la suma de pequeños esfuerzos repetidos día tras día!")

        elif opcion == "4":
            print("\n¡Hasta luego!")