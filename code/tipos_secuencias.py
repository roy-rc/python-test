#!/usr/bin/env python3
"""
Ejemplos completos de tipos de secuencias en Python
- list (listas mutables)
- tuple (tuplas inmutables)
- range (secuencias numéricas)
- Operadores comunes de secuencias
- Métodos específicos de cada tipo
"""

def ejemplos_listas():
    """Ejemplos detallados de listas (list)"""
    print("=" * 60)
    print("LISTAS (list) - SECUENCIAS MUTABLES")
    print("=" * 60)
    
    # Creación de listas
    print("--- CREACIÓN DE LISTAS ---")
    lista_vacia = []
    lista_vacia_alt = list()
    lista_numeros = [1, 2, 3, 4, 5]
    lista_mixta = [1, "texto", 3.14, True, [1, 2]]
    lista_desde_string = list("Python")
    lista_desde_range = list(range(5))
    
    print(f"Lista vacía: {lista_vacia}")
    print(f"Lista vacía (list()): {lista_vacia_alt}")
    print(f"Lista de números: {lista_numeros}")
    print(f"Lista mixta: {lista_mixta}")
    print(f"Desde string: {lista_desde_string}")
    print(f"Desde range: {lista_desde_range}")
    print(f"Tipo: {type(lista_numeros)}")
    print()
    
    # Operadores básicos
    print("--- OPERADORES BÁSICOS ---")
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    
    print(f"Lista1: {lista1}")
    print(f"Lista2: {lista2}")
    print(f"Concatenación (+): {lista1 + lista2}")
    print(f"Repetición (*3): {lista1 * 3}")
    print(f"Pertenencia (2 in lista1): {2 in lista1}")
    print(f"No pertenencia (7 not in lista1): {7 not in lista1}")
    print(f"Longitud: len(lista1) = {len(lista1)}")
    print()
    
    # Indexación y slicing
    print("--- INDEXACIÓN Y SLICING ---")
    frutas = ["manzana", "banana", "naranja", "uva", "kiwi"]
    print(f"Frutas: {frutas}")
    print(f"Primera fruta: frutas[0] = {frutas[0]}")
    print(f"Última fruta: frutas[-1] = {frutas[-1]}")
    print(f"Primeras 3: frutas[:3] = {frutas[:3]}")
    print(f"Desde índice 2: frutas[2:] = {frutas[2:]}")
    print(f"Cada 2: frutas[::2] = {frutas[::2]}")
    print(f"Reverso: frutas[::-1] = {frutas[::-1]}")
    
    # Modificación (mutabilidad)
    print(f"Original: {frutas}")
    frutas[1] = "plátano"  # Cambiar elemento
    print(f"Después de frutas[1] = 'plátano': {frutas}")
    frutas[2:4] = ["mandarina", "pera", "mango"]  # Cambiar slice
    print(f"Después de slice: {frutas}")
    print()
    
    # Métodos de listas
    print("--- MÉTODOS DE LISTAS ---")
    numeros = [1, 3, 2, 4, 3, 5]
    print(f"Lista original: {numeros}")
    
    # Agregar elementos
    numeros.append(6)
    print(f"Después de append(6): {numeros}")
    
    numeros.insert(0, 0)
    print(f"Después de insert(0, 0): {numeros}")
    
    numeros.extend([7, 8, 9])
    print(f"Después de extend([7, 8, 9]): {numeros}")
    
    # Buscar elementos
    print(f"index(3): {numeros.index(3)}")  # Primera ocurrencia
    print(f"count(3): {numeros.count(3)}")  # Contar ocurrencias
    
    # Eliminar elementos
    numeros.remove(3)  # Remover primera ocurrencia
    print(f"Después de remove(3): {numeros}")
    
    elemento = numeros.pop()  # Eliminar y retornar último
    print(f"pop() retornó {elemento}, lista: {numeros}")
    
    elemento = numeros.pop(0)  # Eliminar en índice específico
    print(f"pop(0) retornó {elemento}, lista: {numeros}")
    
    # Ordenamiento
    numeros_copia = numeros.copy()
    numeros.sort()
    print(f"Después de sort(): {numeros}")
    
    numeros.reverse()
    print(f"Después de reverse(): {numeros}")
    
    # Limpiar lista
    numeros.clear()
    print(f"Después de clear(): {numeros}")
    print(f"Copia guardada: {numeros_copia}")
    print()


def ejemplos_tuplas():
    """Ejemplos detallados de tuplas (tuple)"""
    print("=" * 60)
    print("TUPLAS (tuple) - SECUENCIAS INMUTABLES")
    print("=" * 60)
    
    # Creación de tuplas
    print("--- CREACIÓN DE TUPLAS ---")
    tupla_vacia = ()
    tupla_vacia_alt = tuple()
    tupla_un_elemento = (42,)  # Coma necesaria
    tupla_sin_parentesis = 1, 2, 3  # Empaquetado de tupla
    tupla_parentesis = (1, 2, 3, 4, 5)
    tupla_mixta = (1, "texto", 3.14, True)
    tupla_desde_lista = tuple([1, 2, 3, 4])
    tupla_desde_string = tuple("Python")
    
    print(f"Tupla vacía: {tupla_vacia}")
    print(f"Un elemento: {tupla_un_elemento}")
    print(f"Sin paréntesis: {tupla_sin_parentesis}")
    print(f"Con paréntesis: {tupla_parentesis}")
    print(f"Tupla mixta: {tupla_mixta}")
    print(f"Desde lista: {tupla_desde_lista}")
    print(f"Desde string: {tupla_desde_string}")
    print(f"Tipo: {type(tupla_parentesis)}")
    print()
    
    # Operadores (similares a listas)
    print("--- OPERADORES ---")
    tupla1 = (1, 2, 3)
    tupla2 = (4, 5, 6)
    
    print(f"Tupla1: {tupla1}")
    print(f"Tupla2: {tupla2}")
    print(f"Concatenación: {tupla1 + tupla2}")
    print(f"Repetición: {tupla1 * 2}")
    print(f"Pertenencia: {2 in tupla1}")
    print(f"Longitud: {len(tupla1)}")
    print()
    
    # Indexación (como listas)
    print("--- INDEXACIÓN ---")
    coordenadas = (10, 20, 30)
    print(f"Coordenadas: {coordenadas}")
    print(f"x = coordenadas[0] = {coordenadas[0]}")
    print(f"y = coordenadas[1] = {coordenadas[1]}")
    print(f"z = coordenadas[2] = {coordenadas[2]}")
    print()
    
    # Inmutabilidad
    print("--- INMUTABILIDAD ---")
    print("Las tuplas son inmutables:")
    try:
        coordenadas[0] = 15  # Esto causará error
    except TypeError as e:
        print(f"Error al intentar modificar: {e}")
    print()
    
    # Métodos de tuplas (limitados)
    print("--- MÉTODOS DE TUPLAS ---")
    numeros_tupla = (1, 2, 3, 2, 4, 2, 5)
    print(f"Tupla: {numeros_tupla}")
    print(f"count(2): {numeros_tupla.count(2)}")
    print(f"index(4): {numeros_tupla.index(4)}")
    
    # No tiene métodos como append, remove, etc.
    print(f"Métodos disponibles: {[m for m in dir(numeros_tupla) if not m.startswith('_')]}")
    print()
    
    # Desempaquetado de tuplas
    print("--- DESEMPAQUETADO DE TUPLAS ---")
    punto = (100, 200)
    x, y = punto  # Desempaquetar
    print(f"Punto: {punto}")
    print(f"x = {x}, y = {y}")
    
    # Desempaquetado múltiple
    persona = ("Juan", "Pérez", 25, "Ingeniero")
    nombre, apellido, edad, profesion = persona
    print(f"Persona: {persona}")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad}")
    print(f"Profesión: {profesion}")
    
    # Desempaquetado con *
    numeros = (1, 2, 3, 4, 5)
    primero, *resto, ultimo = numeros
    print(f"Números: {numeros}")
    print(f"Primero: {primero}")
    print(f"Resto: {resto}")
    print(f"Último: {ultimo}")
    print()
    
    # Intercambio de variables
    print("--- INTERCAMBIO DE VARIABLES ---")
    a = 10
    b = 20
    print(f"Antes: a = {a}, b = {b}")
    a, b = b, a  # Intercambio usando tuplas
    print(f"Después: a = {a}, b = {b}")
    print()


def ejemplos_ranges():
    """Ejemplos detallados de ranges"""
    print("=" * 60)
    print("RANGES - SECUENCIAS NUMÉRICAS INMUTABLES")
    print("=" * 60)
    
    # Creación de ranges
    print("--- CREACIÓN DE RANGES ---")
    
    # range(stop)
    range1 = range(5)
    print(f"range(5): {range1}")
    print(f"Como lista: {list(range1)}")
    
    # range(start, stop)
    range2 = range(2, 8)
    print(f"range(2, 8): {list(range2)}")
    
    # range(start, stop, step)
    range3 = range(0, 10, 2)
    print(f"range(0, 10, 2): {list(range3)}")
    
    # range con step negativo
    range4 = range(10, 0, -1)
    print(f"range(10, 0, -1): {list(range4)}")
    
    range5 = range(20, 0, -3)
    print(f"range(20, 0, -3): {list(range5)}")
    
    print(f"Tipo: {type(range1)}")
    print()
    
    # Propiedades de ranges
    print("--- PROPIEDADES DE RANGES ---")
    r = range(1, 11)
    print(f"Range: {r}")
    print(f"Longitud: len(r) = {len(r)}")
    print(f"Primer elemento: r[0] = {r[0]}")
    print(f"Último elemento: r[-1] = {r[-1]}")
    print(f"Elemento en índice 5: r[5] = {r[5]}")
    
    # Operadores
    print(f"5 in r: {5 in r}")
    print(f"15 not in r: {15 not in r}")
    
    # Slicing en ranges
    print(f"r[2:5]: {list(r[2:5])}")
    print(f"r[::2]: {list(r[::2])}")
    print(f"r[::-1]: {list(r[::-1])}")
    print()
    
    # Métodos de ranges
    print("--- MÉTODOS DE RANGES ---")
    numeros_r = range(1, 10)
    print(f"Range: {list(numeros_r)}")
    print(f"count(5): {numeros_r.count(5)}")
    print(f"index(7): {numeros_r.index(7)}")
    
    # Ranges son inmutables como tuplas
    print("Los ranges son inmutables (no se pueden modificar)")
    print()
    
    # Eficiencia de ranges
    print("--- EFICIENCIA DE RANGES ---")
    import sys
    
    # Range es eficiente en memoria
    rango_grande = range(1000000)
    lista_grande = list(range(1000))
    
    print(f"Tamaño de range(1000000): {sys.getsizeof(rango_grande)} bytes")
    print(f"Tamaño de list(range(1000)): {sys.getsizeof(lista_grande)} bytes")
    print("Los ranges no almacenan todos los valores, los generan según se necesitan")
    print()
    
    # Casos prácticos
    print("--- CASOS PRÁCTICOS ---")
    
    # Bucles
    print("Usando range en bucles:")
    for i in range(3):
        print(f"  Iteración {i}")
    
    # Índices de una lista
    frutas = ["manzana", "banana", "naranja"]
    print(f"Frutas: {frutas}")
    print("Iterando con índices:")
    for i in range(len(frutas)):
        print(f"  {i}: {frutas[i]}")
    
    # Generar secuencias específicas
    print("Años de la década de los 2020:")
    for año in range(2020, 2030):
        print(f"  {año}")
    
    print("Números pares del 0 al 20:")
    pares = list(range(0, 21, 2))
    print(f"  {pares}")
    print()


def operadores_comunes_secuencias():
    """Operadores comunes a todas las secuencias"""
    print("=" * 60)
    print("OPERADORES COMUNES DE SECUENCIAS")
    print("=" * 60)
    
    # Datos de prueba
    lista = [1, 2, 3, 4, 5]
    tupla = (1, 2, 3, 4, 5)
    rango = range(1, 6)
    cadena = "12345"
    
    print("--- DATOS DE PRUEBA ---")
    print(f"Lista: {lista}")
    print(f"Tupla: {tupla}")
    print(f"Range: {list(rango)}")
    print(f"String: '{cadena}'")
    print()
    
    # Operador in
    print("--- OPERADOR 'in' ---")
    valor_buscar = 3
    print(f"¿{valor_buscar} está en cada secuencia?")
    print(f"  Lista: {valor_buscar in lista}")
    print(f"  Tupla: {valor_buscar in tupla}")
    print(f"  Range: {valor_buscar in rango}")
    print(f"  String: {str(valor_buscar) in cadena}")
    print()
    
    # Operador len()
    print("--- FUNCIÓN len() ---")
    print(f"Longitudes:")
    print(f"  Lista: {len(lista)}")
    print(f"  Tupla: {len(tupla)}")
    print(f"  Range: {len(rango)}")
    print(f"  String: {len(cadena)}")
    print()
    
    # Funciones min, max, sum
    print("--- FUNCIONES min(), max(), sum() ---")
    secuencias_numericas = [lista, tupla, rango]
    nombres = ["Lista", "Tupla", "Range"]
    
    for seq, nombre in zip(secuencias_numericas, nombres):
        print(f"{nombre}:")
        print(f"  min(): {min(seq)}")
        print(f"  max(): {max(seq)}")
        print(f"  sum(): {sum(seq)}")
    
    # Para strings, min y max funcionan con orden lexicográfico
    print(f"String '{cadena}':")
    print(f"  min(): '{min(cadena)}'")
    print(f"  max(): '{max(cadena)}'")
    # sum() no funciona con strings
    print()
    
    # Indexación común
    print("--- INDEXACIÓN COMÚN ---")
    indice = 2
    print(f"Elemento en índice {indice}:")
    print(f"  Lista[{indice}]: {lista[indice]}")
    print(f"  Tupla[{indice}]: {tupla[indice]}")
    print(f"  Range[{indice}]: {rango[indice]}")
    print(f"  String[{indice}]: '{cadena[indice]}'")
    print()
    
    # Slicing común
    print("--- SLICING COMÚN ---")
    print(f"Slice [1:4]:")
    print(f"  Lista: {lista[1:4]}")
    print(f"  Tupla: {tupla[1:4]}")
    print(f"  Range: {list(rango[1:4])}")
    print(f"  String: '{cadena[1:4]}'")
    print()


def comparacion_tipos_secuencias():
    """Comparación entre tipos de secuencias"""
    print("=" * 60)
    print("COMPARACIÓN ENTRE TIPOS DE SECUENCIAS")
    print("=" * 60)
    
    # Crear secuencias equivalentes
    datos = [1, 2, 3, 4, 5]
    lista = datos.copy()
    tupla = tuple(datos)
    rango = range(1, 6)
    
    print("--- CARACTERÍSTICAS ---")
    características = [
        ("Tipo", type(lista).__name__, type(tupla).__name__, type(rango).__name__),
        ("Mutable", "Sí", "No", "No"),
        ("Ordenada", "Sí", "Sí", "Sí"),
        ("Permite duplicados", "Sí", "Sí", "N/A"),
        ("Indexable", "Sí", "Sí", "Sí"),
        ("Iterable", "Sí", "Sí", "Sí")
    ]
    
    print(f"{'Característica':<20} {'Lista':<10} {'Tupla':<10} {'Range':<10}")
    print("-" * 60)
    for caracteristica in características:
        print(f"{caracteristica[0]:<20} {caracteristica[1]:<10} {caracteristica[2]:<10} {caracteristica[3]:<10}")
    print()
    
    # Casos de uso
    print("--- CASOS DE USO RECOMENDADOS ---")
    casos_uso = {
        "Lista": [
            "Cuando necesitas modificar los datos",
            "Colección de elementos homogéneos o heterogéneos",
            "Orden importa y puede cambiar",
            "Necesitas métodos como append, remove, sort"
        ],
        "Tupla": [
            "Datos que no cambian (coordenadas, configuración)",
            "Retorno múltiple de funciones",
            "Como clave de diccionario (son hashables)",
            "Desempaquetado de variables"
        ],
        "Range": [
            "Secuencias numéricas en bucles",
            "Generar índices para otras secuencias",
            "Secuencias aritméticas predecibles",
            "Eficiencia de memoria para números grandes"
        ]
    }
    
    for tipo, usos in casos_uso.items():
        print(f"{tipo}:")
        for uso in usos:
            print(f"  • {uso}")
        print()
    
    # Conversiones entre tipos
    print("--- CONVERSIONES ENTRE TIPOS ---")
    print(f"Lista original: {lista}")
    print(f"Lista → Tupla: {tuple(lista)}")
    print(f"Lista → String: '{''.join(map(str, lista))}'")
    
    print(f"Tupla original: {tupla}")
    print(f"Tupla → Lista: {list(tupla)}")
    
    print(f"Range original: {list(rango)}")
    print(f"Range → Lista: {list(rango)}")
    print(f"Range → Tupla: {tuple(rango)}")
    print()


if __name__ == "__main__":
    ejemplos_listas()
    ejemplos_tuplas()
    ejemplos_ranges()
    operadores_comunes_secuencias()
    comparacion_tipos_secuencias()