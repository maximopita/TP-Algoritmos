# Pregunta si es superusuario
super_usuario = input("Ingrese la letra 'S' para ingresar como superusuario (o cualquier otra para continuar como cliente): ").upper()

if super_usuario == "S":
    peliculas_input = input("Ingrese los nombres de las películas separados por coma: ")
    nombre_peliculas = [p.strip() for p in peliculas_input.split(",")]

    capacidad_salas = []
    for pelicula in nombre_peliculas:
        while True:
            try:
                capacidad = int(input(f"Ingrese la capacidad de la sala para '{pelicula}': "))
                if capacidad > 0:
                    capacidad_salas.append(capacidad)
                    break
                else:
                    print("La capacidad debe ser mayor que cero.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
else:
    # Cartelera por defecto
    nombre_peliculas = ["Toy Story 4", "Donde están las rubias", "Ted 2", "Cars 3"]
    capacidad_salas = [40, 20, 30, 40]

# Mostrar cartelera
fin_programa = False
print("\nCartelera:")
for i, pelicula in enumerate(nombre_peliculas, start=1):
    print(f"{i}. {pelicula} (Entradas disponibles: {capacidad_salas[i-1]})")

# Bucle principal de reserva
while not fin_programa:
    try:
        num_pelicula = int(input("\nIngrese el número de película que quiere ver (-1 para salir): "))

        if num_pelicula == -1:
            fin_programa = True
            print("Programa finalizado.")
            break

        if num_pelicula < 1 or num_pelicula > len(nombre_peliculas):
            print("Error: número de película inválido.")
            continue

        indice = num_pelicula - 1
        print(f"Seleccionó: {nombre_peliculas[indice]}")

        # Validar cantidad de entradas
        while True:
            try:
                cantidad_entradas = int(input("¿Cuántas entradas desea comprar?: "))
                if cantidad_entradas <= 0:
                    print("Error: la cantidad debe ser mayor que 0.")
                elif cantidad_entradas > capacidad_salas[indice]:
                    print(f"No hay suficientes entradas disponibles. Quedan {capacidad_salas[indice]} asientos.")
                else:
                    break
            except ValueError:
                print("Error: ingrese un número válido.")

        # Fecha
        fecha_reserva = input("Ingrese la fecha de la función (dd/mm/aaaa): ")

        # Validar horario
        while True:
            try:
                horario_reserva = int(input("Ingrese el horario de la función (por ejemplo, 1830): "))
                if 0 <= horario_reserva <= 2400:
                    break
                else:
                    print("Error: ingrese un horario válido entre 0000 y 2400.")
            except ValueError:
                print("Error: ingrese un número válido para el horario.")

        # Confirmación
        print("\n¡Reserva exitosa!")
        print(f"Película: {nombre_peliculas[indice]}")
        print(f"Fecha: {fecha_reserva}")
        print(f"Horario: {horario_reserva}")
        print(f"Entradas: {cantidad_entradas}")

        # Actualizar entradas disponibles
        capacidad_salas[indice] -= cantidad_entradas

    except ValueError:
        print("Error: por favor ingrese un valor numérico válido.")
