#!/usr/bin/env python3
"""
Ejemplos completos de tipos de conjuntos en Python
- set (conjuntos mutables)
- frozenset (conjuntos inmutables)
- Operadores de conjuntos (unión, intersección, diferencia)
- Métodos específicos de conjuntos
- Operaciones matemáticas de teoría de conjuntos
"""

def ejemplos_sets_basicos():
    """Ejemplos básicos de conjuntos (set)"""
    print("=" * 60)
    print("CONJUNTOS (set) - COLECCIONES NO ORDENADAS SIN DUPLICADOS")
    print("=" * 60)
    
    # Creación de conjuntos
    print("--- CREACIÓN DE CONJUNTOS ---")
    
    # Diferentes formas de crear sets
    set_vacio = set()  # {} crea dict, no set
    set_literal = {1, 2, 3, 4, 5}
    set_desde_lista = set([1, 2, 2, 3, 3, 4])  # Duplicados se eliminan
    set_desde_string = set("Python")
    set_desde_tupla = set((1, 2, 3, 2, 1))
    
    print(f"Set vacío: {set_vacio}")
    print(f"Set literal: {set_literal}")
    print(f"Desde lista con duplicados: {set_desde_lista}")
    print(f"Desde string: {set_desde_string}")
    print(f"Desde tupla: {set_desde_tupla}")
    print(f"Tipo: {type(set_literal)}")
    print()
    
    # Características principales
    print("--- CARACTERÍSTICAS PRINCIPALES ---")
    numeros = {3, 1, 4, 1, 5, 9, 2, 6, 5}
    print(f"Set con duplicados: {numeros}")
    print(f"Longitud: {len(numeros)}")
    print("• No mantiene orden de inserción")
    print("• No permite elementos duplicados")
    print("• Elementos deben ser hashables (inmutables)")
    print()
    
    # Operadores básicos
    print("--- OPERADORES BÁSICOS ---")
    frutas = {"manzana", "banana", "naranja"}
    
    print(f"Frutas: {frutas}")
    print(f"'banana' in frutas: {'banana' in frutas}")
    print(f"'uva' not in frutas: {'uva' not in frutas}")
    print(f"len(frutas): {len(frutas)}")
    
    # Los sets no soportan indexación
    print("Los sets NO soportan indexación:")
    try:
        primer_elemento = frutas[0]  # Error
    except TypeError as e:
        print(f"Error: {e}")
    print()


def metodos_sets_mutables():
    """Métodos de conjuntos mutables"""
    print("=" * 60)
    print("MÉTODOS DE CONJUNTOS MUTABLES")
    print("=" * 60)
    
    # Agregar elementos
    print("--- AGREGAR ELEMENTOS ---")
    numeros = {1, 2, 3}
    print(f"Set inicial: {numeros}")
    
    # add() - agregar un elemento
    numeros.add(4)
    print(f"Después de add(4): {numeros}")
    
    numeros.add(2)  # Elemento duplicado - no cambia nada
    print(f"Después de add(2) duplicado: {numeros}")
    
    # update() - agregar múltiples elementos
    numeros.update([5, 6, 7])
    print(f"Después de update([5, 6, 7]): {numeros}")
    
    numeros.update({8, 9}, [10, 11])  # Múltiples iterables
    print(f"Después de update múltiple: {numeros}")
    print()
    
    # Eliminar elementos
    print("--- ELIMINAR ELEMENTOS ---")
    colores = {"rojo", "verde", "azul", "amarillo", "naranja"}
    print(f"Colores iniciales: {colores}")
    
    # remove() - error si no existe
    colores.remove("verde")
    print(f"Después de remove('verde'): {colores}")
    
    try:
        colores.remove("violeta")  # Error
    except KeyError as e:
        print(f"Error con remove('violeta'): {e}")
    
    # discard() - no error si no existe
    colores.discard("azul")
    print(f"Después de discard('azul'): {colores}")
    
    colores.discard("violeta")  # No error
    print(f"Después de discard('violeta') inexistente: {colores}")
    
    # pop() - eliminar y retornar elemento arbitrario
    elemento = colores.pop()
    print(f"pop() retornó: '{elemento}', set: {colores}")
    
    # clear() - eliminar todos los elementos
    colores_copia = colores.copy()
    colores.clear()
    print(f"Después de clear(): {colores}")
    print(f"Copia guardada: {colores_copia}")
    print()


def operadores_conjuntos():
    """Operadores matemáticos de conjuntos"""
    print("=" * 60)
    print("OPERADORES MATEMÁTICOS DE CONJUNTOS")
    print("=" * 60)
    
    # Conjuntos de ejemplo
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    set_c = {1, 2, 3}
    
    print(f"Conjunto A: {set_a}")
    print(f"Conjunto B: {set_b}")
    print(f"Conjunto C: {set_c}")
    print()
    
    # UNIÓN (|)
    print("--- UNIÓN (|) ---")
    union_operador = set_a | set_b
    union_metodo = set_a.union(set_b)
    
    print(f"A | B = {union_operador}")
    print(f"A.union(B) = {union_metodo}")
    print("Elementos que están en A o B (o ambos)")
    
    # Unión múltiple
    union_multiple = set_a | set_b | set_c
    print(f"A | B | C = {union_multiple}")
    print()
    
    # INTERSECCIÓN (&)
    print("--- INTERSECCIÓN (&) ---")
    interseccion_operador = set_a & set_b
    interseccion_metodo = set_a.intersection(set_b)
    
    print(f"A & B = {interseccion_operador}")
    print(f"A.intersection(B) = {interseccion_metodo}")
    print("Elementos que están en A Y B")
    
    # Intersección múltiple
    interseccion_multiple = set_a & set_b & set_c
    print(f"A & B & C = {interseccion_multiple}")
    print()
    
    # DIFERENCIA (-)
    print("--- DIFERENCIA (-) ---")
    diferencia_a_b = set_a - set_b
    diferencia_b_a = set_b - set_a
    diferencia_metodo = set_a.difference(set_b)
    
    print(f"A - B = {diferencia_a_b}")
    print(f"B - A = {diferencia_b_a}")
    print(f"A.difference(B) = {diferencia_metodo}")
    print("A - B: elementos en A pero no en B")
    print("B - A: elementos en B pero no en A")
    print()
    
    # DIFERENCIA SIMÉTRICA (^)
    print("--- DIFERENCIA SIMÉTRICA (^) ---")
    diff_simetrica = set_a ^ set_b
    diff_simetrica_metodo = set_a.symmetric_difference(set_b)
    
    print(f"A ^ B = {diff_simetrica}")
    print(f"A.symmetric_difference(B) = {diff_simetrica_metodo}")
    print("Elementos que están en A o B, pero no en ambos")
    
    # Equivalencia con unión - intersección
    equivalente = (set_a | set_b) - (set_a & set_b)
    print(f"(A | B) - (A & B) = {equivalente}")
    print(f"Son iguales: {diff_simetrica == equivalente}")
    print()


def relaciones_conjuntos():
    """Relaciones entre conjuntos (subconjuntos, superconjuntos, etc.)"""
    print("=" * 60)
    print("RELACIONES ENTRE CONJUNTOS")
    print("=" * 60)
    
    # Conjuntos de ejemplo
    universo = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    pares = {2, 4, 6, 8, 10}
    impares = {1, 3, 5, 7, 9}
    pequeños = {1, 2, 3}
    
    print(f"Universo: {universo}")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Pequeños: {pequeños}")
    print()
    
    # SUBCONJUNTO (<=)
    print("--- SUBCONJUNTO (<=) ---")
    print(f"Pares <= Universo: {pares <= universo} (pares.issubset(universo))")
    print(f"Pequeños <= Universo: {pequeños <= universo}")
    print(f"Pequeños <= Pares: {pequeños <= pares}")
    print(f"Universo <= Pares: {universo <= pares}")
    print()
    
    # SUBCONJUNTO PROPIO (<)
    print("--- SUBCONJUNTO PROPIO (<) ---")
    print(f"Pares < Universo: {pares < universo}")
    print(f"Universo < Universo: {universo < universo}")  # False - no es propio
    print(f"Pequeños < Impares: {pequeños < impares}")
    print()
    
    # SUPERCONJUNTO (>=)
    print("--- SUPERCONJUNTO (>=) ---")
    print(f"Universo >= Pares: {universo >= pares} (universo.issuperset(pares))")
    print(f"Pares >= Pequeños: {pares >= pequeños}")
    print(f"Impares >= Pequeños: {impares >= pequeños}")
    print()
    
    # SUPERCONJUNTO PROPIO (>)
    print("--- SUPERCONJUNTO PROPIO (>) ---")
    print(f"Universo > Pares: {universo > pares}")
    print(f"Pares > Pares: {pares > pares}")  # False - no es propio
    print()
    
    # CONJUNTOS DISJUNTOS
    print("--- CONJUNTOS DISJUNTOS ---")
    print(f"Pares e Impares son disjuntos: {pares.isdisjoint(impares)}")
    print(f"Pares y Pequeños son disjuntos: {pares.isdisjoint(pequeños)}")
    
    # Verificación manual
    interseccion_pares_impares = pares & impares
    print(f"Pares & Impares = {interseccion_pares_impares}")
    print(f"Son disjuntos si intersección es vacía: {len(interseccion_pares_impares) == 0}")
    print()


def metodos_actualizacion_conjuntos():
    """Métodos de actualización in-place de conjuntos"""
    print("=" * 60)
    print("MÉTODOS DE ACTUALIZACIÓN IN-PLACE")
    print("=" * 60)
    
    # Conjuntos de ejemplo
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    
    print("--- ACTUALIZACIÓN CON UNIÓN (|=) ---")
    print(f"A inicial: {set_a}")
    print(f"B: {set_b}")
    
    set_a_copia = set_a.copy()
    set_a_copia |= set_b  # Equivale a update()
    print(f"A |= B: {set_a_copia}")
    
    set_a_copia = set_a.copy()
    set_a_copia.update(set_b)
    print(f"A.update(B): {set_a_copia}")
    print()
    
    print("--- ACTUALIZACIÓN CON INTERSECCIÓN (&=) ---")
    set_a_copia = set_a.copy()
    set_a_copia &= set_b  # Equivale a intersection_update()
    print(f"A &= B: {set_a_copia}")
    
    set_a_copia = set_a.copy()
    set_a_copia.intersection_update(set_b)
    print(f"A.intersection_update(B): {set_a_copia}")
    print()
    
    print("--- ACTUALIZACIÓN CON DIFERENCIA (-=) ---")
    set_a_copia = set_a.copy()
    set_a_copia -= set_b  # Equivale a difference_update()
    print(f"A -= B: {set_a_copia}")
    
    set_a_copia = set_a.copy()
    set_a_copia.difference_update(set_b)
    print(f"A.difference_update(B): {set_a_copia}")
    print()
    
    print("--- ACTUALIZACIÓN CON DIFERENCIA SIMÉTRICA (^=) ---")
    set_a_copia = set_a.copy()
    set_a_copia ^= set_b  # Equivale a symmetric_difference_update()
    print(f"A ^= B: {set_a_copia}")
    
    set_a_copia = set_a.copy()
    set_a_copia.symmetric_difference_update(set_b)
    print(f"A.symmetric_difference_update(B): {set_a_copia}")
    print()


def ejemplos_frozenset():
    """Ejemplos de frozenset (conjuntos inmutables)"""
    print("=" * 60)
    print("FROZENSET - CONJUNTOS INMUTABLES")
    print("=" * 60)
    
    # Creación de frozensets
    print("--- CREACIÓN DE FROZENSETS ---")
    
    frozenset_vacio = frozenset()
    frozenset_desde_lista = frozenset([1, 2, 3, 3, 4])
    frozenset_desde_set = frozenset({1, 2, 3, 4, 5})
    frozenset_desde_string = frozenset("Python")
    
    print(f"Frozenset vacío: {frozenset_vacio}")
    print(f"Desde lista: {frozenset_desde_lista}")
    print(f"Desde set: {frozenset_desde_set}")
    print(f"Desde string: {frozenset_desde_string}")
    print(f"Tipo: {type(frozenset_desde_lista)}")
    print()
    
    # Inmutabilidad
    print("--- INMUTABILIDAD ---")
    fs = frozenset([1, 2, 3, 4])
    print(f"Frozenset: {fs}")
    
    # Estos métodos NO existen en frozenset
    metodos_no_disponibles = ['add', 'remove', 'discard', 'pop', 'clear', 'update']
    print("Métodos NO disponibles en frozenset:")
    for metodo in metodos_no_disponibles:
        tiene_metodo = hasattr(fs, metodo)
        print(f"  {metodo}: {tiene_metodo}")
    print()
    
    # Operaciones disponibles (las mismas que set, pero sin modificar)
    print("--- OPERACIONES DISPONIBLES ---")
    fs1 = frozenset([1, 2, 3, 4])
    fs2 = frozenset([3, 4, 5, 6])
    
    print(f"fs1: {fs1}")
    print(f"fs2: {fs2}")
    print(f"fs1 | fs2: {fs1 | fs2}")
    print(f"fs1 & fs2: {fs1 & fs2}")
    print(f"fs1 - fs2: {fs1 - fs2}")
    print(f"fs1 ^ fs2: {fs1 ^ fs2}")
    
    # Métodos de consulta
    print(f"fs1.issubset(fs2): {fs1.issubset(fs2)}")
    print(f"fs1.isdisjoint(fs2): {fs1.isdisjoint(fs2)}")
    print(f"3 in fs1: {3 in fs1}")
    print()
    
    # Uso como clave de diccionario
    print("--- USO COMO CLAVE DE DICCIONARIO ---")
    
    # frozenset es hashable, puede ser clave de dict
    conjunto_inmutable = frozenset([1, 2, 3])
    diccionario = {conjunto_inmutable: "Conjunto de números"}
    
    print(f"Diccionario con frozenset como clave:")
    print(f"  {conjunto_inmutable}: '{diccionario[conjunto_inmutable]}'")
    
    # set NO puede ser clave porque no es hashable
    try:
        conjunto_mutable = {1, 2, 3}
        diccionario_error = {conjunto_mutable: "Error"}
    except TypeError as e:
        print(f"Error usando set como clave: {e}")
    print()


def casos_uso_practicos():
    """Casos de uso prácticos de conjuntos"""
    print("=" * 60)
    print("CASOS DE USO PRÁCTICOS")
    print("=" * 60)
    
    # Eliminar duplicados
    print("--- ELIMINAR DUPLICADOS ---")
    lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    sin_duplicados = list(set(lista_con_duplicados))
    print(f"Lista original: {lista_con_duplicados}")
    print(f"Sin duplicados: {sin_duplicados}")
    print("Nota: Se pierde el orden original")
    
    # Preservar orden mientras se eliminan duplicados
    def eliminar_duplicados_con_orden(lista):
        visto = set()
        resultado = []
        for item in lista:
            if item not in visto:
                visto.add(item)
                resultado.append(item)
        return resultado
    
    sin_duplicados_con_orden = eliminar_duplicados_con_orden(lista_con_duplicados)
    print(f"Sin duplicados (orden preservado): {sin_duplicados_con_orden}")
    print()
    
    # Análisis de datos
    print("--- ANÁLISIS DE DATOS ---")
    
    # Estudiantes en diferentes cursos
    curso_python = {"Ana", "Bob", "Carol", "David", "Eva"}
    curso_java = {"Bob", "David", "Frank", "Grace", "Helen"}
    curso_sql = {"Ana", "Carol", "Frank", "Ian", "Jack"}
    
    print(f"Curso Python: {curso_python}")
    print(f"Curso Java: {curso_java}")
    print(f"Curso SQL: {curso_sql}")
    print()
    
    # Estudiantes en al menos un curso
    todos_estudiantes = curso_python | curso_java | curso_sql
    print(f"Todos los estudiantes: {todos_estudiantes}")
    print(f"Total de estudiantes únicos: {len(todos_estudiantes)}")
    
    # Estudiantes en múltiples cursos
    python_y_java = curso_python & curso_java
    python_y_sql = curso_python & curso_sql
    java_y_sql = curso_java & curso_sql
    
    print(f"Python Y Java: {python_y_java}")
    print(f"Python Y SQL: {python_y_sql}")
    print(f"Java Y SQL: {java_y_sql}")
    
    # Estudiantes en los tres cursos
    tres_cursos = curso_python & curso_java & curso_sql
    print(f"En los tres cursos: {tres_cursos}")
    
    # Estudiantes solo en Python
    solo_python = curso_python - curso_java - curso_sql
    print(f"Solo en Python: {solo_python}")
    
    # Estudiantes en exactamente dos cursos
    exactamente_dos = (python_y_java | python_y_sql | java_y_sql) - tres_cursos
    print(f"En exactamente dos cursos: {exactamente_dos}")
    print()
    
    # Validación de permisos
    print("--- VALIDACIÓN DE PERMISOS ---")
    
    permisos_admin = {"read", "write", "delete", "execute", "admin"}
    permisos_editor = {"read", "write", "execute"}
    permisos_viewer = {"read"}
    
    def verificar_acceso(permisos_usuario, accion_requerida):
        permisos_necesarios = {
            "ver_archivo": {"read"},
            "editar_archivo": {"read", "write"},
            "ejecutar_script": {"read", "execute"},
            "eliminar_archivo": {"delete"},
            "administrar_sistema": {"admin"}
        }
        
        requeridos = permisos_necesarios.get(accion_requerida, set())
        return requeridos.issubset(permisos_usuario)
    
    usuarios = [
        ("Admin", permisos_admin),
        ("Editor", permisos_editor),
        ("Viewer", permisos_viewer)
    ]
    
    acciones = ["ver_archivo", "editar_archivo", "ejecutar_script", "eliminar_archivo", "administrar_sistema"]
    
    print("Matriz de permisos:")
    print(f"{'Usuario':<10} {'Ver':<5} {'Edit':<5} {'Exec':<5} {'Del':<5} {'Admin':<5}")
    print("-" * 40)
    
    for nombre, permisos in usuarios:
        resultados = []
        for accion in acciones:
            puede = verificar_acceso(permisos, accion)
            resultados.append("✓" if puede else "✗")
        print(f"{nombre:<10} {' '.join(f'{r:<5}' for r in resultados)}")
    print()


if __name__ == "__main__":
    ejemplos_sets_basicos()
    metodos_sets_mutables()
    operadores_conjuntos()
    relaciones_conjuntos()
    metodos_actualizacion_conjuntos()
    ejemplos_frozenset()
    casos_uso_practicos()