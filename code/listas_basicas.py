#!/usr/bin/env python3
"""
Ejemplos de manejo de listas básicas de Python
- Búsqueda de elementos
- Agregado de elementos
- Eliminación de elementos
- Listas unidimensionales y bidimensionales
"""

def ejemplos_listas_1d():
    """Ejemplos con listas unidimensionales"""
    print("=" * 50)
    print("EJEMPLOS DE LISTAS UNIDIMENSIONALES")
    print("=" * 50)
    
    # Crear lista inicial
    numeros = [1, 2, 3, 4, 5]
    frutas = ["manzana", "banana", "naranja"]
    
    print(f"Lista inicial de números: {numeros}")
    print(f"Lista inicial de frutas: {frutas}")
    print()
    
    # BÚSQUEDA DE ELEMENTOS
    print("--- BÚSQUEDA DE ELEMENTOS ---")
    
    # Verificar si un elemento existe
    if 3 in numeros:
        print(f"El número 3 está en la lista")
        print(f"Posición del número 3: {numeros.index(3)}")
    
    # Buscar elemento que no existe
    try:
        posicion = frutas.index("pera")
    except ValueError:
        print("La fruta 'pera' no está en la lista")
    
    # Contar ocurrencias
    numeros_repetidos = [1, 2, 3, 2, 4, 2, 5]
    print(f"El número 2 aparece {numeros_repetidos.count(2)} veces")
    print()
    
    # AGREGADO DE ELEMENTOS
    print("--- AGREGADO DE ELEMENTOS ---")
    
    # Agregar al final
    numeros.append(6)
    print(f"Después de append(6): {numeros}")
    
    # Agregar en posición específica
    numeros.insert(0, 0)
    print(f"Después de insert(0, 0): {numeros}")
    
    # Agregar múltiples elementos
    numeros.extend([7, 8, 9])
    print(f"Después de extend([7, 8, 9]): {numeros}")
    
    # Concatenar listas con +
    frutas_extra = ["kiwi", "mango"]
    frutas_completa = frutas + frutas_extra
    print(f"Frutas concatenadas: {frutas_completa}")
    print()
    
    # ELIMINACIÓN DE ELEMENTOS
    print("--- ELIMINACIÓN DE ELEMENTOS ---")
    
    # Eliminar por valor
    numeros.remove(0)
    print(f"Después de remove(0): {numeros}")
    
    # Eliminar por índice
    elemento_eliminado = numeros.pop(0)
    print(f"Eliminado por índice 0: {elemento_eliminado}")
    print(f"Lista resultante: {numeros}")
    
    # Eliminar último elemento
    ultimo = numeros.pop()
    print(f"Último elemento eliminado: {ultimo}")
    print(f"Lista resultante: {numeros}")
    
    # Eliminar por slice
    del numeros[1:3]
    print(f"Después de del numeros[1:3]: {numeros}")
    
    # Limpiar toda la lista
    copia_numeros = numeros.copy()
    numeros.clear()
    print(f"Después de clear(): {numeros}")
    print(f"Copia guardada: {copia_numeros}")
    print()


def ejemplos_listas_2d():
    """Ejemplos con listas bidimensionales (listas de listas)"""
    print("=" * 50)
    print("EJEMPLOS DE LISTAS BIDIMENSIONALES")
    print("=" * 50)
    
    # Crear matriz 3x3
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Matriz inicial:")
    for fila in matriz:
        print(fila)
    print()
    
    # BÚSQUEDA EN MATRIZ
    print("--- BÚSQUEDA EN MATRIZ ---")
    
    def buscar_elemento(matriz, elemento):
        """Busca un elemento en una matriz 2D"""
        for i, fila in enumerate(matriz):
            for j, valor in enumerate(fila):
                if valor == elemento:
                    return (i, j)
        return None
    
    posicion = buscar_elemento(matriz, 5)
    if posicion:
        print(f"Elemento 5 encontrado en posición: fila {posicion[0]}, columna {posicion[1]}")
    
    # Acceso directo
    print(f"Elemento en [1][1]: {matriz[1][1]}")
    print()
    
    # AGREGADO EN MATRIZ
    print("--- AGREGADO EN MATRIZ ---")
    
    # Agregar nueva fila
    matriz.append([10, 11, 12])
    print("Después de agregar fila [10, 11, 12]:")
    for fila in matriz:
        print(fila)
    print()
    
    # Agregar columna (elemento por fila)
    for i, fila in enumerate(matriz):
        fila.append(i + 13)
    print("Después de agregar columna:")
    for fila in matriz:
        print(fila)
    print()
    
    # MODIFICACIÓN EN MATRIZ
    print("--- MODIFICACIÓN EN MATRIZ ---")
    
    # Cambiar un elemento específico
    matriz[0][0] = 100
    print("Después de cambiar [0][0] a 100:")
    for fila in matriz:
        print(fila)
    print()
    
    # ELIMINACIÓN EN MATRIZ
    print("--- ELIMINACIÓN EN MATRIZ ---")
    
    # Eliminar una fila
    fila_eliminada = matriz.pop(1)
    print(f"Fila eliminada: {fila_eliminada}")
    print("Matriz después de eliminar fila 1:")
    for fila in matriz:
        print(fila)
    print()
    
    # Eliminar columna (último elemento de cada fila)
    for fila in matriz:
        if fila:  # Verificar que la fila no esté vacía
            fila.pop()
    print("Después de eliminar última columna:")
    for fila in matriz:
        print(fila)
    print()


def ejemplos_avanzados():
    """Ejemplos más avanzados con listas"""
    print("=" * 50)
    print("EJEMPLOS AVANZADOS CON LISTAS")
    print("=" * 50)
    
    # List comprehensions para búsqueda
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Encontrar números pares
    pares = [n for n in numeros if n % 2 == 0]
    print(f"Números pares: {pares}")
    
    # Encontrar índices de números pares
    indices_pares = [i for i, n in enumerate(numeros) if n % 2 == 0]
    print(f"Índices de números pares: {indices_pares}")
    
    # Filtrar con filter()
    mayores_que_5 = list(filter(lambda x: x > 5, numeros))
    print(f"Números mayores que 5: {mayores_que_5}")
    
    # Buscar múltiples elementos
    elementos_buscar = [2, 4, 6, 11]
    encontrados = [x for x in elementos_buscar if x in numeros]
    no_encontrados = [x for x in elementos_buscar if x not in numeros]
    print(f"Elementos encontrados: {encontrados}")
    print(f"Elementos no encontrados: {no_encontrados}")
    
    # Trabajar con listas anidadas
    datos = [
        ["Juan", 25, "Ingeniero"],
        ["María", 30, "Doctora"],
        ["Pedro", 28, "Profesor"]
    ]
    
    # Buscar por criterio en lista anidada
    doctores = [persona for persona in datos if persona[2] == "Doctora"]
    print(f"Doctores encontrados: {doctores}")
    
    # Extraer solo nombres
    nombres = [persona[0] for persona in datos]
    print(f"Nombres: {nombres}")
    print()


if __name__ == "__main__":
    ejemplos_listas_1d()
    ejemplos_listas_2d()
    ejemplos_avanzados()