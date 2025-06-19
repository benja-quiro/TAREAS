
# VALIDACIONES
def validar_nombre(contexto: str) -> str:
    while True:
        nombre = input(contexto).strip()
        if all(palabra.isalpha() for palabra in nombre.split()):
            return nombre.title()
        else:
            print("Solo se permiten letras!")

def validar_numero_en_rango(contexto: str, min_val: int | None = None, max_val: int | None = None) -> int:
    while True:
        try:
            numero = int(input(contexto))
            if min_val is not None and numero < min_val:
                print(f"No puede ingresar un número menor a {min_val}")
                continue
            if max_val is not None and numero > max_val:
                print(f"No puede ingresar un número mayor a {max_val}")
                continue
            return numero
        except ValueError:
            print("Solo se permiten números!")


"""
No seguiré algunos requisitos que piden, como recibir los inputs desde fuera, lo haré un poco a mí manera
pero siempre solucionando el problema planteado.
"""

# OPCIONES 

# 1
def turista_por_pais(dicc: dict):
    pais = validar_nombre("Ingrese un país: ")
    lista_nombres = [x[0] for x in dicc.values() if pais == x[1]]
    if not lista_nombres:
        print(f"No hay turistas de {pais}")
    else:
        print(f"Turistas de {pais}:")
        for nombre in lista_nombres:
            print(nombre, end= ", ")

# 2
def turista_por_mes(dicc: dict):
    contador = 0
    input_mes = validar_numero_en_rango("Ingrese un mes: ", 1, 12)
    input_mes = str(input_mes).zfill(2) # Este método rellena de ceros a la izquierda hasta alcanzar la longitud determinada, con esto hago que coincida con las fechas del dicc
    lista_meses = [x[2][3:5] for x in dicc.values()] # Comprensión de listas, obtengo todos los datos con dicc.values() y accedo a la fecha con el indice[2] y para obtener el mes uso slicing
    for mes in lista_meses:
        if mes == input_mes:
            contador += 1
    if not contador:
        print(f"No se encontraron turistas que ingresarón el mes {input_mes}")
    else:
        print(f"El porcentaje de personas que ingreso el mes: {input_mes} es {contador * 100 / len(dicc.keys()):.1f}%")

# 3
def eliminar_turista(dicc: dict):
    nombre = validar_nombre("Ingrese el nombre del turista a eliminar: ")
    eliminado = False
    for clave, valor in list(dicc.items()): # Hay que hacer una copia del iterable porque si este sufre modificaciones da  un error
        if valor[0] == nombre:
            eliminado = True
            del dicc[clave]

    if not eliminado:
        print(f"{nombre} no existe.")
    else:
        print(f"{nombre} fue eliminado con éxito.")

