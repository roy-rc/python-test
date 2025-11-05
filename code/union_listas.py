#!/usr/bin/env python3
"""
Ejemplos de unión de 2 o más listas de Python
- Concatenación simple
- Unión con operadores
- Métodos extend y append
- Comprensiones de listas
- Funciones de Python para unir listas
"""

def union_basica_listas():
    """Métodos básicos para unir listas"""
    print("=" * 60)
    print("MÉTODOS BÁSICOS PARA UNIR LISTAS")
    print("=" * 60)
    
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    lista3 = [7, 8, 9]
    
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Lista 3: {lista3}")
    print()
    
    # CONCATENACIÓN CON OPERADOR +
    print("--- CONCATENACIÓN CON OPERADOR + ---")
    
    # Unir dos listas
    union_dos = lista1 + lista2
    print(f"Lista1 + Lista2: {union_dos}")
    
    # Unir múltiples listas
    union_tres = lista1 + lista2 + lista3
    print(f"Lista1 + Lista2 + Lista3: {union_tres}")
    
    # Concatenación en una sola expresión
    todas_juntas = [1, 2] + [3, 4] + [5, 6] + [7, 8]
    print(f"Concatenación directa: {todas_juntas}")
    print()
    
    # MÉTODO EXTEND()
    print("--- MÉTODO EXTEND() ---")
    
    # extend() modifica la lista original
    lista_original = [1, 2, 3]
    print(f"Lista original antes de extend: {lista_original}")
    
    lista_original.extend([4, 5, 6])
    print(f"Después de extend([4, 5, 6]): {lista_original}")
    
    lista_original.extend([7, 8])
    lista_original.extend([9])
    print(f"Después de más extends: {lista_original}")
    
    # extend() con diferentes iterables
    lista_extend = [1, 2, 3]
    lista_extend.extend("abc")  # String es iterable
    print(f"Extend con string: {lista_extend}")
    
    lista_extend.extend(range(4, 7))  # Range es iterable
    print(f"Extend con range: {lista_extend}")
    print()
    
    # OPERADOR += (equivalente a extend)
    print("--- OPERADOR += ---")
    
    lista_suma = [1, 2, 3]
    print(f"Lista antes de +=: {lista_suma}")
    
    lista_suma += [4, 5, 6]
    print(f"Después de += [4, 5, 6]: {lista_suma}")
    
    lista_suma += [7]
    print(f"Después de += [7]: {lista_suma}")
    print()


def union_con_append():
    """Unión usando append en bucles"""
    print("=" * 60)
    print("UNIÓN USANDO APPEND Y BUCLES")
    print("=" * 60)
    
    listas_multiples = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    
    print("Listas a unir:")
    for i, lista in enumerate(listas_multiples):
        print(f"  Lista {i+1}: {lista}")
    print()
    
    # APPEND ELEMENTO POR ELEMENTO
    print("--- APPEND ELEMENTO POR ELEMENTO ---")
    
    resultado_append = []
    for lista in listas_multiples:
        for elemento in lista:
            resultado_append.append(elemento)
    
    print(f"Resultado con append: {resultado_append}")
    print()
    
    # APPEND DE LISTAS COMPLETAS (crea lista de listas)
    print("--- APPEND DE LISTAS COMPLETAS ---")
    
    lista_de_listas = []
    for lista in listas_multiples:
        lista_de_listas.append(lista)
    
    print(f"Lista de listas: {lista_de_listas}")
    
    # Para aplanar la lista de listas
    aplanada = []
    for sublista in lista_de_listas:
        aplanada.extend(sublista)
    
    print(f"Lista aplanada: {aplanada}")
    print()


def union_con_funciones_builtin():
    """Unión usando funciones integradas de Python"""
    print("=" * 60)
    print("UNIÓN CON FUNCIONES INTEGRADAS")
    print("=" * 60)
    
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    lista3 = [7, 8, 9]
    lista4 = ["a", "b", "c"]
    
    # USANDO SUM() PARA LISTAS
    print("--- USANDO sum() ---")
    
    listas_numericas = [lista1, lista2, lista3]
    print(f"Listas a sumar: {listas_numericas}")
    
    # sum() puede concatenar listas si se proporciona lista vacía como inicio
    resultado_sum = sum(listas_numericas, [])
    print(f"Resultado con sum(): {resultado_sum}")
    print()
    
    # USANDO itertools.chain
    print("--- USANDO itertools.chain ---")
    
    import itertools
    
    # chain() conecta iterables de forma perezosa
    todas_listas = [lista1, lista2, lista3, lista4]
    resultado_chain = list(itertools.chain(*todas_listas))
    print(f"Resultado con chain(): {resultado_chain}")
    
    # chain.from_iterable() para lista de listas
    resultado_chain_iter = list(itertools.chain.from_iterable(todas_listas))
    print(f"Resultado con chain.from_iterable(): {resultado_chain_iter}")
    print()
    
    # USANDO operator.add con functools.reduce
    print("--- USANDO functools.reduce ---")
    
    import functools
    import operator
    
    listas_numericas_solo = [lista1, lista2, lista3]
    resultado_reduce = functools.reduce(operator.add, listas_numericas_solo)
    print(f"Resultado con reduce + operator.add: {resultado_reduce}")
    
    # También se puede usar lambda
    resultado_reduce_lambda = functools.reduce(lambda x, y: x + y, listas_numericas_solo)
    print(f"Resultado con reduce + lambda: {resultado_reduce_lambda}")
    print()


def union_con_comprehensions():
    """Unión usando comprensiones de lista"""
    print("=" * 60)
    print("UNIÓN CON COMPRENSIONES DE LISTA")
    print("=" * 60)
    
    listas = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    
    print("Listas originales:")
    for i, lista in enumerate(listas):
        print(f"  Lista {i+1}: {lista}")
    print()
    
    # COMPRENSIÓN SIMPLE PARA APLANAR
    print("--- COMPRENSIÓN SIMPLE ---")
    
    aplanada = [elemento for lista in listas for elemento in lista]
    print(f"Lista aplanada: {aplanada}")
    print()
    
    # COMPRENSIÓN CON CONDICIONES
    print("--- COMPRENSIÓN CON CONDICIONES ---")
    
    # Solo elementos pares
    solo_pares = [elemento for lista in listas for elemento in lista if elemento % 2 == 0]
    print(f"Solo números pares: {solo_pares}")
    
    # Solo de las primeras dos listas
    primeras_dos = [elemento for lista in listas[:2] for elemento in lista]
    print(f"Solo primeras dos listas: {primeras_dos}")
    
    # Aplicar transformación durante la unión
    al_cuadrado = [elemento**2 for lista in listas for elemento in lista]
    print(f"Elementos al cuadrado: {al_cuadrado}")
    print()
    
    # COMPRENSIÓN ANIDADA PARA MANTENER ESTRUCTURA
    print("--- COMPRENSIÓN MANTENIENDO ESTRUCTURA ---")
    
    # Duplicar cada elemento pero mantener sublistas
    duplicados = [[elemento * 2 for elemento in lista] for lista in listas]
    print("Elementos duplicados por sublista:")
    for i, lista in enumerate(duplicados):
        print(f"  Sublista {i+1}: {lista}")
    print()


def union_con_diferentes_tipos():
    """Unión de listas con diferentes tipos de datos"""
    print("=" * 60)
    print("UNIÓN DE LISTAS CON DIFERENTES TIPOS")
    print("=" * 60)
    
    numeros = [1, 2, 3]
    strings = ["a", "b", "c"]
    mixtos = [True, 3.14, None]
    listas_anidadas = [[1, 2], [3, 4]]
    
    print(f"Números: {numeros}")
    print(f"Strings: {strings}")
    print(f"Mixtos: {mixtos}")
    print(f"Listas anidadas: {listas_anidadas}")
    print()
    
    # UNIÓN DIRECTA DE TIPOS DIFERENTES
    print("--- UNIÓN DE TIPOS DIFERENTES ---")
    
    todo_junto = numeros + strings + mixtos
    print(f"Todo junto: {todo_junto}")
    
    # Incluir listas anidadas
    con_anidadas = numeros + strings + mixtos + listas_anidadas
    print(f"Con listas anidadas: {con_anidadas}")
    print()
    
    # UNIÓN CON CONVERSIÓN DE TIPOS
    print("--- UNIÓN CON CONVERSIÓN ---")
    
    # Convertir números a strings antes de unir
    numeros_str = [str(x) for x in numeros]
    solo_strings = numeros_str + strings
    print(f"Solo strings: {solo_strings}")
    
    # Filtrar solo ciertos tipos
    solo_numeros = []
    for lista in [numeros, strings, mixtos]:
        for elemento in lista:
            if isinstance(elemento, (int, float)):
                solo_numeros.append(elemento)
    
    print(f"Solo números: {solo_numeros}")
    print()


def union_preservando_orden():
    """Ejemplos de unión preservando o alterando el orden"""
    print("=" * 60)
    print("UNIÓN PRESERVANDO/ALTERANDO ORDEN")
    print("=" * 60)
    
    lista_a = [3, 1, 4, 1, 5]
    lista_b = [9, 2, 6, 5, 3]
    lista_c = [5, 8, 9, 7, 9]
    
    print(f"Lista A: {lista_a}")
    print(f"Lista B: {lista_b}")
    print(f"Lista C: {lista_c}")
    print()
    
    # UNIÓN PRESERVANDO ORDEN ORIGINAL
    print("--- PRESERVANDO ORDEN ORIGINAL ---")
    
    union_ordenada = lista_a + lista_b + lista_c
    print(f"Unión en orden: {union_ordenada}")
    print()
    
    # UNIÓN Y ORDENAMIENTO
    print("--- UNIÓN Y ORDENAMIENTO ---")
    
    union_y_sort = sorted(lista_a + lista_b + lista_c)
    print(f"Unión y ordenamiento: {union_y_sort}")
    
    # Orden inverso
    union_inversa = sorted(lista_a + lista_b + lista_c, reverse=True)
    print(f"Unión y orden inverso: {union_inversa}")
    print()
    
    # ELIMINAR DUPLICADOS
    print("--- ELIMINANDO DUPLICADOS ---")
    
    # Mantener orden, eliminar duplicados
    sin_duplicados = []
    for elemento in (lista_a + lista_b + lista_c):
        if elemento not in sin_duplicados:
            sin_duplicados.append(elemento)
    
    print(f"Sin duplicados (orden preservado): {sin_duplicados}")
    
    # Usar set (no preserva orden)
    sin_duplicados_set = list(set(lista_a + lista_b + lista_c))
    print(f"Sin duplicados (con set): {sin_duplicados_set}")
    
    # Usar dict.fromkeys() para preservar orden (Python 3.7+)
    sin_duplicados_dict = list(dict.fromkeys(lista_a + lista_b + lista_c))
    print(f"Sin duplicados (dict.fromkeys): {sin_duplicados_dict}")
    print()


def union_con_intercalado():
    """Unión intercalando elementos de las listas"""
    print("=" * 60)
    print("UNIÓN INTERCALANDO ELEMENTOS")
    print("=" * 60)
    
    lista1 = [1, 2, 3, 4, 5]
    lista2 = ["a", "b", "c", "d"]
    lista3 = [10, 20, 30]
    
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Lista 3: {lista3}")
    print()
    
    # INTERCALADO USANDO zip
    print("--- INTERCALADO CON zip ---")
    
    # Intercalar dos listas
    intercalado_dos = []
    for a, b in zip(lista1, lista2):
        intercalado_dos.extend([a, b])
    
    print(f"Intercalado de dos listas: {intercalado_dos}")
    
    # Intercalar tres listas (hasta la más corta)
    intercalado_tres = []
    for a, b, c in zip(lista1, lista2, lista3):
        intercalado_tres.extend([a, b, c])
    
    print(f"Intercalado de tres listas: {intercalado_tres}")
    
    # Intercalado con zip_longest (hasta la más larga)
    from itertools import zip_longest
    
    intercalado_longest = []
    for elementos in zip_longest(lista1, lista2, lista3, fillvalue="X"):
        intercalado_longest.extend(elementos)
    
    print(f"Intercalado completo: {intercalado_longest}")
    print()
    
    # INTERCALADO MANUAL
    print("--- INTERCALADO MANUAL ---")
    
    def intercalar_listas(*listas):
        """Intercala elementos de múltiples listas"""
        resultado = []
        max_len = max(len(lista) for lista in listas)
        
        for i in range(max_len):
            for lista in listas:
                if i < len(lista):
                    resultado.append(lista[i])
        
        return resultado
    
    resultado_manual = intercalar_listas(lista1, lista2, lista3)
    print(f"Intercalado manual: {resultado_manual}")
    print()


if __name__ == "__main__":
    union_basica_listas()
    union_con_append()
    union_con_funciones_builtin()
    union_con_comprehensions()
    union_con_diferentes_tipos()
    union_preservando_orden()
    union_con_intercalado()