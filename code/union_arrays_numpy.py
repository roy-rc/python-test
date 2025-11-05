#!/usr/bin/env python3
"""
Ejemplos de unión de 2 o más arrays de NumPy
- Concatenación en diferentes ejes
- Apilamiento vertical y horizontal
- Unión de arrays de diferentes dimensiones
- Operaciones avanzadas de combinación
"""

import numpy as np

def union_basica_arrays():
    """Métodos básicos para unir arrays de NumPy"""
    print("=" * 60)
    print("MÉTODOS BÁSICOS PARA UNIR ARRAYS NUMPY")
    print("=" * 60)
    
    # Arrays unidimensionales
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr3 = np.array([7, 8, 9])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Array 3: {arr3}")
    print()
    
    # CONCATENACIÓN BÁSICA
    print("--- CONCATENACIÓN BÁSICA ---")
    
    # Concatenar dos arrays
    concat_dos = np.concatenate([arr1, arr2])
    print(f"Concatenar arr1 y arr2: {concat_dos}")
    
    # Concatenar múltiples arrays
    concat_tres = np.concatenate([arr1, arr2, arr3])
    print(f"Concatenar tres arrays: {concat_tres}")
    
    # Especificar eje explícitamente (para 1D, axis=0)
    concat_axis0 = np.concatenate([arr1, arr2, arr3], axis=0)
    print(f"Concatenar en axis=0: {concat_axis0}")
    print()
    
    # USANDO r_ y c_
    print("--- USANDO r_ y c_ ---")
    
    # r_ concatena a lo largo del primer eje
    using_r = np.r_[arr1, arr2, arr3]
    print(f"Usando r_: {using_r}")
    
    # c_ apila como columnas (convierte a 2D)
    using_c = np.c_[arr1, arr2, arr3]
    print("Usando c_:")
    print(using_c)
    print()


def union_arrays_2d():
    """Unión de arrays bidimensionales"""
    print("=" * 60)
    print("UNIÓN DE ARRAYS BIDIMENSIONALES")
    print("=" * 60)
    
    # Arrays 2D
    matriz1 = np.array([[1, 2], [3, 4]])
    matriz2 = np.array([[5, 6], [7, 8]])
    matriz3 = np.array([[9, 10], [11, 12]])
    
    print("Matriz 1:")
    print(matriz1)
    print("\nMatriz 2:")
    print(matriz2)
    print("\nMatriz 3:")
    print(matriz3)
    print()
    
    # CONCATENACIÓN VERTICAL (axis=0)
    print("--- CONCATENACIÓN VERTICAL (FILAS) ---")
    
    concat_vertical = np.concatenate([matriz1, matriz2], axis=0)
    print("Concatenación vertical (axis=0):")
    print(concat_vertical)
    
    # Tres matrices verticalmente
    concat_tres_vertical = np.concatenate([matriz1, matriz2, matriz3], axis=0)
    print("\nTres matrices verticalmente:")
    print(concat_tres_vertical)
    print()
    
    # CONCATENACIÓN HORIZONTAL (axis=1)
    print("--- CONCATENACIÓN HORIZONTAL (COLUMNAS) ---")
    
    concat_horizontal = np.concatenate([matriz1, matriz2], axis=1)
    print("Concatenación horizontal (axis=1):")
    print(concat_horizontal)
    
    # Tres matrices horizontalmente
    concat_tres_horizontal = np.concatenate([matriz1, matriz2, matriz3], axis=1)
    print("\nTres matrices horizontalmente:")
    print(concat_tres_horizontal)
    print()


def apilamiento_arrays():
    """Ejemplos de apilamiento de arrays"""
    print("=" * 60)
    print("APILAMIENTO DE ARRAYS")
    print("=" * 60)
    
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr3 = np.array([7, 8, 9])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Array 3: {arr3}")
    print()
    
    # VSTACK (VERTICAL STACK)
    print("--- VSTACK (APILAMIENTO VERTICAL) ---")
    
    vstack_result = np.vstack([arr1, arr2, arr3])
    print("vstack result:")
    print(vstack_result)
    print(f"Forma: {vstack_result.shape}")
    print()
    
    # HSTACK (HORIZONTAL STACK)
    print("--- HSTACK (APILAMIENTO HORIZONTAL) ---")
    
    hstack_result = np.hstack([arr1, arr2, arr3])
    print(f"hstack result: {hstack_result}")
    print(f"Forma: {hstack_result.shape}")
    print()
    
    # DSTACK (DEPTH STACK - 3D)
    print("--- DSTACK (APILAMIENTO EN PROFUNDIDAD) ---")
    
    dstack_result = np.dstack([arr1, arr2, arr3])
    print("dstack result:")
    print(dstack_result)
    print(f"Forma: {dstack_result.shape}")
    print()
    
    # STACK CON AXIS PERSONALIZADO
    print("--- STACK CON AXIS PERSONALIZADO ---")
    
    # Apilar en nueva dimensión (axis=0)
    stack_axis0 = np.stack([arr1, arr2, arr3], axis=0)
    print("stack axis=0:")
    print(stack_axis0)
    print(f"Forma: {stack_axis0.shape}")
    
    # Apilar en nueva dimensión (axis=1)
    stack_axis1 = np.stack([arr1, arr2, arr3], axis=1)
    print("\nstack axis=1:")
    print(stack_axis1)
    print(f"Forma: {stack_axis1.shape}")
    
    # Apilar en nueva dimensión (axis=-1)
    stack_axis_minus1 = np.stack([arr1, arr2, arr3], axis=-1)
    print("\nstack axis=-1:")
    print(stack_axis_minus1)
    print(f"Forma: {stack_axis_minus1.shape}")
    print()


def union_arrays_diferentes_dimensiones():
    """Unión de arrays con diferentes dimensiones"""
    print("=" * 60)
    print("UNIÓN DE ARRAYS CON DIFERENTES DIMENSIONES")
    print("=" * 60)
    
    # Arrays de diferentes formas
    arr_1d = np.array([1, 2, 3])
    arr_2d = np.array([[4, 5, 6]])
    arr_2d_vertical = np.array([[7], [8], [9]])
    
    print(f"Array 1D: {arr_1d}, forma: {arr_1d.shape}")
    print(f"Array 2D horizontal: {arr_2d}, forma: {arr_2d.shape}")
    print(f"Array 2D vertical:\n{arr_2d_vertical}, forma: {arr_2d_vertical.shape}")
    print()
    
    # EXPANDIR DIMENSIONES
    print("--- EXPANDIR DIMENSIONES ---")
    
    # Expandir arr_1d para que sea compatible
    arr_1d_expanded = np.expand_dims(arr_1d, axis=0)
    print(f"Array 1D expandido: {arr_1d_expanded}, forma: {arr_1d_expanded.shape}")
    
    # Ahora se pueden concatenar
    concat_compatible = np.concatenate([arr_1d_expanded, arr_2d], axis=0)
    print("Concatenación después de expandir:")
    print(concat_compatible)
    print()
    
    # USAR RESHAPE PARA COMPATIBILIDAD
    print("--- USAR RESHAPE PARA COMPATIBILIDAD ---")
    
    # Reshape para hacer compatible con concatenación vertical
    arr_1d_reshaped = arr_1d.reshape(1, -1)
    print(f"Array 1D reshaped: {arr_1d_reshaped}, forma: {arr_1d_reshaped.shape}")
    
    concat_reshaped = np.vstack([arr_1d_reshaped, arr_2d])
    print("Concatenación con reshape:")
    print(concat_reshaped)
    print()
    
    # BROADCASTING PARA UNIÓN
    print("--- BROADCASTING PARA UNIÓN ---")
    
    # Crear arrays con broadcasting
    arr_broadcast_1 = np.ones((3, 1))
    arr_broadcast_2 = np.array([1, 2, 3])
    
    print(f"Array 1 (3,1): \n{arr_broadcast_1}")
    print(f"Array 2 (3,): {arr_broadcast_2}")
    
    # Suma con broadcasting
    suma_broadcast = arr_broadcast_1 + arr_broadcast_2
    print("Suma con broadcasting:")
    print(suma_broadcast)
    print()


def union_con_mascaras():
    """Unión de arrays usando máscaras y condiciones"""
    print("=" * 60)
    print("UNIÓN CON MÁSCARAS Y CONDICIONES")
    print("=" * 60)
    
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([6, 7, 8, 9, 10])
    arr3 = np.array([11, 12, 13, 14, 15])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Array 3: {arr3}")
    print()
    
    # CONCATENAR SOLO ELEMENTOS QUE CUMPLEN CONDICIÓN
    print("--- CONCATENAR CON CONDICIONES ---")
    
    # Solo elementos pares de cada array
    pares_arr1 = arr1[arr1 % 2 == 0]
    pares_arr2 = arr2[arr2 % 2 == 0]
    pares_arr3 = arr3[arr3 % 2 == 0]
    
    print(f"Pares de arr1: {pares_arr1}")
    print(f"Pares de arr2: {pares_arr2}")
    print(f"Pares de arr3: {pares_arr3}")
    
    todos_los_pares = np.concatenate([pares_arr1, pares_arr2, pares_arr3])
    print(f"Todos los pares concatenados: {todos_los_pares}")
    print()
    
    # USAR WHERE PARA SELECCIONAR Y UNIR
    print("--- USAR WHERE PARA UNIR ---")
    
    # Crear condición compleja
    condicion1 = arr1 > 2
    condicion2 = arr2 < 9
    
    filtrado1 = arr1[condicion1]
    filtrado2 = arr2[condicion2]
    
    print(f"arr1 > 2: {filtrado1}")
    print(f"arr2 < 9: {filtrado2}")
    
    union_filtrada = np.concatenate([filtrado1, filtrado2])
    print(f"Unión filtrada: {union_filtrada}")
    print()


def union_con_funciones_avanzadas():
    """Unión usando funciones avanzadas de NumPy"""
    print("=" * 60)
    print("FUNCIONES AVANZADAS PARA UNIÓN")
    print("=" * 60)
    
    # Arrays de ejemplo
    arr1 = np.array([1, 3, 5, 7])
    arr2 = np.array([2, 4, 6, 8])
    arr3 = np.array([9, 10, 11, 12])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Array 3: {arr3}")
    print()
    
    # INTERLEAVE (INTERCALAR)
    print("--- INTERCALAR ARRAYS ---")
    
    def intercalar_arrays(arr_a, arr_b):
        """Intercala elementos de dos arrays"""
        resultado = np.empty(arr_a.size + arr_b.size, dtype=arr_a.dtype)
        resultado[0::2] = arr_a
        resultado[1::2] = arr_b
        return resultado
    
    intercalado = intercalar_arrays(arr1, arr2)
    print(f"Arrays intercalados: {intercalado}")
    print()
    
    # APPEND (SIMILAR A CONCATENATE)
    print("--- USANDO np.append ---")
    
    append_result = np.append(arr1, arr2)
    print(f"np.append result: {append_result}")
    
    # Append múltiple
    for arr in [arr2, arr3]:
        append_result = np.append(append_result, arr)
    print(f"Append múltiple: {append_result}")
    print()
    
    # INSERT EN POSICIONES ESPECÍFICAS
    print("--- INSERT EN POSICIONES ESPECÍFICAS ---")
    
    # Insertar arr2 en posición 2 de arr1
    insert_result = np.insert(arr1, 2, arr2)
    print(f"Insert arr2 en posición 2 de arr1: {insert_result}")
    
    # Insert con índices específicos
    insert_indices = np.insert(arr1, [1, 3], [99, 88])
    print(f"Insert valores en índices específicos: {insert_indices}")
    print()


def union_arrays_complejos():
    """Unión de arrays con tipos de datos complejos"""
    print("=" * 60)
    print("UNIÓN DE ARRAYS CON TIPOS COMPLEJOS")
    print("=" * 60)
    
    # Arrays con diferentes tipos de datos
    arr_int = np.array([1, 2, 3], dtype=np.int32)
    arr_float = np.array([4.5, 5.5, 6.5], dtype=np.float64)
    arr_complex = np.array([1+2j, 2+3j], dtype=np.complex128)
    
    print(f"Array int: {arr_int}, dtype: {arr_int.dtype}")
    print(f"Array float: {arr_float}, dtype: {arr_float.dtype}")
    print(f"Array complex: {arr_complex}, dtype: {arr_complex.dtype}")
    print()
    
    # CONCATENACIÓN CON PROMOCIÓN DE TIPO
    print("--- CONCATENACIÓN CON PROMOCIÓN DE TIPO ---")
    
    # NumPy automáticamente promociona tipos
    concat_int_float = np.concatenate([arr_int, arr_float])
    print(f"int + float: {concat_int_float}, dtype: {concat_int_float.dtype}")
    
    # Convertir explícitamente si es necesario
    arr_int_as_float = arr_int.astype(np.float64)
    concat_explicit = np.concatenate([arr_int_as_float, arr_float])
    print(f"Conversión explícita: {concat_explicit}, dtype: {concat_explicit.dtype}")
    print()
    
    # ARRAYS ESTRUCTURADOS
    print("--- ARRAYS ESTRUCTURADOS ---")
    
    # Crear arrays estructurados
    dtype_persona = [('nombre', 'U10'), ('edad', 'i4'), ('altura', 'f4')]
    
    personas1 = np.array([('Juan', 25, 1.75), ('María', 30, 1.68)], dtype=dtype_persona)
    personas2 = np.array([('Pedro', 28, 1.80), ('Ana', 22, 1.65)], dtype=dtype_persona)
    
    print("Personas 1:")
    print(personas1)
    print("\nPersonas 2:")
    print(personas2)
    
    # Concatenar arrays estructurados
    todas_personas = np.concatenate([personas1, personas2])
    print("\nTodas las personas:")
    print(todas_personas)
    print()


def union_con_repeticion():
    """Unión con repetición de arrays"""
    print("=" * 60)
    print("UNIÓN CON REPETICIÓN DE ARRAYS")
    print("=" * 60)
    
    arr_base = np.array([1, 2, 3])
    print(f"Array base: {arr_base}")
    print()
    
    # TILE (REPETIR ARRAY COMPLETO)
    print("--- TILE (REPETIR ARRAY) ---")
    
    # Repetir 3 veces
    tile_simple = np.tile(arr_base, 3)
    print(f"Tile simple (3 veces): {tile_simple}")
    
    # Repetir en forma 2D
    tile_2d = np.tile(arr_base, (2, 3))
    print("Tile 2D (2 filas, 3 repeticiones):")
    print(tile_2d)
    print()
    
    # REPEAT (REPETIR CADA ELEMENTO)
    print("--- REPEAT (REPETIR ELEMENTOS) ---")
    
    # Repetir cada elemento 2 veces
    repeat_uniform = np.repeat(arr_base, 2)
    print(f"Repeat uniforme: {repeat_uniform}")
    
    # Repetir cada elemento diferente número de veces
    repeat_variable = np.repeat(arr_base, [1, 3, 2])
    print(f"Repeat variable: {repeat_variable}")
    
    # Repeat en eje específico (para arrays 2D)
    arr_2d = np.array([[1, 2], [3, 4]])
    repeat_axis0 = np.repeat(arr_2d, 2, axis=0)
    repeat_axis1 = np.repeat(arr_2d, 2, axis=1)
    
    print("\nArray 2D original:")
    print(arr_2d)
    print("Repeat en axis=0:")
    print(repeat_axis0)
    print("Repeat en axis=1:")
    print(repeat_axis1)
    print()


if __name__ == "__main__":
    union_basica_arrays()
    union_arrays_2d()
    apilamiento_arrays()
    union_arrays_diferentes_dimensiones()
    union_con_mascaras()
    union_con_funciones_avanzadas()
    union_arrays_complejos()
    union_con_repeticion()