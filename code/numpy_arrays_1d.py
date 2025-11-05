#!/usr/bin/env python3
"""
Ejemplos de manejo de arrays unidimensionales con NumPy
- Búsqueda de elementos
- Agregado de elementos
- Eliminación de elementos
- Operaciones vectoriales
"""

import numpy as np

def crear_arrays_basicos():
    """Ejemplos de creación de arrays unidimensionales"""
    print("=" * 50)
    print("CREACIÓN DE ARRAYS UNIDIMENSIONALES")
    print("=" * 50)
    
    # Diferentes formas de crear arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.arange(10)  # 0 a 9
    arr3 = np.linspace(0, 10, 5)  # 5 números entre 0 y 10
    arr4 = np.zeros(5)
    arr5 = np.ones(5)
    arr6 = np.full(5, 7)  # Array lleno de 7s
    arr7 = np.random.randint(1, 100, 10)  # 10 números aleatorios entre 1 y 99
    
    print(f"Array básico: {arr1}")
    print(f"Array con arange: {arr2}")
    print(f"Array con linspace: {arr3}")
    print(f"Array de zeros: {arr4}")
    print(f"Array de ones: {arr5}")
    print(f"Array lleno de 7s: {arr6}")
    print(f"Array aleatorio: {arr7}")
    print(f"Tipo de datos: {arr1.dtype}")
    print(f"Forma del array: {arr1.shape}")
    print(f"Tamaño del array: {arr1.size}")
    print()


def busqueda_elementos():
    """Ejemplos de búsqueda en arrays NumPy"""
    print("=" * 50)
    print("BÚSQUEDA DE ELEMENTOS EN ARRAYS")
    print("=" * 50)
    
    arr = np.array([10, 20, 30, 40, 50, 20, 60, 70])
    print(f"Array original: {arr}")
    print()
    
    # Buscar elementos con condiciones
    print("--- BÚSQUEDA CON CONDICIONES ---")
    
    # Encontrar elementos mayores que 30
    mayores_30 = arr > 30
    print(f"Elementos > 30 (booleanos): {mayores_30}")
    print(f"Valores > 30: {arr[mayores_30]}")
    
    # Encontrar índices de elementos que cumplen condición
    indices_mayores_30 = np.where(arr > 30)
    print(f"Índices donde arr > 30: {indices_mayores_30[0]}")
    
    # Buscar elemento específico
    indices_20 = np.where(arr == 20)
    print(f"Índices donde arr == 20: {indices_20[0]}")
    
    # Verificar si existe un elemento
    existe_40 = np.any(arr == 40)
    print(f"¿Existe el valor 40?: {existe_40}")
    
    # Encontrar primer índice que cumple condición
    primer_mayor_30 = np.argmax(arr > 30)
    print(f"Primer índice donde arr > 30: {primer_mayor_30}")
    
    # Buscar elementos en un rango
    en_rango = (arr >= 20) & (arr <= 50)
    print(f"Elementos entre 20 y 50: {arr[en_rango]}")
    print()
    
    # BÚSQUEDA AVANZADA
    print("--- BÚSQUEDA AVANZADA ---")
    
    # Encontrar elementos únicos
    unicos = np.unique(arr)
    print(f"Elementos únicos: {unicos}")
    
    # Contar elementos únicos
    unicos, conteos = np.unique(arr, return_counts=True)
    print("Conteo de elementos únicos:")
    for valor, conteo in zip(unicos, conteos):
        print(f"  {valor}: {conteo} veces")
    
    # Encontrar elementos más frecuentes
    indice_max_frecuencia = np.argmax(conteos)
    elemento_mas_frecuente = unicos[indice_max_frecuencia]
    print(f"Elemento más frecuente: {elemento_mas_frecuente}")
    
    # Buscar usando searchsorted (para arrays ordenados)
    arr_ordenado = np.sort(arr)
    print(f"Array ordenado: {arr_ordenado}")
    posicion_insertar = np.searchsorted(arr_ordenado, 35)
    print(f"Posición para insertar 35: {posicion_insertar}")
    print()


def agregado_elementos():
    """Ejemplos de agregado de elementos en arrays"""
    print("=" * 50)
    print("AGREGADO DE ELEMENTOS EN ARRAYS")
    print("=" * 50)
    
    arr_original = np.array([1, 2, 3, 4, 5])
    print(f"Array original: {arr_original}")
    print()
    
    # NOTA: Los arrays NumPy tienen tamaño fijo, 
    # las operaciones de "agregado" crean nuevos arrays
    
    print("--- AGREGADO AL FINAL ---")
    
    # Agregar un elemento al final
    arr_append = np.append(arr_original, 6)
    print(f"Después de append(6): {arr_append}")
    
    # Agregar múltiples elementos
    arr_append_multi = np.append(arr_original, [6, 7, 8])
    print(f"Después de append([6, 7, 8]): {arr_append_multi}")
    print()
    
    print("--- INSERCIÓN EN POSICIONES ESPECÍFICAS ---")
    
    # Insertar en posición específica
    arr_insert = np.insert(arr_original, 2, 99)  # Insertar 99 en índice 2
    print(f"Después de insert(2, 99): {arr_insert}")
    
    # Insertar múltiples valores
    arr_insert_multi = np.insert(arr_original, [1, 3], [11, 33])
    print(f"Insertar 11 en pos 1 y 33 en pos 3: {arr_insert_multi}")
    
    # Insertar al principio
    arr_prepend = np.insert(arr_original, 0, 0)
    print(f"Insertar al principio: {arr_prepend}")
    print()
    
    print("--- CONCATENACIÓN DE ARRAYS ---")
    
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr3 = np.array([7, 8, 9])
    
    # Concatenar dos arrays
    concatenado = np.concatenate([arr1, arr2])
    print(f"Concatenar {arr1} y {arr2}: {concatenado}")
    
    # Concatenar múltiples arrays
    multi_concatenado = np.concatenate([arr1, arr2, arr3])
    print(f"Concatenar múltiples: {multi_concatenado}")
    
    # Usando hstack (horizontal stack) - equivalente para 1D
    hstack_result = np.hstack([arr1, arr2, arr3])
    print(f"Usando hstack: {hstack_result}")
    print()
    
    print("--- REPETICIÓN DE ELEMENTOS ---")
    
    # Repetir array completo
    repetido = np.tile(arr1, 3)
    print(f"Repetir {arr1} tres veces: {repetido}")
    
    # Repetir cada elemento
    repeat_elementos = np.repeat(arr1, 2)
    print(f"Repetir cada elemento 2 veces: {repeat_elementos}")
    
    # Repetir elementos diferente número de veces
    repeat_variable = np.repeat(arr1, [1, 2, 3])
    print(f"Repetir elementos [1,2,3] veces: {repeat_variable}")
    print()


def eliminacion_elementos():
    """Ejemplos de eliminación de elementos en arrays"""
    print("=" * 50)
    print("ELIMINACIÓN DE ELEMENTOS EN ARRAYS")
    print("=" * 50)
    
    arr = np.array([10, 20, 30, 40, 50, 20, 60])
    print(f"Array original: {arr}")
    print()
    
    print("--- ELIMINACIÓN POR ÍNDICE ---")
    
    # Eliminar por índice específico
    sin_indice_2 = np.delete(arr, 2)  # Elimina elemento en índice 2
    print(f"Sin elemento en índice 2: {sin_indice_2}")
    
    # Eliminar múltiples índices
    sin_indices = np.delete(arr, [0, 2, 4])  # Elimina índices 0, 2, 4
    print(f"Sin índices [0, 2, 4]: {sin_indices}")
    
    # Eliminar usando slice
    sin_slice = np.delete(arr, slice(1, 4))  # Elimina índices 1 a 3
    print(f"Sin slice [1:4]: {sin_slice}")
    print()
    
    print("--- ELIMINACIÓN POR CONDICIÓN ---")
    
    # Filtrar elementos (mantener los que cumplen condición)
    mayores_25 = arr[arr > 25]
    print(f"Solo elementos > 25: {mayores_25}")
    
    # Eliminar elementos que cumplen condición
    sin_20 = arr[arr != 20]
    print(f"Sin elementos igual a 20: {sin_20}")
    
    # Filtros más complejos
    en_rango = arr[(arr >= 20) & (arr <= 50)]
    print(f"Solo elementos entre 20 y 50: {en_rango}")
    
    # Eliminar elementos duplicados
    sin_duplicados = np.unique(arr)
    print(f"Sin duplicados: {sin_duplicados}")
    print()
    
    print("--- ELIMINACIÓN USANDO MÁSCARAS ---")
    
    # Crear máscara booleana
    mascara = (arr % 20) != 0  # Elementos no divisibles por 20
    filtrado = arr[mascara]
    print(f"Elementos no divisibles por 20: {filtrado}")
    
    # Máscara inversa
    mascara_inversa = ~mascara
    divisibles_20 = arr[mascara_inversa]
    print(f"Elementos divisibles por 20: {divisibles_20}")
    print()


def operaciones_avanzadas():
    """Operaciones avanzadas con arrays 1D"""
    print("=" * 50)
    print("OPERACIONES AVANZADAS")
    print("=" * 50)
    
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([10, 20, 30, 40, 50])
    
    # Operaciones elemento a elemento
    suma = arr1 + arr2
    producto = arr1 * arr2
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Suma elemento a elemento: {suma}")
    print(f"Producto elemento a elemento: {producto}")
    
    # Operaciones con escalares
    arr_por_10 = arr1 * 10
    arr_mas_5 = arr1 + 5
    print(f"Array 1 * 10: {arr_por_10}")
    print(f"Array 1 + 5: {arr_mas_5}")
    
    # Funciones estadísticas
    datos = np.array([1, 5, 3, 9, 2, 8, 4, 7, 6])
    print(f"\nDatos para estadísticas: {datos}")
    print(f"Suma: {np.sum(datos)}")
    print(f"Promedio: {np.mean(datos):.2f}")
    print(f"Mediana: {np.median(datos)}")
    print(f"Desviación estándar: {np.std(datos):.2f}")
    print(f"Mínimo: {np.min(datos)} (índice: {np.argmin(datos)})")
    print(f"Máximo: {np.max(datos)} (índice: {np.argmax(datos)})")
    
    # Ordenamiento
    ordenado = np.sort(datos)
    indices_ordenamiento = np.argsort(datos)
    print(f"Ordenado: {ordenado}")
    print(f"Índices de ordenamiento: {indices_ordenamiento}")
    print()


if __name__ == "__main__":
    crear_arrays_basicos()
    busqueda_elementos()
    agregado_elementos()
    eliminacion_elementos()
    operaciones_avanzadas()