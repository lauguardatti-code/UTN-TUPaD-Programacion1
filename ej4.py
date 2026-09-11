# --- VARIABLES INICIALES ---
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzados_seguidos = 0  # Para la regla anti-spam de la opción 1

# --- INGRESO Y VALIDACIÓN DEL AGENTE ---
agente = input("Ingrese el nombre del agente: ")

while not agente.isalpha():
    print("Error: El nombre del agente debe contener únicamente letras.")
    agente = input("Ingrese el nombre del agente: ")

print(f"\n¡Agente {agente}, la misión en la bóveda ha comenzado!")

# --- BUCLE PRINCIPAL DEL JUEGO ---
# Condición: energía > 0, tiempo > 0, cerraduras < 3 y que no se cumpla la regla de bloqueo por alarma
mision_bloqueada = False

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not mision_bloqueada:
    # Verificación de regla de bloqueo por alarma (alarma == True y tiempo <= 3)
    if alarma and tiempo <= 3:
        mision_bloqueada = True
        break

    print("\n----------------------------------------")
    print(f"ESTADO: Energía={energia} | Tiempo={tiempo} | Cerraduras={cerraduras_abiertas}/3 | Alarma={'ON' if alarma else 'OFF'}")
    print("----------------------------------------")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = input("\nSeleccione una acción (1-3): ")

    # Validación con .isdigit()
    while not opcion.isdigit() or int(opcion) not in range(1, 4):
        print("Error: Opción inválida. Ingrese un número entre 1 y 3.")
        opcion = input("Seleccione una acción (1-3): ")

    # ==========================================
    # OPCIÓN 1: FORZAR CERRADURA
    # ==========================================
    if opcion == "1":
        forzados_seguidos += 1
        
        # Descuento de recursos
        energia -= 20
        tiempo -= 2

        # Regla Anti-spam: si es la 3ra vez seguida
        if forzados_seguidos == 3:
            alarma = True
            print("\n¡ALERTA ANTI-SPAM! Forzaste la cerradura 3 veces seguidas. La cerradura se trabó y se activó la alarma.")
        else:
            # Riesgo de alarma si la energía (antes de forzar o actual) cae bajo 40
            if energia < 40:
                print("\n¡ADVERTENCIA! Al tener menos de 40 de energía hay RIESGO DE ALARMA.")
                num_riesgo = input("Ingrese un número de riesgo (1-3): ")
                
                while not num_riesgo.isdigit() or int(num_riesgo) not in range(1, 4):
                    print("Error: Ingrese un número válido entre 1 y 3.")
                    num_riesgo = input("Ingrese un número de riesgo (1-3): ")

                if num_riesgo == "3":
                    alarma = True
                    print("¡Se activó la alarma por cometer un error!")

            # Si no saltó la alarma, abre cerradura
            if not alarma:
                cerraduras_abiertas += 1
                print(f"¡Éxito! Lograste abrir una cerradura. (Abiertas: {cerraduras_abiertas}/3)")

    # ==========================================
    # OPCIÓN 2: HACKEAR PANEL
    # ==========================================
    elif opcion == "2":
        forzados_seguidos = 0  # Corta la racha de forzado
        energia -= 10
        tiempo -= 3

        print("\nHackeando panel de control...")
        # Bucle for de 4 pasos mostrando progreso
        for paso in range(1, 5):
            print(f"  Progreso: paso {paso}/4...")
            codigo_parcial += "A"  # Agrega una letra al código parcial

        print(f"Código parcial acumulado: '{codigo_parcial}' (Largo: {len(codigo_parcial)})")

        # Si junta 8 o más caracteres, abre una cerradura
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                codigo_parcial = ""  # Se reinicia el código
                print(f"¡Código completado! Se abrió automáticamente 1 cerradura. (Abiertas: {cerraduras_abiertas}/3)")

    # ==========================================
    # OPCIÓN 3: DESCANSAR
    # ==========================================
    elif opcion == "3":
        forzados_seguidos = 0  # Corta la racha de forzado
        
        # Recuperación base y costo de tiempo
        ganancia_energia = 15
        tiempo -= 1

        # Penalización si la alarma está encendida
        if alarma:
            ganancia_energia -= 10  # Costo extra de -10 energía
            print("\nDescansando en tensión (Alarma ON: penalización de -10 energía extra).")
        else:
            print("\nDescansando tranquilamente...")

        energia += ganancia_energia

        # Tope máximo de energía: 100
        if energia > 100:
            energia = 100

        print(f"Energía recuperada. Energía actual: {energia}")

    # Chequeo extra de la regla de bloqueo tras ejecutar la acción
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        mision_bloqueada = True

# ==========================================
# RESULTADOS / CONDICIONES DE FIN
# ==========================================
print("\n================ FINAL DEL JUEGO ================")

if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! Felicitaciones Agente {agente}, lograste abrir la bóveda a tiempo.")
elif mision_bloqueada:
    print(f"DERROTA (Bloqueo): Se activó la alarma y el tiempo bajó a 3 o menos. El sistema se bloqueó por completo.")
elif energia <= 0:
    print(f"DERROTA: Te quedaste sin energía ({energia}). El agente se desmayó.")
elif tiempo <= 0:
    print(f"DERROTA: Te quedaste sin tiempo ({tiempo}). Llegó el equipo de seguridad.")