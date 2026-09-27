lista_nombres = []
conjunto_cedulas = set()
diccionario_notas = {}

while True:
    print("\n1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        nota = input("Nota: ")

        if cedula in conjunto_cedulas:
            print("Esa cédula ya está registrada.")
        else:
            lista_nombres.append(nombre)
            conjunto_cedulas.add(cedula)
            diccionario_notas[nombre] = nota
            print("Estudiante agregado.")

    elif opcion == "2":
        for nombre in lista_nombres:
            print(nombre, "-", diccionario_notas[nombre])

    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        if nombre in diccionario_notas:
            print("Nota:", diccionario_notas[nombre])
        else:
            print("No encontrado.")

    elif opcion == "4":
        break

    else:
        print("Opción no válida.")