#!/usr/bin/env python3
"""
Ejemplos completos de strings (cadenas de texto) en Python
- Creación y representación
- Operadores de string (+, *, in, not in)
- Métodos de strings
- Formateo de strings (%, .format(), f-strings)
- Caracteres de escape y strings raw
"""

def creacion_strings():
    """Ejemplos de creación de strings"""
    print("=" * 60)
    print("CREACIÓN Y REPRESENTACIÓN DE STRINGS")
    print("=" * 60)
    
    # Diferentes formas de crear strings
    string_simple = "Hola mundo"
    string_comillas_dobles = "Texto con 'comillas simples' dentro"
    string_comillas_simples = 'Texto con "comillas dobles" dentro'
    string_multilinea = """Este es un string
    que ocupa múltiples
    líneas de texto"""
    
    string_multilinea_simple = '''También se puede
    usar comillas simples
    para strings multilínea'''
    
    # String vacío
    string_vacio = ""
    string_vacio_alt = str()
    
    print("--- TIPOS DE CREACIÓN ---")
    print(f"Simple: {repr(string_simple)}")
    print(f"Con comillas simples dentro: {repr(string_comillas_dobles)}")
    print(f"Con comillas dobles dentro: {repr(string_comillas_simples)}")
    print(f"Multilínea: {repr(string_multilinea)}")
    print(f"Vacío: {repr(string_vacio)}")
    print(f"Tipo: {type(string_simple)}")
    print()
    
    # Caracteres de escape
    print("--- CARACTERES DE ESCAPE ---")
    print(f"Nueva línea: {'Línea 1\\nLínea 2'}")
    print(f"Tabulación: {'Col1\\tCol2\\tCol3'}")
    print(f"Barra invertida: {'Ruta: C:\\\\Users\\\\nombre'}")
    print(f"Comilla: {'Dijo: \"Hola\"'}")
    print("Comilla simple: Isn't it?")
    print(f"Carriage return: {'Texto\\rNuevo'}")
    print(f"Unicode: {'Corazón: \\u2764'}")
    print(f"Unicode emoji: {'\\U0001F600'}")  # 😀
    print()
    
    # Raw strings
    print("--- RAW STRINGS ---")
    ruta_normal = "C:\\Users\\nombre\\documents"
    ruta_raw = r"C:\Users\nombre\documents"
    regex_pattern = r"\d+\.\d+"  # Útil para expresiones regulares
    
    print(f"Normal: {repr(ruta_normal)}")
    print(f"Raw: {repr(ruta_raw)}")
    print(f"Regex pattern: {repr(regex_pattern)}")
    print()


def operadores_strings():
    """Operadores que se pueden usar con strings"""
    print("=" * 60)
    print("OPERADORES CON STRINGS")
    print("=" * 60)
    
    # Concatenación con +
    print("--- CONCATENACIÓN (+) ---")
    nombre = "Juan"
    apellido = "Pérez"
    nombre_completo = nombre + " " + apellido
    print(f"'{nombre}' + ' ' + '{apellido}' = '{nombre_completo}'")
    
    # Concatenación múltiple
    saludo = "Hola" + ", " + "¿cómo" + " " + "estás?"
    print(f"Concatenación múltiple: '{saludo}'")
    print()
    
    # Repetición con *
    print("--- REPETICIÓN (*) ---")
    caracter = "="
    separador = caracter * 50
    print(f"'{caracter}' * 50 = '{separador}'")
    
    patron = "abc" * 3
    print(f"'abc' * 3 = '{patron}'")
    
    # Crear espacios para alineación
    espacios = " " * 10
    texto_centrado = espacios + "CENTRADO" + espacios
    print(f"Texto con espacios: '{texto_centrado}'")
    print()
    
    # Operadores de pertenencia (in, not in)
    print("--- OPERADORES DE PERTENENCIA ---")
    texto = "Python es un lenguaje de programación"
    
    print(f"Texto: '{texto}'")
    print(f"'Python' in texto: {'Python' in texto}")
    print(f"'Java' in texto: {'Java' in texto}")
    print(f"'java' in texto: {'java' in texto}")  # Case sensitive
    print(f"'PYTHON' not in texto: {'PYTHON' not in texto}")
    
    # Buscar subcadenas
    subcadenas = ["Python", "lenguaje", "xyz", "programación"]
    for sub in subcadenas:
        if sub in texto:
            print(f"  ✓ Encontrado: '{sub}'")
        else:
            print(f"  ✗ No encontrado: '{sub}'")
    print()
    
    # Operadores de comparación
    print("--- OPERADORES DE COMPARACIÓN ---")
    str1 = "abc"
    str2 = "abd"
    str3 = "abc"
    str4 = "ABC"
    
    print(f"'{str1}' == '{str3}': {str1 == str3}")
    print(f"'{str1}' == '{str4}': {str1 == str4}")
    print(f"'{str1}' < '{str2}': {str1 < str2}")  # Comparación lexicográfica
    print(f"'{str1}' > '{str4}': {str1 > str4}")  # Minúsculas > Mayúsculas
    
    # Comparación de longitudes
    print(f"len('{str1}') = {len(str1)}")
    print(f"len('{texto}') = {len(texto)}")
    print()


def indexacion_y_slicing():
    """Indexación y slicing de strings"""
    print("=" * 60)
    print("INDEXACIÓN Y SLICING")
    print("=" * 60)
    
    texto = "Python Programming"
    print(f"Texto: '{texto}'")
    print(f"Longitud: {len(texto)}")
    print()
    
    # Indexación
    print("--- INDEXACIÓN ---")
    print(f"Primer carácter: texto[0] = '{texto[0]}'")
    print(f"Último carácter: texto[-1] = '{texto[-1]}'")
    print(f"Quinto carácter: texto[4] = '{texto[4]}'")
    print(f"Segundo desde el final: texto[-2] = '{texto[-2]}'")
    print()
    
    # Slicing
    print("--- SLICING ---")
    print(f"Primeros 6: texto[0:6] = '{texto[0:6]}'")
    print(f"Desde índice 7: texto[7:] = '{texto[7:]}'")
    print(f"Hasta índice 6: texto[:6] = '{texto[:6]}'")
    print(f"Últimos 11: texto[-11:] = '{texto[-11:]}'")
    print(f"Desde -11 hasta -1: texto[-11:-1] = '{texto[-11:-1]}'")
    
    # Slicing con paso
    print(f"Cada 2 caracteres: texto[::2] = '{texto[::2]}'")
    print(f"Reverso: texto[::-1] = '{texto[::-1]}'")
    print(f"Reverso de parte: texto[6:0:-1] = '{texto[6:0:-1]}'")
    print()
    
    # Intentar modificar (error)
    print("--- INMUTABILIDAD ---")
    print("Los strings son inmutables:")
    try:
        texto[0] = 'j'  # Esto causará error
    except TypeError as e:
        print(f"Error al intentar modificar: {e}")
    print("Para modificar, se debe crear un nuevo string")
    texto_modificado = 'j' + texto[1:]
    print(f"Nuevo string: '{texto_modificado}'")
    print()


def metodos_strings_basicos():
    """Métodos básicos de strings"""
    print("=" * 60)
    print("MÉTODOS BÁSICOS DE STRINGS")
    print("=" * 60)
    
    texto = "  Hello World Python Programming  "
    print(f"Texto original: '{texto}'")
    print()
    
    # Métodos de limpieza
    print("--- MÉTODOS DE LIMPIEZA ---")
    print(f"strip(): '{texto.strip()}'")
    print(f"lstrip(): '{texto.lstrip()}'")
    print(f"rstrip(): '{texto.rstrip()}'")
    print(f"strip('P '): '{texto.strip('P ')}'")  # Caracteres específicos
    print()
    
    # Métodos de caso
    print("--- MÉTODOS DE CASO ---")
    sample_text = "Hello World"
    print(f"Texto: '{sample_text}'")
    print(f"lower(): '{sample_text.lower()}'")
    print(f"upper(): '{sample_text.upper()}'")
    print(f"title(): '{sample_text.title()}'")
    print(f"capitalize(): '{sample_text.capitalize()}'")
    print(f"swapcase(): '{sample_text.swapcase()}'")
    print()
    
    # Métodos de verificación
    print("--- MÉTODOS DE VERIFICACIÓN ---")
    test_strings = ["Hello", "hello", "HELLO", "Hello World", "123", "abc123", "   "]
    
    for s in test_strings:
        print(f"'{s}':")
        print(f"  islower(): {s.islower()}")
        print(f"  isupper(): {s.isupper()}")
        print(f"  istitle(): {s.istitle()}")
        print(f"  isalpha(): {s.isalpha()}")
        print(f"  isdigit(): {s.isdigit()}")
        print(f"  isalnum(): {s.isalnum()}")
        print(f"  isspace(): {s.isspace()}")
        print()


def metodos_busqueda_reemplazo():
    """Métodos de búsqueda y reemplazo"""
    print("=" * 60)
    print("MÉTODOS DE BÚSQUEDA Y REEMPLAZO")
    print("=" * 60)
    
    texto = "Python es genial. Python es poderoso. Python es fácil."
    print(f"Texto: '{texto}'")
    print()
    
    # Métodos de búsqueda
    print("--- MÉTODOS DE BÚSQUEDA ---")
    print(f"find('Python'): {texto.find('Python')}")
    print(f"find('Java'): {texto.find('Java')}")  # -1 si no encuentra
    print(f"rfind('Python'): {texto.rfind('Python')}")  # Último
    print(f"index('es'): {texto.index('es')}")
    
    try:
        print(f"index('Java'): {texto.index('Java')}")  # Error si no encuentra
    except ValueError as e:
        print(f"Error con index('Java'): {e}")
    
    print(f"count('Python'): {texto.count('Python')}")
    print(f"count('es'): {texto.count('es')}")
    print()
    
    # Métodos de verificación de inicio/fin
    print("--- INICIO Y FIN ---")
    print(f"startswith('Python'): {texto.startswith('Python')}")
    print(f"startswith('Java'): {texto.startswith('Java')}")
    print(f"endswith('fácil.'): {texto.endswith('fácil.')}")
    print(f"endswith('difícil.'): {texto.endswith('difícil.')}")
    
    # Con tupla de opciones
    print(f"startswith(('Python', 'Java')): {texto.startswith(('Python', 'Java'))}")
    print()
    
    # Métodos de reemplazo
    print("--- MÉTODOS DE REEMPLAZO ---")
    print(f"replace('Python', 'Java'): '{texto.replace('Python', 'Java')}'")
    print(f"replace('es', 'ES'): '{texto.replace('es', 'ES')}'")
    print(f"replace('Python', 'Java', 1): '{texto.replace('Python', 'Java', 1)}'")  # Solo 1 vez
    print()


def metodos_division_union():
    """Métodos de división y unión de strings"""
    print("=" * 60)
    print("MÉTODOS DE DIVISIÓN Y UNIÓN")
    print("=" * 60)
    
    # Split
    print("--- DIVISIÓN (SPLIT) ---")
    frase = "manzana,banana,naranja,uva"
    palabras = "Hola mundo Python programación"
    
    print(f"Frase: '{frase}'")
    print(f"split(','): {frase.split(',')}")
    print(f"split(): {palabras.split()}")  # Por defecto divide por espacios
    print(f"split(' ', 2): {palabras.split(' ', 2)}")  # Máximo 2 divisiones
    
    # rsplit (desde la derecha)
    path = "/home/user/documents/file.txt"
    print(f"Path: '{path}'")
    print(f"rsplit('/', 1): {path.rsplit('/', 1)}")  # Solo última división
    print()
    
    # splitlines
    texto_lineas = "Línea 1\nLínea 2\nLínea 3\r\nLínea 4"
    print(f"Texto con líneas: '{repr(texto_lineas)}'")
    print(f"splitlines(): {texto_lineas.splitlines()}")
    print(f"splitlines(True): {texto_lineas.splitlines(True)}")  # Mantener \n
    print()
    
    # Join
    print("--- UNIÓN (JOIN) ---")
    frutas = ["manzana", "banana", "naranja", "uva"]
    numeros = [1, 2, 3, 4, 5]
    
    print(f"Lista de frutas: {frutas}")
    print(f"', '.join(frutas): '{', '.join(frutas)}'")
    print(f"' - '.join(frutas): '{' - '.join(frutas)}'")
    print(f"''.join(frutas): '{''.join(frutas)}'")  # Sin separador
    
    # Convertir números a string para join
    numeros_str = [str(n) for n in numeros]
    print(f"'-'.join(números): '{'-'.join(numeros_str)}'")
    
    # Join con caracteres especiales
    print(f"'\\n'.join(frutas):")
    print('\n'.join(frutas))
    print()


def formateo_strings():
    """Diferentes métodos de formateo de strings"""
    print("=" * 60)
    print("FORMATEO DE STRINGS")
    print("=" * 60)
    
    nombre = "Ana"
    edad = 25
    altura = 1.68
    pi = 3.141592653589793
    
    # Formateo con % (estilo C)
    print("--- FORMATEO CON % ---")
    print(f"Nombre: %s, Edad: %d años" % (nombre, edad))
    print(f"Altura: %.2f metros" % altura)
    print(f"Pi: %.3f" % pi)
    print(f"Pi con padding: %10.3f" % pi)
    print(f"Hexadecimal: %x" % 255)
    print(f"Octal: %o" % 64)
    print()
    
    # Formateo con .format()
    print("--- FORMATEO CON .format() ---")
    print("Nombre: {}, Edad: {} años".format(nombre, edad))
    print("Nombre: {0}, Edad: {1} años".format(nombre, edad))
    print("Edad: {1}, Nombre: {0}".format(nombre, edad))  # Orden diferente
    print("Nombre: {n}, Edad: {e} años".format(n=nombre, e=edad))
    
    # Formateo numérico con .format()
    print("Pi: {:.3f}".format(pi))
    print("Pi con padding: {:10.3f}".format(pi))
    print("Entero con ceros: {:05d}".format(42))
    print("Porcentaje: {:.2%}".format(0.1234))
    print("Notación científica: {:.2e}".format(12345.67))
    print()
    
    # F-strings (Python 3.6+)
    print("--- F-STRINGS (RECOMENDADO) ---")
    print(f"Nombre: {nombre}, Edad: {edad} años")
    print(f"Altura: {altura:.2f} metros")
    print(f"Pi: {pi:.3f}")
    print(f"Pi con padding: {pi:10.3f}")
    
    # Expresiones dentro de f-strings
    print(f"Área del círculo (r=2): {pi * 2**2:.2f}")
    print(f"Nombre en mayúsculas: {nombre.upper()}")
    print(f"¿Es mayor de edad?: {edad >= 18}")
    print(f"Edad el próximo año: {edad + 1}")
    
    # Formateo avanzado en f-strings
    precio = 1234.56
    print(f"Precio: ${precio:,.2f}")  # Con comas para miles
    print(f"Precio: ${precio:>10.2f}")  # Alineado a la derecha
    print(f"Precio: ${precio:<10.2f}")  # Alineado a la izquierda
    print(f"Precio: ${precio:^10.2f}")  # Centrado
    
    fecha = "2023-12-25"
    print(f"Fecha: {fecha:=^20}")  # Centrado con relleno =
    print()


def metodos_alineacion_relleno():
    """Métodos de alineación y relleno"""
    print("=" * 60)
    print("ALINEACIÓN Y RELLENO")
    print("=" * 60)
    
    texto = "Python"
    ancho = 20
    
    print(f"Texto original: '{texto}' (longitud: {len(texto)})")
    print(f"Ancho objetivo: {ancho}")
    print()
    
    # Métodos de alineación
    print("--- MÉTODOS DE ALINEACIÓN ---")
    print(f"ljust({ancho}): '{texto.ljust(ancho)}'")
    print(f"rjust({ancho}): '{texto.rjust(ancho)}'")
    print(f"center({ancho}): '{texto.center(ancho)}'")
    
    # Con caracteres de relleno
    print(f"ljust({ancho}, '-'): '{texto.ljust(ancho, '-')}'")
    print(f"rjust({ancho}, '*'): '{texto.rjust(ancho, '*')}'")
    print(f"center({ancho}, '='): '{texto.center(ancho, '=')}'")
    
    # zfill para números
    numero = "42"
    print(f"zfill(5): '{numero.zfill(5)}'")
    print(f"zfill(8): '{numero.zfill(8)}'")
    print()
    
    # Formateo de tablas
    print("--- FORMATEO DE TABLAS ---")
    datos = [
        ("Producto", "Precio", "Stock"),
        ("Laptop", 999.99, 15),
        ("Mouse", 29.99, 50),
        ("Teclado", 79.99, 25)
    ]
    
    for fila in datos:
        if isinstance(fila[1], str):  # Header
            print(f"{fila[0]:<10} {fila[1]:<8} {fila[2]:<5}")
        else:  # Data
            print(f"{fila[0]:<10} ${fila[1]:<7.2f} {fila[2]:<5}")
    print()


def encoding_unicode():
    """Ejemplos de encoding y Unicode"""
    print("=" * 60)
    print("ENCODING Y UNICODE")
    print("=" * 60)
    
    # Caracteres Unicode
    print("--- CARACTERES UNICODE ---")
    texto_unicode = "Hola 🌍 mundo! ñáéíóú"
    print(f"Texto: {texto_unicode}")
    print(f"Longitud: {len(texto_unicode)}")
    
    # Caracteres especiales
    print("Símbolos matemáticos: α β γ π ∑ ∞")
    print("Emojis: 😀 😂 ❤️ 🔥 ⭐")
    print("Otros idiomas: こんにちは العربية русский")
    print()
    
    # Códigos Unicode
    print("--- CÓDIGOS UNICODE ---")
    print(f"ord('A'): {ord('A')}")
    print(f"ord('ñ'): {ord('ñ')}")
    print(f"chr(65): '{chr(65)}'")
    print(f"chr(241): '{chr(241)}'")
    print(f"chr(128512): '{chr(128512)}'")  # 😀
    
    # Escape Unicode
    print(f"\\u0041: '\\u0041'")  # A
    print(f"\\u00f1: '\\u00f1'")  # ñ
    print(f"\\U0001f600: '\\U0001f600'")  # 😀
    print()
    
    # Encoding/Decoding
    print("--- ENCODING Y DECODING ---")
    texto = "Hola ñoño"
    
    # Encode to bytes
    bytes_utf8 = texto.encode('utf-8')
    bytes_latin1 = texto.encode('latin-1')
    
    print(f"Texto original: '{texto}'")
    print(f"UTF-8 bytes: {bytes_utf8}")
    print(f"Latin-1 bytes: {bytes_latin1}")
    
    # Decode back to string
    decoded_utf8 = bytes_utf8.decode('utf-8')
    decoded_latin1 = bytes_latin1.decode('latin-1')
    
    print(f"Decoded UTF-8: '{decoded_utf8}'")
    print(f"Decoded Latin-1: '{decoded_latin1}'")
    print()


if __name__ == "__main__":
    creacion_strings()
    operadores_strings()
    indexacion_y_slicing()
    metodos_strings_basicos()
    metodos_busqueda_reemplazo()
    metodos_division_union()
    formateo_strings()
    metodos_alineacion_relleno()
    encoding_unicode()