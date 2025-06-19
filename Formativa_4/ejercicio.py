import funciones as fc

turistas = {
"001": ["John Doe", "Estados Unidos", "12-01-2024"],
"002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
"012": ["Julian Martinez", "Argentina", "19-09-2023"],
"014": ["Agustin Morales", "Argentina", "28-03-2024"],
"005": ["Carlos Garcia", "Mexico", "10-05-2024"],
"006": ["Maria Lopez", "Mexico", "08-12-2023"],
"007": ["Joao Silva", "Brasil", "20-06-2024"],
"003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
"004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
"008": ["Ana Santos", "Brasil", "03-10-2023"],
"010": ["Martin Fernandez", "Argentina", "13-02-2023"],
"011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

opcion = ""
while opcion != "4":
    print("\n\nMENÚ PRINCIPAL\n1.- Turistas por pais\n2.- Turista por mes.\n3.- Eliminar turista.\n4.- Salir.")
    opcion = input("Opción: ")
    if opcion == "1":
        fc.turista_por_pais(turistas)
    elif opcion == "2":
        fc.turista_por_mes(turistas)
    elif opcion == "3":
        fc.eliminar_turista(turistas)
    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opción inválida")
