#!/usr/bin/env python3
"""
Ejemplos de manejo de arrays bidimensionales con NumPy
- Búsqueda de elementos en matrices
- Agregado de filas y columnas
- Eliminación de filas y columnas
- Operaciones matriciales
"""

import numpy as np

def crear_arrays_2d():
    """Ejemplos de creación de arrays bidimensionales"""
    print("=" * 50)
    print("CREACIÓN DE ARRAYS BIDIMENSIONALES (MATRICES)")
    print("=" * 50)
    
    # Diferentes formas de crear matrices
    matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matriz2 = np.zeros((3, 4))  # 3 filas, 4 columnas
    matriz3 = np.ones((2, 5))
    matriz4 = np.full((3, 3), 7)  # Matriz 3x3 llena de 7s
    matriz5 = np.eye(4)  # Matriz identidad 4x4
    matriz6 = np.random.randint(1, 10, (3, 3))  # Matriz aleatoria 3x3
    matriz7 = np.arange(12).reshape(3, 4)  # Reshape de array 1D a 2D
    
    print("Matriz básica 3x3:")
    print(matriz1)
    print(f"Forma: {matriz1.shape}")
    print(f"Tamaño total: {matriz1.size}")
    print(f"Número de dimensiones: {matriz1.ndim}")
    print()
    
    print("Matriz de zeros 3x4:")
    print(matriz2)
    print()
    
    print("Matriz de ones 2x5:")
    print(matriz3)
    print()
    
    print("Matriz identidad 4x4:")
    print(matriz4)
    print()
    
    print("Matriz aleatoria 3x3:")
    print(matriz6)
    print()
    
    print("Matriz reshape 3x4:")
    print(matriz7)
    print()


def busqueda_elementos_2d():
    """Ejemplos de búsqueda en arrays 2D"""
    print("=" * 50)
    print("BÚSQUEDA DE ELEMENTOS EN MATRICES")
    print("=" * 50)
    
    matriz = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    
    print("Matriz original:")
    print(matriz)
    print()
    
    # ACCESO A ELEMENTOS
    print("--- ACCESO A ELEMENTOS ---")
    print(f"Elemento en [1, 2]: {matriz[1, 2]}")
    print(f"Fila 2 completa: {matriz[2, :]}")
    print(f"Columna 1 completa: {matriz[:, 1]}")
    print(f"Submatriz [0:2, 1:3]:")
    print(matriz[0:2, 1:3])
    print()
    
    # BÚSQUEDA CON CONDICIONES
    print("--- BÚSQUEDA CON CONDICIONES ---")
    
    # Elementos mayores que 8
    mayores_8 = matriz > 8
    print("Máscara booleana (elementos > 8):")
    print(mayores_8)
    print(f"Elementos > 8: {matriz[mayores_8]}")
    
    # Encontrar posiciones de elementos que cumplen condición
    filas, columnas = np.where(matriz > 8)
    print("Posiciones donde matriz > 8:")
    for f, c in zip(filas, columnas):
        print(f"  Fila {f}, Columna {c}: {matriz[f, c]}")
    print()
    
    # Buscar elemento específico
    filas_6, cols_6 = np.where(matriz == 6)
    if len(filas_6) > 0:
        print(f"Elemento 6 encontrado en: fila {filas_6[0]}, columna {cols_6[0]}")
    
    # Verificar si existe un elemento
    existe_15 = np.any(matriz == 15)
    print(f"¿Existe el valor 15?: {existe_15}")
    
    # Encontrar elementos en rango
    en_rango = (matriz >= 5) & (matriz <= 10)
    print(f"Elementos entre 5 y 10: {matriz[en_rango]}")
    print()
    
    # BÚSQUEDA POR FILAS Y COLUMNAS
    print("--- BÚSQUEDA POR FILAS Y COLUMNAS ---")
    
    # Encontrar fila con valor máximo en cada columna
    max_por_columna = np.argmax(matriz, axis=0)
    print(f"Fila con máximo en cada columna: {max_por_columna}")
    
    # Encontrar columna con valor máximo en cada fila
    max_por_fila = np.argmax(matriz, axis=1)
    print(f"Columna con máximo en cada fila: {max_por_fila}")
    
    # Valor máximo global y su posición
    pos_max_global = np.unravel_index(np.argmax(matriz), matriz.shape)
    print(f"Posición del máximo global: fila {pos_max_global[0]}, columna {pos_max_global[1]}")
    print(f"Valor máximo: {matriz[pos_max_global]}")
    print()


def agregado_elementos_2d():
    """Ejemplos de agregado en arrays 2D"""
    print("=" * 50)
    print("AGREGADO DE ELEMENTOS EN MATRICES")
    print("=" * 50)
    
    matriz = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    
    print("Matriz original:")
    print(matriz)
    print(f"Forma: {matriz.shape}")
    print()
    
    # AGREGAR FILAS
    print("--- AGREGAR FILAS ---")
    
    # Agregar una fila al final
    nueva_fila = np.array([[7, 8, 9]])
    matriz_con_fila = np.append(matriz, nueva_fila, axis=0)
    print("Después de agregar fila [7, 8, 9]:")
    print(matriz_con_fila)
    print()
    
    # Agregar múltiples filas
    nuevas_filas = np.array([[10, 11, 12], [13, 14, 15]])
    matriz_con_filas = np.append(matriz, nuevas_filas, axis=0)
    print("Después de agregar múltiples filas:")
    print(matriz_con_filas)
    print()
    
    # Insertar fila en posición específica
    fila_insertar = np.array([[0, 0, 0]])
    matriz_insert_fila = np.insert(matriz, 1, fila_insertar, axis=0)
    print("Insertar fila de zeros en posición 1:")
    print(matriz_insert_fila)
    print()
    
    # AGREGAR COLUMNAS
    print("--- AGREGAR COLUMNAS ---")
    
    # Agregar una columna al final
    nueva_columna = np.array([[10], [11]])
    matriz_con_col = np.append(matriz, nueva_columna, axis=1)
    print("Después de agregar columna [10, 11]:")
    print(matriz_con_col)
    print()
    
    # Agregar múltiples columnas
    nuevas_columnas = np.array([[10, 20], [11, 21]])
    matriz_con_cols = np.append(matriz, nuevas_columnas, axis=1)
    print("Después de agregar múltiples columnas:")
    print(matriz_con_cols)
    print()
    
    # Insertar columna en posición específica
    columna_insertar = np.array([[0], [0]])
    matriz_insert_col = np.insert(matriz, 1, columna_insertar, axis=1)
    print("Insertar columna de zeros en posición 1:")
    print(matriz_insert_col)
    print()
    
    # CONCATENACIÓN DE MATRICES
    print("--- CONCATENACIÓN DE MATRICES ---")
    
    matriz_a = np.array([[1, 2], [3, 4]])
    matriz_b = np.array([[5, 6], [7, 8]])
    
    # Concatenar verticalmente (apilar filas)
    concat_vertical = np.concatenate([matriz_a, matriz_b], axis=0)
    # También se puede usar: np.vstack([matriz_a, matriz_b])
    print("Concatenación vertical:")
    print(concat_vertical)
    print()
    
    # Concatenar horizontalmente (apilar columnas)
    concat_horizontal = np.concatenate([matriz_a, matriz_b], axis=1)
    # También se puede usar: np.hstack([matriz_a, matriz_b])
    print("Concatenación horizontal:")
    print(concat_horizontal)
    print()
    
    # Usar vstack y hstack explícitamente
    vstack_result = np.vstack([matriz_a, matriz_b])
    hstack_result = np.hstack([matriz_a, matriz_b])
    print("Usando vstack:")
    print(vstack_result)
    print("Usando hstack:")
    print(hstack_result)
    print()


def eliminacion_elementos_2d():
    """Ejemplos de eliminación en arrays 2D"""
    print("=" * 50)
    print("ELIMINACIÓN DE ELEMENTOS EN MATRICES")
    print("=" * 50)
    
    matriz = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    
    print("Matriz original:")
    print(matriz)
    print()
    
    # ELIMINAR FILAS
    print("--- ELIMINAR FILAS ---")
    
    # Eliminar fila por índice
    sin_fila_1 = np.delete(matriz, 1, axis=0)
    print("Sin fila índice 1:")
    print(sin_fila_1)
    print()
    
    # Eliminar múltiples filas
    sin_filas = np.delete(matriz, [0, 2], axis=0)
    print("Sin filas índices 0 y 2:")
    print(sin_filas)
    print()
    
    # ELIMINAR COLUMNAS
    print("--- ELIMINAR COLUMNAS ---")
    
    # Eliminar columna por índice
    sin_col_2 = np.delete(matriz, 2, axis=1)
    print("Sin columna índice 2:")
    print(sin_col_2)
    print()
    
    # Eliminar múltiples columnas
    sin_cols = np.delete(matriz, [1, 3], axis=1)
    print("Sin columnas índices 1 y 3:")
    print(sin_cols)
    print()
    
    # FILTRADO POR CONDICIONES
    print("--- FILTRADO POR CONDICIONES ---")
    
    # Mantener solo filas donde la suma > 20
    sumas_filas = np.sum(matriz, axis=1)
    print(f"Suma por fila: {sumas_filas}")
    filas_suma_mayor_20 = matriz[sumas_filas > 20]
    print("Filas con suma > 20:")
    print(filas_suma_mayor_20)
    print()
    
    # Mantener solo columnas donde el máximo > 10
    max_columnas = np.max(matriz, axis=0)
    print(f"Máximo por columna: {max_columnas}")
    cols_max_mayor_10 = matriz[:, max_columnas > 10]
    print("Columnas con máximo > 10:")
    print(cols_max_mayor_10)
    print()
    
    # FILTRADO DE ELEMENTOS ESPECÍFICOS
    print("--- FILTRADO DE ELEMENTOS ---")
    
    # Reemplazar elementos que cumplen condición
    matriz_copia = matriz.copy()
    matriz_copia[matriz_copia < 8] = 0  # Reemplazar < 8 por 0
    print("Matriz con elementos < 8 reemplazados por 0:")
    print(matriz_copia)
    print()
    
    # Mantener solo elementos en cierto rango
    matriz_filtrada = np.where((matriz >= 5) & (matriz <= 12), matriz, 0)
    print("Mantener solo elementos entre 5 y 12 (otros = 0):")
    print(matriz_filtrada)
    print()


def operaciones_matriciales():
    """Operaciones avanzadas con matrices"""
    print("=" * 50)
    print("OPERACIONES AVANZADAS CON MATRICES")
    print("=" * 50)
    
    matriz_a = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    
    matriz_b = np.array([
        [7, 8],
        [9, 10],
        [11, 12]
    ])
    
    print("Matriz A (2x3):")
    print(matriz_a)
    print("\nMatriz B (3x2):")
    print(matriz_b)
    print()
    
    # Multiplicación de matrices
    producto_matricial = np.dot(matriz_a, matriz_b)  # o matriz_a @ matriz_b
    print("Producto matricial A × B:")
    print(producto_matricial)
    print()
    
    # Transposición
    matriz_t = matriz_a.T
    print("Transposición de A:")
    print(matriz_t)
    print()
    
    # Operaciones estadísticas por ejes
    matriz_datos = np.random.randint(1, 10, (4, 3))
    print("Matriz de datos aleatorios:")
    print(matriz_datos)
    print(f"Suma total: {np.sum(matriz_datos)}")
    print(f"Suma por filas: {np.sum(matriz_datos, axis=1)}")
    print(f"Suma por columnas: {np.sum(matriz_datos, axis=0)}")
    print(f"Promedio por filas: {np.mean(matriz_datos, axis=1)}")
    print(f"Promedio por columnas: {np.mean(matriz_datos, axis=0)}")
    print()
    
    # Reshape y flatten
    print("--- RESHAPE Y FLATTEN ---")
    matriz_cuadrada = np.arange(12).reshape(3, 4)
    print("Matriz 3x4:")
    print(matriz_cuadrada)
    
    # Cambiar forma
    matriz_2x6 = matriz_cuadrada.reshape(2, 6)
    print("Reshape a 2x6:")
    print(matriz_2x6)
    
    # Aplanar matriz
    aplanada = matriz_cuadrada.flatten()
    print(f"Matriz aplanada: {aplanada}")
    
    # Reshape a 1D automático
    auto_1d = matriz_cuadrada.reshape(-1)
    print(f"Reshape automático a 1D: {auto_1d}")
    print()


if __name__ == "__main__":
    crear_arrays_2d()
    busqueda_elementos_2d()
    agregado_elementos_2d()
    eliminacion_elementos_2d()
    operaciones_matriciales()