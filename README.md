# TPI-Barcena-Costantini

## Descripción del Proyecto
Sistema desarrollado en Python para la gestión de información de países, permitiendo realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un conjunto de datos almacenados en un archivo CSV.

El programa permite:
- Visualizar el listado completo de países
- Agregar nuevos países con validación de datos
- Actualizar población y superficie de un país existente
- Buscar países por nombre (coincidencia parcial)
- Filtrar por continente, rango de población y rango de superficie
- Ordenar por nombre, población y superficie (ascendente/descendente)
- Mostrar estadísticas: mayor/menor población, promedios, cantidad por continente

## Datos de la Universidad y la Cátedra
| Campo | Dato |
|-------|------|
| **Universidad** | Universidad Tecnológica Nacional (UTN) |
| **Carrera** | Tecnicatura Universitaria en Programación (TUP) |
| **Cátedra** | Programación I |
| **Docente Titular** | Ariel Enferrel - Martín A. García - Cinthia Rigoni |
| **Docente Tutor** | Luciano Chiroli - Virginia Cimino |

## Integrantes del Equipo
| Apellido y Nombre | Comision |
|-------------------|--------|
| Bárcena, Pablo Iván | 8 |
| Costantini, Luciano | 26 |

| Recurso | Enlace |
|---------|--------|
| **Repositorio GitHub** | [https://github.com/Ivan-cinho/TPI-Barcena-Costantini](https://github.com/Ivan-cinho/TPI-Barcena-Costantini) |
| **Video explicativo** | [https://www.youtube.com/watch?v=mkYAeAwK4lc]([https://www.youtube.com/watch?v=mkYAEaW4lc](https://www.youtube.com/watch?v=mkYAeAwK4lc)) |
---

## Estructura del Proyecto
```
TPI-Barcena-Costantini/
│
├── tp_integrador.py # Archivo principal del programa
├── paises.csv # Base de datos (archivo CSV)
├── README.md # Documentación del proyecto
└── .gitignore # Archivos ignorados por Git
```
---

## Instrucciones de Ejecución

### Requisitos previos
- Python 3.x instalado
- Git (opcional, para clonar el repositorio)

### Paso a paso
1. **Clonar el repositorio**
```bash
git clone https://github.com/Ivan-cinho/TPI-Barcena-Costantini.git
cd TPI-Barcena-Costantini

2. **Ejecutar el programa**
tp_integrador.py

3. **Seguir las instrucciones del menú interactivo**

## Ejemplos de Entrada y Salida
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
Ingrese una opción (1-8):

## Ejemplo 1: Mostrar listado de países

Entrada: 1

Salida:
Argentina,45376763,2780400,America
Japon,125800000,377975,Asia
Brasil,213993437,8515767,America
Alemania,83149300,357022,Europa
Canada,38250000,9984670,America
...

## Ejemplo 2: Agregar un país

Entrada:
2
Ingrese el nombre del pais: Chile
Ingrese la poblacion: 19116201
Ingrese la superficie: 756102
Ingrese el continente: America

Salida:
========================================
            AGREGAR PAIS
========================================

Nombre ingresado
Poblacion ingresada
Superficie ingresada
Continente ingresado

'Chile' se agrego correctamente

--- LISTA ACTUALIZADA ---
Argentina,45376763,2780400,America
Japon,125800000,377975,Asia
Brasil,213993437,8515767,America
Alemania,83149300,357022,Europa
Chile,19116201,756102,America

## Tecnologías Utilizadas

Lenguaje: Python 3

Estructuras de datos: Listas, diccionarios

Manejo de archivos: CSV (lectura/escritura)

Control de versiones: Git / GitHub

Validaciones: Funciones específicas con manejo de errores

## Funcionalidades Implementadas
Función				Descripción
cargar_datos()			Lee el archivo CSV y devuelve una lista de diccionarios
guardar_datos()			Guarda la lista de países en el archivo CSV
mostrar_datos()			Muestra todos los países en formato CSV
agregar_pais()			Agrega un nuevo país con validaciones
actualizar_datos()		Modifica población o superficie de un país
buscar_pais()			Busca países por coincidencia parcial
filtrar_por_continente()	Filtra por continente exacto
filtrar_por_poblacion()		Filtra por rango de población
filtrar_por_superficie()	Filtra por rango de superficie
ordenar_por_nombre()		Ordena alfabéticamente (ASC/DESC)
ordenar_por_poblacion()		Ordena por población (ASC/DESC)
ordenar_por_superficie()	Ordena por superficie (ASC/DESC)
estadistica()			Menú de estadísticas
mayor_y_menor_poblacion()	País con mayor y menor población
promedio_de_poblacion()		Promedio de población
promedio_de_superficie()	Promedio de superficie
paises_por_continente()		Cantidad de países por continente

## Validaciones Implementadas
Control de errores de formato en el CSV
Validación de nombres: solo letras y espacios, no vacíos
Validación de números: enteros positivos, no vacíos
Control de duplicados al agregar países
Manejo de errores con try-except en el menú principal
Mensajes claros de éxito/error
Prevención de fallos en búsquedas y filtros sin resultados
