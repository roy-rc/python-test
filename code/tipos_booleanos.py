#!/usr/bin/env python3
"""
Ejemplos completos de tipo booleano (bool) en Python
- Valores True y False
- Operadores lógicos (and, or, not)
- Conversiones a booleano
- Evaluación de truthiness
- Operadores de comparación
"""

def valores_booleanos():
    """Ejemplos básicos de valores booleanos"""
    print("=" * 60)
    print("VALORES BOOLEANOS BÁSICOS")
    print("=" * 60)
    
    # Valores booleanos literales
    verdadero = True
    falso = False
    
    print(f"True: {verdadero} (tipo: {type(verdadero)})")
    print(f"False: {falso} (tipo: {type(falso)})")
    print()
    
    # Los booleanos son subclase de int
    print("--- BOOLEANOS COMO ENTEROS ---")
    print(f"True como entero: {int(True)}")
    print(f"False como entero: {int(False)}")
    print(f"True + True = {True + True}")
    print(f"True * 5 = {True * 5}")
    print(f"False * 100 = {False * 100}")
    print(f"isinstance(True, int): {isinstance(True, int)}")
    print(f"isinstance(True, bool): {isinstance(True, bool)}")
    print()
    
    # Crear booleanos
    print("--- CREAR BOOLEANOS ---")
    print(f"bool(1): {bool(1)}")
    print(f"bool(0): {bool(0)}")
    print(f"bool('texto'): {bool('texto')}")
    print(f"bool(''): {bool('')}")
    print(f"bool([]): {bool([])}")
    print(f"bool([1, 2, 3]): {bool([1, 2, 3])}")
    print()


def operadores_logicos():
    """Operadores lógicos: and, or, not"""
    print("=" * 60)
    print("OPERADORES LÓGICOS")
    print("=" * 60)
    
    # Tabla de verdad para AND
    print("--- OPERADOR AND ---")
    valores = [True, False]
    print("Tabla de verdad para AND:")
    for a in valores:
        for b in valores:
            resultado = a and b
            print(f"{a!s:5} and {b!s:5} = {resultado!s:5}")
    print()
    
    # Tabla de verdad para OR
    print("--- OPERADOR OR ---")
    print("Tabla de verdad para OR:")
    for a in valores:
        for b in valores:
            resultado = a or b
            print(f"{a!s:5} or  {b!s:5} = {resultado!s:5}")
    print()
    
    # Operador NOT
    print("--- OPERADOR NOT ---")
    print("Tabla de verdad para NOT:")
    for a in valores:
        resultado = not a
        print(f"not {a!s:5} = {resultado!s:5}")
    print()
    
    # Ejemplos prácticos
    print("--- EJEMPLOS PRÁCTICOS ---")
    edad = 25
    tiene_licencia = True
    experiencia_anos = 3
    
    # Condiciones compuestas
    puede_conducir = edad >= 18 and tiene_licencia
    conductor_experimentado = puede_conducir and experiencia_anos >= 2
    conductor_novato = puede_conducir and not conductor_experimentado
    
    print(f"Edad: {edad}")
    print(f"Tiene licencia: {tiene_licencia}")
    print(f"Años de experiencia: {experiencia_anos}")
    print(f"Puede conducir: {puede_conducir}")
    print(f"Conductor experimentado: {conductor_experimentado}")
    print(f"Conductor novato: {conductor_novato}")
    print()


def cortocircuito_evaluacion():
    """Evaluación de cortocircuito en operadores lógicos"""
    print("=" * 60)
    print("EVALUACIÓN DE CORTOCIRCUITO")
    print("=" * 60)
    
    print("--- CORTOCIRCUITO CON AND ---")
    
    # Función que indica cuando se ejecuta
    def funcion_que_imprime(valor, nombre):
        print(f"  Ejecutando {nombre}(): {valor}")
        return valor
    
    print("Ejemplo: False and función()")
    resultado = funcion_que_imprime(False, "primera") and funcion_que_imprime(True, "segunda")
    print(f"Resultado: {resultado}")
    print("La segunda función no se ejecutó (cortocircuito)\n")
    
    print("Ejemplo: True and función()")
    resultado = funcion_que_imprime(True, "primera") and funcion_que_imprime(False, "segunda")
    print(f"Resultado: {resultado}")
    print("Ambas funciones se ejecutaron\n")
    
    print("--- CORTOCIRCUITO CON OR ---")
    
    print("Ejemplo: True or función()")
    resultado = funcion_que_imprime(True, "primera") or funcion_que_imprime(False, "segunda")
    print(f"Resultado: {resultado}")
    print("La segunda función no se ejecutó (cortocircuito)\n")
    
    print("Ejemplo: False or función()")
    resultado = funcion_que_imprime(False, "primera") or funcion_que_imprime(True, "segunda")
    print(f"Resultado: {resultado}")
    print("Ambas funciones se ejecutaron\n")
    
    # Aplicación práctica del cortocircuito
    print("--- APLICACIÓN PRÁCTICA ---")
    
    lista = []
    # Usar cortocircuito para evitar error de índice
    tiene_elementos = len(lista) > 0 and lista[0] is not None
    print(f"Lista vacía - tiene elementos válidos: {tiene_elementos}")
    
    lista = [42, None, 100]
    tiene_elementos = len(lista) > 0 and lista[0] is not None
    print(f"Lista con elementos - tiene elementos válidos: {tiene_elementos}")
    
    lista = [None, 42, 100]
    tiene_elementos = len(lista) > 0 and lista[0] is not None
    print(f"Lista con None al inicio - tiene elementos válidos: {tiene_elementos}")
    print()


def truthiness_valores():
    """Valores que se evalúan como True o False"""
    print("=" * 60)
    print("TRUTHINESS - VALORES TRUTHY Y FALSY")
    print("=" * 60)
    
    # Valores que se evalúan como False (falsy)
    print("--- VALORES FALSY ---")
    valores_falsy = [
        False, 0, 0.0, 0j, "", [], (), {}, set(), None, range(0)
    ]
    
    for valor in valores_falsy:
        print(f"bool({valor!r:15}) = {bool(valor)}")
    print()
    
    # Valores que se evalúan como True (truthy)
    print("--- VALORES TRUTHY ---")
    valores_truthy = [
        True, 1, -1, 3.14, 1+2j, "texto", " ", [1], (1,), {1: 2}, {1}, range(1)
    ]
    
    for valor in valores_truthy:
        print(f"bool({valor!r:15}) = {bool(valor)}")
    print()
    
    # Casos especiales
    print("--- CASOS ESPECIALES ---")
    print(f"bool('0'): {bool('0')}")  # String no vacío es truthy
    print(f"bool('False'): {bool('False')}")  # String no vacío es truthy
    print(f"bool(' '): {bool(' ')}")  # Espacio es truthy
    print(f"bool([0]): {bool([0])}")  # Lista no vacía es truthy
    print(f"bool([False]): {bool([False])}")  # Lista no vacía es truthy
    print()


def operadores_comparacion():
    """Operadores de comparación que retornan booleanos"""
    print("=" * 60)
    print("OPERADORES DE COMPARACIÓN")
    print("=" * 60)
    
    # Comparaciones numéricas
    print("--- COMPARACIONES NUMÉRICAS ---")
    a = 10
    b = 20
    c = 10
    
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"a == c: {a == c}")
    print(f"a != b: {a != b}")
    print(f"a < b: {a < b}")
    print(f"a <= c: {a <= c}")
    print(f"b > a: {b > a}")
    print(f"a >= c: {a >= c}")
    print()
    
    # Comparaciones de strings
    print("--- COMPARACIONES DE STRINGS ---")
    str1 = "abc"
    str2 = "abd"
    str3 = "ABC"
    
    print(f"'{str1}' == '{str1}': {str1 == str1}")
    print(f"'{str1}' < '{str2}': {str1 < str2}")
    print(f"'{str1}' > '{str3}': {str1 > str3}")
    print(f"'{str1}'.lower() == '{str3}'.lower(): {str1.lower() == str3.lower()}")
    print()
    
    # Comparaciones encadenadas
    print("--- COMPARACIONES ENCADENADAS ---")
    x = 15
    print(f"x = {x}")
    print(f"10 < x < 20: {10 < x < 20}")
    print(f"10 < x > 20: {10 < x > 20}")  # x > 10 AND x > 20
    print(f"x == 15 == 15: {x == 15 == 15}")
    print(f"0 <= x <= 100: {0 <= x <= 100}")
    print()
    
    # Operadores is e in
    print("--- OPERADORES is E in ---")
    lista1 = [1, 2, 3]
    lista2 = [1, 2, 3]
    lista3 = lista1
    
    print(f"lista1 = {lista1}")
    print(f"lista2 = {lista2}")
    print(f"lista3 = lista1")
    print(f"lista1 == lista2: {lista1 == lista2}")  # Mismo contenido
    print(f"lista1 is lista2: {lista1 is lista2}")  # Misma identidad
    print(f"lista1 is lista3: {lista1 is lista3}")  # Misma identidad
    print(f"2 in lista1: {2 in lista1}")
    print(f"4 not in lista1: {4 not in lista1}")
    
    # Casos especiales con is
    print(f"None is None: {None is None}")
    print(f"True is True: {True is True}")
    print(f"5 is 5: {5 is 5}")  # Pequeños enteros son singleton
    print(f"1000 is 1000: {1000 is 1000}")  # Puede ser False
    print()


def combinacion_operadores():
    """Combinación compleja de operadores lógicos y de comparación"""
    print("=" * 60)
    print("COMBINACIÓN DE OPERADORES")
    print("=" * 60)
    
    # Sistema de autenticación simple
    print("--- SISTEMA DE AUTENTICACIÓN ---")
    usuarios_validos = ["admin", "user1", "user2"]
    passwords = {"admin": "admin123", "user1": "pass1", "user2": "pass2"}
    sesiones_activas = ["user1"]
    
    def autenticar(usuario, password, requiere_admin=False):
        usuario_existe = usuario in usuarios_validos
        password_correcto = usuario_existe and passwords.get(usuario) == password
        es_admin = usuario == "admin"
        sesion_activa = usuario in sesiones_activas
        
        if requiere_admin:
            return password_correcto and es_admin
        else:
            return password_correcto and (not requiere_admin or es_admin)
    
    # Casos de prueba
    casos = [
        ("admin", "admin123", True),
        ("admin", "wrong", True),
        ("user1", "pass1", False),
        ("user1", "pass1", True),
        ("nouser", "any", False)
    ]
    
    for usuario, password, req_admin in casos:
        resultado = autenticar(usuario, password, req_admin)
        print(f"Usuario: {usuario:8} Password: {password:8} Admin req: {req_admin} → {resultado}")
    print()
    
    # Validación de datos
    print("--- VALIDACIÓN DE DATOS ---")
    
    def validar_edad(edad_str):
        # Verificar si es numérico y está en rango válido
        es_numerico = edad_str.isdigit()
        if es_numerico:
            edad = int(edad_str)
            es_valida = 0 <= edad <= 120
            return es_numerico and es_valida
        return False
    
    def validar_email(email):
        # Validación básica de email
        tiene_arroba = '@' in email
        partes = email.split('@') if tiene_arroba else []
        tiene_dos_partes = len(partes) == 2
        nombre_valido = tiene_dos_partes and len(partes[0]) > 0
        dominio_valido = tiene_dos_partes and '.' in partes[1] and len(partes[1]) > 3
        
        return tiene_arroba and tiene_dos_partes and nombre_valido and dominio_valido
    
    # Probar validaciones
    edades_prueba = ["25", "abc", "150", "-5", "0", "120"]
    emails_prueba = ["test@example.com", "invalid", "@example.com", "test@", "test@ex.co"]
    
    print("Validación de edades:")
    for edad in edades_prueba:
        valida = validar_edad(edad)
        print(f"  '{edad}' → {valida}")
    
    print("\nValidación de emails:")
    for email in emails_prueba:
        valido = validar_email(email)
        print(f"  '{email}' → {valido}")
    print()


def precedencia_operadores():
    """Precedencia de operadores lógicos"""
    print("=" * 60)
    print("PRECEDENCIA DE OPERADORES")
    print("=" * 60)
    
    # Precedencia: not > and > or
    print("--- PRECEDENCIA: not > and > or ---")
    
    print("Expresión: True or False and False")
    resultado1 = True or False and False
    print(f"Resultado: {resultado1}")
    print("Se evalúa como: True or (False and False) = True\n")
    
    print("Expresión: not False or True and False")
    resultado2 = not False or True and False
    print(f"Resultado: {resultado2}")
    print("Se evalúa como: (not False) or (True and False) = True or False = True\n")
    
    print("Expresión: False and True or True")
    resultado3 = False and True or True
    print(f"Resultado: {resultado3}")
    print("Se evalúa como: (False and True) or True = False or True = True\n")
    
    # Uso de paréntesis para cambiar precedencia
    print("--- USO DE PARÉNTESIS ---")
    
    expr1 = True or False and False
    expr2 = (True or False) and False
    
    print(f"True or False and False = {expr1}")
    print(f"(True or False) and False = {expr2}")
    print()
    
    # Comparación vs lógicos
    print("--- PRECEDENCIA: comparación > not > and > or ---")
    
    x = 5
    y = 10
    z = 15
    
    # Sin paréntesis
    resultado = x < y and y < z or z > 20
    print(f"x={x}, y={y}, z={z}")
    print(f"x < y and y < z or z > 20 = {resultado}")
    print("Se evalúa como: (x < y) and (y < z) or (z > 20)\n")
    
    # Con paréntesis para claridad
    resultado_claro = (x < y and y < z) or (z > 20)
    print(f"(x < y and y < z) or (z > 20) = {resultado_claro}")
    print()


if __name__ == "__main__":
    valores_booleanos()
    operadores_logicos()
    cortocircuito_evaluacion()
    truthiness_valores()
    operadores_comparacion()
    combinacion_operadores()
    precedencia_operadores()