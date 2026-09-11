print("--- BIENVENIDO A LA ARENA ---")
gladiador = input("Nombre del Gladiador: ")

while not gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    gladiador = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
dano_pesado = 15
dano_enemigo = 12
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{gladiador} (HP: {int(vida_jugador)}) vs Enemigo (HP: {int(vida_enemigo)}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")
    
    while not opcion.isdigit() or int(opcion) not in range(1, 4):
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")
        
    if opcion == "1":
        if vida_enemigo < 20:
            dano_final = dano_pesado * 1.5
            print("¡Golpe Crítico!")
        else:
            dano_final = float(dano_pesado)

        vida_enemigo -= dano_final
        if vida_enemigo < 0:
            vida_enemigo = 0
        print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")

    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
        if vida_enemigo < 0:
            vida_enemigo = 0

    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Te has curado 30 HP. Te quedan {pociones} pociones.")
        else:
            print("¡No quedan pociones!")
            
    if vida_enemigo > 0:
        vida_jugador -= dano_enemigo
        if vida_jugador < 0:
            vida_jugador = 0
        print(f">> ¡El enemigo contraataca por {dano_enemigo} puntos!")
        if vida_jugador > 0:
            print("=== NUEVO TURNO ===")
            
print("\n================ FIN DE LA BATALLA ================")
if vida_jugador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")