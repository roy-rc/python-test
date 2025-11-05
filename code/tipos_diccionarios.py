#!/usr/bin/env python3
"""
Ejemplos completos de diccionarios (dict) en Python
- Creación y manipulación de diccionarios
- Operadores y métodos de diccionarios
- Acceso, modificación y eliminación de elementos
- Métodos de vistas (keys(), values(), items())
- Comprensiones de diccionarios
- Casos de uso avanzados
"""

def creacion_diccionarios():
    """Ejemplos de creación de diccionarios"""
    print("=" * 60)
    print("DICCIONARIOS (dict) - MAPEO DE CLAVE-VALOR")
    print("=" * 60)
    
    # Diferentes formas de crear diccionarios
    print("--- CREACIÓN DE DICCIONARIOS ---")
    
    # Diccionario vacío
    dict_vacio = {}
    dict_vacio_alt = dict()
    
    # Diccionario literal
    dict_literal = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
    
    # Constructor dict() con argumentos con nombre
    dict_constructor = dict(nombre="Ana", edad=30, ciudad="Barcelona")
    
    # Constructor dict() desde lista de tuplas
    dict_desde_tuplas = dict([("a", 1), ("b", 2), ("c", 3)])
    
    # Constructor dict() desde zip
    claves = ["x", "y", "z"]
    valores = [10, 20, 30]
    dict_desde_zip = dict(zip(claves, valores))
    
    # Diccionario con comprehension
    dict_comprehension = {x: x**2 for x in range(5)}
    
    # Diccionario anidado
    dict_anidado = {
        "persona1": {"nombre": "Juan", "edad": 25},
        "persona2": {"nombre": "Ana", "edad": 30}
    }
    
    print(f"Vacío: {dict_vacio}")
    print(f"Literal: {dict_literal}")
    print(f"Constructor: {dict_constructor}")
    print(f"Desde tuplas: {dict_desde_tuplas}")
    print(f"Desde zip: {dict_desde_zip}")
    print(f"Comprehension: {dict_comprehension}")
    print(f"Anidado: {dict_anidado}")
    print(f"Tipo: {type(dict_literal)}")
    print()
    
    # Características importantes
    print("--- CARACTERÍSTICAS ---")
    print("• Claves deben ser inmutables (hashables)")
    print("• Valores pueden ser cualquier tipo")
    print("• Mantiene orden de inserción (Python 3.7+)")
    print("• Claves únicas (no duplicadas)")
    print()


def acceso_y_modificacion():
    """Acceso y modificación de elementos en diccionarios"""
    print("=" * 60)
    print("ACCESO Y MODIFICACIÓN")
    print("=" * 60)
    
    # Diccionario de ejemplo
    estudiante = {
        "nombre": "María",
        "edad": 22,
        "carrera": "Ingeniería",
        "notas": [8.5, 9.0, 7.5, 8.8]
    }
    
    print(f"Estudiante: {estudiante}")
    print()
    
    # ACCESO A ELEMENTOS
    print("--- ACCESO A ELEMENTOS ---")
    
    # Acceso directo con []
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad: {estudiante['edad']}")
    
    # Acceso seguro con get()
    print(f"Carrera: {estudiante.get('carrera')}")
    print(f"Teléfono: {estudiante.get('telefono')}")  # None si no existe
    print(f"Teléfono: {estudiante.get('telefono', 'No disponible')}")  # Valor por defecto
    
    # Error al acceder clave inexistente
    try:
        telefono = estudiante["telefono"]  # KeyError
    except KeyError as e:
        print(f"Error de acceso: {e}")
    print()
    
    # MODIFICACIÓN DE ELEMENTOS
    print("--- MODIFICACIÓN DE ELEMENTOS ---")
    
    print("Estado original:")
    print(f"  Edad: {estudiante['edad']}")
    
    # Modificar elemento existente
    estudiante["edad"] = 23
    print(f"Después de modificar edad: {estudiante['edad']}")
    
    # Agregar nuevo elemento
    estudiante["telefono"] = "123-456-789"
    print(f"Después de agregar teléfono: {estudiante.get('telefono')}")
    
    # Modificar elementos anidados
    estudiante["notas"].append(9.2)
    print(f"Después de agregar nota: {estudiante['notas']}")
    
    print(f"Estudiante actualizado: {estudiante}")
    print()
    
    # VERIFICACIÓN DE EXISTENCIA
    print("--- VERIFICACIÓN DE EXISTENCIA ---")
    
    claves_buscar = ["nombre", "edad", "telefono", "direccion"]
    
    for clave in claves_buscar:
        # Operador in
        existe_in = clave in estudiante
        
        # Método has_key() (no existe en Python 3)
        # existe_has_key = estudiante.has_key(clave)  # Deprecated
        
        print(f"'{clave}' in estudiante: {existe_in}")
    
    # También se puede verificar en las claves
    print(f"'nombre' in estudiante.keys(): {'nombre' in estudiante.keys()}")
    print()


def metodos_diccionarios():
    """Métodos importantes de diccionarios"""
    print("=" * 60)
    print("MÉTODOS DE DICCIONARIOS")
    print("=" * 60)
    
    # Diccionario de ejemplo
    colores = {"rojo": "#FF0000", "verde": "#00FF00", "azul": "#0000FF"}
    print(f"Colores originales: {colores}")
    print()
    
    # MÉTODOS DE VISTA
    print("--- MÉTODOS DE VISTA ---")
    
    claves = colores.keys()
    valores = colores.values()
    items = colores.items()
    
    print(f"keys(): {list(claves)}")
    print(f"values(): {list(valores)}")
    print(f"items(): {list(items)}")
    
    # Las vistas son dinámicas
    print("\nLas vistas son dinámicas:")
    print(f"Claves antes: {list(claves)}")
    colores["amarillo"] = "#FFFF00"
    print(f"Claves después de agregar: {list(claves)}")
    print()
    
    # MÉTODO UPDATE()
    print("--- MÉTODO update() ---")
    
    colores_adicionales = {"naranja": "#FFA500", "violeta": "#800080"}
    print(f"Antes de update: {colores}")
    print(f"Agregando: {colores_adicionales}")
    
    colores.update(colores_adicionales)
    print(f"Después de update: {colores}")
    
    # update() con argumentos con nombre
    colores.update(negro="#000000", blanco="#FFFFFF")
    print(f"Después de update con kwargs: {colores}")
    print()
    
    # MÉTODOS DE ELIMINACIÓN
    print("--- MÉTODOS DE ELIMINACIÓN ---")
    
    inventario = {"manzanas": 50, "naranjas": 30, "plátanos": 20, "uvas": 15}
    print(f"Inventario inicial: {inventario}")
    
    # pop() - eliminar y retornar valor
    manzanas = inventario.pop("manzanas")
    print(f"pop('manzanas') retornó: {manzanas}")
    print(f"Inventario después: {inventario}")
    
    # pop() con valor por defecto
    kiwis = inventario.pop("kiwis", 0)
    print(f"pop('kiwis', 0) retornó: {kiwis}")
    
    # popitem() - eliminar y retornar último elemento (Python 3.7+)
    ultimo_item = inventario.popitem()
    print(f"popitem() retornó: {ultimo_item}")
    print(f"Inventario después: {inventario}")
    
    # del - eliminar elemento
    del inventario["naranjas"]
    print(f"Después de del inventario['naranjas']: {inventario}")
    
    # clear() - eliminar todos los elementos
    inventario_copia = inventario.copy()
    inventario.clear()
    print(f"Después de clear(): {inventario}")
    print(f"Copia guardada: {inventario_copia}")
    print()
    
    # OTROS MÉTODOS ÚTILES
    print("--- OTROS MÉTODOS ---")
    
    configuracion = {"host": "localhost", "puerto": 8080, "debug": False}
    print(f"Configuración: {configuracion}")
    
    # copy() - copia superficial
    copia_config = configuracion.copy()
    print(f"Copia: {copia_config}")
    
    # setdefault() - obtener o establecer valor por defecto
    puerto_db = configuracion.setdefault("puerto_db", 5432)
    print(f"setdefault('puerto_db', 5432): {puerto_db}")
    print(f"Configuración actualizada: {configuracion}")
    
    # Intentar setdefault con clave existente
    host_actual = configuracion.setdefault("host", "127.0.0.1")
    print(f"setdefault('host', '127.0.0.1'): {host_actual}")
    print(f"Host no cambió: {configuracion['host']}")
    print()


def operadores_diccionarios():
    """Operadores que funcionan con diccionarios"""
    print("=" * 60)
    print("OPERADORES CON DICCIONARIOS")
    print("=" * 60)
    
    # Diccionarios de ejemplo
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"c": 30, "d": 4, "e": 5}
    dict3 = {"a": 1, "b": 2, "c": 3}
    
    print(f"dict1: {dict1}")
    print(f"dict2: {dict2}")
    print(f"dict3: {dict3}")
    print()
    
    # OPERADORES DE COMPARACIÓN
    print("--- COMPARACIÓN ---")
    
    print(f"dict1 == dict3: {dict1 == dict3}")
    print(f"dict1 == dict2: {dict1 == dict2}")
    print(f"dict1 != dict2: {dict1 != dict2}")
    
    # Los operadores <, <=, >, >= no están definidos para dicts
    try:
        resultado = dict1 < dict2
    except TypeError as e:
        print(f"Error con <: {e}")
    print()
    
    # OPERADORES DE PERTENENCIA
    print("--- PERTENENCIA (solo claves) ---")
    
    print(f"'a' in dict1: {'a' in dict1}")
    print(f"'x' in dict1: {'x' in dict1}")
    print(f"'a' not in dict1: {'a' not in dict1}")
    
    # in solo busca en las claves, no en los valores
    print(f"1 in dict1: {1 in dict1}")  # False, 1 es valor, no clave
    print(f"1 in dict1.values(): {1 in dict1.values()}")  # True, buscar en valores
    print()
    
    # OPERADOR | (Python 3.9+)
    print("--- UNIÓN | (Python 3.9+) ---")
    try:
        # Unión de diccionarios (dict2 sobrescribe dict1 si hay claves duplicadas)
        union = dict1 | dict2
        print(f"dict1 | dict2: {union}")
        
        # Actualización in-place
        dict1_copia = dict1.copy()
        dict1_copia |= dict2
        print(f"dict1 |= dict2: {dict1_copia}")
        
    except TypeError:
        print("Operador | no disponible (requiere Python 3.9+)")
        # Alternativa compatible
        union_alt = {**dict1, **dict2}
        print(f"Alternativa {{**dict1, **dict2}}: {union_alt}")
    print()
    
    # LONGITUD
    print("--- LONGITUD ---")
    print(f"len(dict1): {len(dict1)}")
    print(f"len(dict2): {len(dict2)}")
    print()


def comprension_diccionarios():
    """Comprensiones de diccionarios"""
    print("=" * 60)
    print("COMPRENSIONES DE DICCIONARIOS")
    print("=" * 60)
    
    # COMPRENSIONES BÁSICAS
    print("--- COMPRENSIONES BÁSICAS ---")
    
    # Cuadrados de números
    cuadrados = {x: x**2 for x in range(1, 6)}
    print(f"Cuadrados: {cuadrados}")
    
    # Desde listas
    nombres = ["Ana", "Bob", "Carl", "Diana"]
    longitudes = {nombre: len(nombre) for nombre in nombres}
    print(f"Longitudes de nombres: {longitudes}")
    
    # Desde otro diccionario
    precios_euros = {"manzana": 2.5, "banana": 1.8, "naranja": 3.0}
    precios_dolares = {fruta: precio * 1.1 for fruta, precio in precios_euros.items()}
    print(f"Precios en dólares: {precios_dolares}")
    print()
    
    # COMPRENSIONES CON CONDICIONES
    print("--- COMPRENSIONES CON CONDICIONES ---")
    
    # Solo números pares
    pares_cuadrados = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print(f"Cuadrados de pares: {pares_cuadrados}")
    
    # Filtrar diccionario existente
    estudiantes = {
        "Ana": 85,
        "Bob": 92,
        "Carl": 78,
        "Diana": 96,
        "Eva": 88
    }
    
    aprobados = {nombre: nota for nombre, nota in estudiantes.items() if nota >= 80}
    print(f"Estudiantes aprobados: {aprobados}")
    
    # Transformación condicional
    estado_estudiantes = {
        nombre: "Excelente" if nota >= 90 else "Bueno" if nota >= 80 else "Regular"
        for nombre, nota in estudiantes.items()
    }
    print(f"Estado estudiantes: {estado_estudiantes}")
    print()
    
    # COMPRENSIONES ANIDADAS
    print("--- COMPRENSIONES ANIDADAS ---")
    
    # Tabla de multiplicar
    tabla_multiplicar = {
        i: {j: i*j for j in range(1, 4)} 
        for i in range(1, 4)
    }
    print("Tabla de multiplicar:")
    for i, fila in tabla_multiplicar.items():
        print(f"  {i}: {fila}")
    
    # Invertir diccionario (si valores son únicos)
    original = {"a": 1, "b": 2, "c": 3}
    invertido = {v: k for k, v in original.items()}
    print(f"Original: {original}")
    print(f"Invertido: {invertido}")
    print()


def casos_uso_avanzados():
    """Casos de uso avanzados con diccionarios"""
    print("=" * 60)
    print("CASOS DE USO AVANZADOS")
    print("=" * 60)
    
    # CONTAR ELEMENTOS
    print("--- CONTADOR DE ELEMENTOS ---")
    
    texto = "python programming"
    contador_caracteres = {}
    
    # Método manual
    for char in texto:
        if char != ' ':  # Ignorar espacios
            contador_caracteres[char] = contador_caracteres.get(char, 0) + 1
    
    print(f"Texto: '{texto}'")
    print(f"Contador manual: {contador_caracteres}")
    
    # Usando defaultdict
    from collections import defaultdict
    contador_default = defaultdict(int)
    for char in texto:
        if char != ' ':
            contador_default[char] += 1
    
    print(f"Contador defaultdict: {dict(contador_default)}")
    
    # Usando Counter
    from collections import Counter
    contador_counter = Counter(char for char in texto if char != ' ')
    print(f"Contador Counter: {dict(contador_counter)}")
    print()
    
    # AGRUPACIÓN DE DATOS
    print("--- AGRUPACIÓN DE DATOS ---")
    
    estudiantes = [
        {"nombre": "Ana", "curso": "Python", "nota": 85},
        {"nombre": "Bob", "curso": "Java", "nota": 92},
        {"nombre": "Carl", "curso": "Python", "nota": 78},
        {"nombre": "Diana", "curso": "Java", "nota": 96},
        {"nombre": "Eva", "curso": "Python", "nota": 88}
    ]
    
    # Agrupar por curso
    por_curso = {}
    for estudiante in estudiantes:
        curso = estudiante["curso"]
        if curso not in por_curso:
            por_curso[curso] = []
        por_curso[curso].append(estudiante)
    
    print("Estudiantes por curso:")
    for curso, lista in por_curso.items():
        print(f"  {curso}:")
        for est in lista:
            print(f"    {est['nombre']}: {est['nota']}")
    print()
    
    # CACHÉ/MEMOIZACIÓN
    print("--- CACHÉ/MEMOIZACIÓN ---")
    
    # Función fibonacci con caché
    cache_fibonacci = {}
    
    def fibonacci(n):
        if n in cache_fibonacci:
            return cache_fibonacci[n]
        
        if n <= 1:
            resultado = n
        else:
            resultado = fibonacci(n-1) + fibonacci(n-2)
        
        cache_fibonacci[n] = resultado
        return resultado
    
    # Calcular algunos valores
    valores_fib = [fibonacci(i) for i in range(10)]
    print(f"Fibonacci(0-9): {valores_fib}")
    print(f"Caché actual: {cache_fibonacci}")
    print()
    
    # CONFIGURACIÓN JERÁRQUICA
    print("--- CONFIGURACIÓN JERÁRQUICA ---")
    
    config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "credentials": {
                "username": "admin",
                "password": "secret"
            }
        },
        "server": {
            "host": "0.0.0.0",
            "port": 8080,
            "debug": True
        }
    }
    
    def get_config_value(config_dict, path):
        """Obtener valor usando path con notación punto"""
        keys = path.split('.')
        current = config_dict
        
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        
        return current
    
    # Ejemplos de acceso
    paths = [
        "database.host",
        "database.port",
        "database.credentials.username",
        "server.debug",
        "nonexistent.path"
    ]
    
    print("Acceso a configuración:")
    for path in paths:
        valor = get_config_value(config, path)
        print(f"  {path}: {valor}")
    print()


def rendimiento_diccionarios():
    """Aspectos de rendimiento de diccionarios"""
    print("=" * 60)
    print("RENDIMIENTO DE DICCIONARIOS")
    print("=" * 60)
    
    import time
    
    # Comparar acceso en dict vs list
    print("--- COMPARACIÓN dict vs list ---")
    
    # Crear estructuras grandes
    n = 100000
    lista_numeros = list(range(n))
    dict_numeros = {i: i for i in range(n)}
    
    # Buscar elemento en lista (O(n))
    start = time.time()
    resultado_lista = 99999 in lista_numeros
    tiempo_lista = time.time() - start
    
    # Buscar elemento en dict (O(1) promedio)
    start = time.time()
    resultado_dict = 99999 in dict_numeros
    tiempo_dict = time.time() - start
    
    print(f"Búsqueda en lista de {n} elementos: {tiempo_lista:.6f}s")
    print(f"Búsqueda en dict de {n} elementos: {tiempo_dict:.6f}s")
    print(f"Dict es ~{tiempo_lista/tiempo_dict:.1f}x más rápido")
    print()
    
    # Mejores prácticas
    print("--- MEJORES PRÁCTICAS ---")
    print("1. Usar get() en lugar de [] para acceso seguro")
    print("2. Usar setdefault() para inicializar valores")
    print("3. Usar defaultdict para contadores/agrupaciones")
    print("4. Los diccionarios son ideales para búsquedas O(1)")
    print("5. Las claves deben ser hashables (inmutables)")
    print()
    
    # Tipos de claves válidas e inválidas
    print("--- TIPOS DE CLAVES ---")
    
    claves_validas = [
        ("int", 42),
        ("str", "clave"),
        ("tuple", (1, 2, 3)),
        ("frozenset", frozenset([1, 2, 3])),
        ("bool", True),
        ("None", None)
    ]
    
    claves_invalidas = [
        ("list", [1, 2, 3]),
        ("set", {1, 2, 3}),
        ("dict", {"a": 1})
    ]
    
    print("Claves válidas (hashables):")
    for nombre, clave in claves_validas:
        try:
            test_dict = {clave: "valor"}
            print(f"  ✓ {nombre}: {clave}")
        except TypeError:
            print(f"  ✗ {nombre}: {clave}")
    
    print("\nClaves inválidas (no hashables):")
    for nombre, clave in claves_invalidas:
        try:
            test_dict = {clave: "valor"}
            print(f"  ✓ {nombre}: {clave}")
        except TypeError as e:
            print(f"  ✗ {nombre}: {clave} - {e}")
    print()


if __name__ == "__main__":
    creacion_diccionarios()
    acceso_y_modificacion()
    metodos_diccionarios()
    operadores_diccionarios()
    comprension_diccionarios()
    casos_uso_avanzados()
    rendimiento_diccionarios()