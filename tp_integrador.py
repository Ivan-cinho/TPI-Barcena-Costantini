# Variables
menu = """
========================================
        SISTEMA DE GESTIÓN DE PAÍSES
========================================

1. Mostrar listado total de países
2. Agregar un país
3. Actualizar datos de población o superficie
4. Buscar un país
5. Filtrar países
6. Ordenar países
7. Mostrar estadísticas
8. Finalizar programa

========================================
Ingrese una opción (1-8): """

error_de_opcion = """"
========================================
                ERROR
    DEBE INGRESAR UN NRO ENTRE 1 Y 8
========================================
"""

mensaje_agregar_pais = """"
========================================
            AGREGAR PAIS
========================================
"""

# Funciones auxiliares
#Funcion para obtener los datos del .csv y acumularlos en una lista
def cargar_datos(): 
    paises = []
    with open('paises.csv', 'r', encoding='utf-8') as listado:
        contenido = listado.readlines()

    for linea in contenido[1:]:
        if linea.strip(): # solo itera lineas q no esten vacias
            dato = linea.strip().split(",")
            pais = {
                "nombre": dato[0],
                "poblacion": int(dato[1]),
                "superficie": int(dato[2]),
                "continente": dato[3]
            }
            paises.append(pais)
    return paises

# Funcion para dar formato previo a ejecutar otras funciones evitando incluirla en ellas
def formatear_datos(pais):
    return f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}"

#Funcion para mostrar/printear los datos en pantalla, invoca a la funcion formatear_datos()
def mostrar_datos(paises): 
    for pais in paises:
        print(formatear_datos(pais))

#Funcion para guardar las modificaciones en el csv
def guardar_datos(paises):
    with open('paises.csv', 'w', encoding='utf-8') as listado:
        listado.write("nombre,poblacion,superficie,continente\n")
        for pais in paises:
            listado.write(formatear_datos(pais) + "\n")

# Actualizar datos
#Funcion para validar que los datos numericos cumplen con el formato
def validar_numero_entero(numero):
    if not numero:
        print("ERROR - No puede dejar el dato vacio")
        return None
    try:
        numero = int(numero)
        if numero <= 0:
            print("El numero no puede ser menor a cero (0)")
            return None
        else:
            return numero
    except ValueError:
        print("Debe ingresar un numero")   

#Funcion para validar que el nombre cumpla con el formato
def validar_nombre(nombre):
    nombre = nombre.strip()
    if not nombre:
        print("ERROR - No puede dejar el dato vacio")
        return None
    if not nombre.replace(" ", "").isalpha():
        print("ERROR - Solo puede ingresar texto")
        return None
    else:
        nombre = nombre.title()
        return nombre

#Funccion para agregar un nuevo pais con sus 4 datos correspondientes, tal vez se pueda reducir o modularizar
def agregar_pais():
    print(mensaje_agregar_pais)
    while True: #Bloque para el nombre
        nombre = input("Ingrese el nombre del pais: ").strip()
        nombre_valido = validar_nombre(nombre) #Invocacion a la funcion validar_nombre 
        if not nombre_valido:
            continue
        paises = cargar_datos()
        existe = False
        for p in paises: #Verficacion de nombre duplicado
            if p["nombre"].lower() == nombre_valido.lower():
                print(f"ERROR - El pais {nombre_valido} ya existe en la lista")
                existe = True
                break 
        if not existe:
            nombre = nombre_valido
            print("Nombre ingresado")
            break

    while True: #Bloque para la poblacion
        poblacion_str = input("Ingrese la poblacion: ").strip()
        poblacion_validada = validar_numero_entero(poblacion_str)
        if poblacion_validada is not None:
            poblacion = poblacion_validada
            print("Poblaion ingresada")
            break

    while True: #Bloque para la superficie
        superficie_str = input("Ingrese la superficie: ").strip()
        superficie_validada = validar_numero_entero(superficie_str)
        if superficie_validada is not None:
            superficie = superficie_validada
            print("Superficie ingresada")
            break

    while True: #Bloque para el continente
        continente = input("Ingrese el continente: ").strip()
        continente_validado = validar_nombre(continente)
        if continente_validado:
            continente = continente_validado
            print("Continente ingresado")
            break

    paises.append({  # Agregar a la lista y guardar
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    guardar_datos(paises)
    print(f"\n'{nombre}' se agrego correctamente")
    print("\n--- LISTA ACTUALIZADA ---")
    mostrar_datos(paises)


def actualizar_datos():
    paises = cargar_datos()
    nombre = input("Ingrese el nombre del país a modificar: ").strip()
    encontrado = False
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            encontrado = True
            print("\nPaís encontrado:")
            print(formatear_datos(p))
            print("\n1. Modificar población")
            print("2. Modificar superficie")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1": #Modificar población
                while True:
                    poblacion_str = input("Ingrese la nueva población: ").strip()
                    poblacion_validada = validar_numero_entero(poblacion_str)
                    if poblacion_validada is not None:
                        p["poblacion"] = poblacion_validada
                        print("Población actualizada")
                        break

            elif opcion == "2": #Modificar superficie
                while True:
                    superficie_str = input("Ingrese la nueva superficie: ").strip()
                    superficie_validada = validar_numero_entero(superficie_str)
                    if superficie_validada is not None:
                        p["superficie"] = superficie_validada
                        print("Superficie actualizada")
                        break
                    
            else:
                print("Opción inválida.")
                return
            guardar_datos(paises)
            print("Datos actualizados correctamente.")
            break

    if not encontrado:
        print(f"No existe el país '{nombre}'.")

def buscar_pais():
    print()

# Filtros
def filtrar_por_continente():
    print()
    
def filtrar_por_poblacion():
    print()
    
def filtrar_por_superficie():
    print()
    
# Ordenar
def ordenar_por_nombre():
    print()

def ordenar_por_poblacion():
    print()

def ordenar_por_superficie():
    print()

# mostrar estadisticas
def mayor_y_menor_poblacion():
    print()

def promedio_de_poblacion():
    print()

def promedio_de_superficie():
    print()

def paises_por_continente():
    print()

# PROGRAMA
while True:
    try:
        opcion = input(menu) #menu principal
        opcion = int(opcion)
        if opcion < 1 or opcion > 8:
            print(f"{error_de_opcion}")
        else:
            match opcion:
                case 1:
                    paises = cargar_datos()
                    mostrar_datos(paises)
                case 2:
                    agregar_pais()
                case 3:
                    print("Actualizar datos de poblacion o superficie")
                case 4:
                    print("Buscar un pais")
                case 5:
                    print("Filtrar paises")
                case 6:
                    print("Ordenar paises")
                case 7:
                    print("Mostrar estadisticas")
                case 8:
                    print("Finalizar programa")
                    break
    except ValueError: #manejo de error en caso de ingresar un caracter q no sea numerico
        print(f"{error_de_opcion}")
    except Exception as e:
        print("Error", type(e).__name__)

    