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

def formatear_datos(pais):
    return f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}"

#Funcion para mostrar/printear los datos en pantalla, invoca a la funcion cargar_datos()
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
def agregar_pais():
    print()
    
def actualizar_datos():
    print()

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
                    mostrar_datos()
                case 2:
                    print("Agregar un pais")
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

    