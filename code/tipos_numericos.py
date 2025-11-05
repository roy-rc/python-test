#!/usr/bin/env python3
"""
Ejemplos completos de tipos de datos numéricos en Python
- int (enteros)
- float (punto flotante)
- complex (números complejos)
- Operadores aritméticos, de comparación y bitwise
"""

def ejemplos_enteros():
    """Ejemplos con números enteros (int)"""
    print("=" * 60)
    print("NÚMEROS ENTEROS (int)")
    print("=" * 60)
    
    # Creación de enteros
    entero_decimal = 42
    entero_binario = 0b101010  # 42 en binario
    entero_octal = 0o52        # 42 en octal
    entero_hexadecimal = 0x2A  # 42 en hexadecimal
    entero_negativo = -42
    entero_grande = 12345678901234567890123456789
    
    print("--- CREACIÓN Y REPRESENTACIÓN ---")
    print(f"Decimal: {entero_decimal}")
    print(f"Binario 0b101010: {entero_binario}")
    print(f"Octal 0o52: {entero_octal}")
    print(f"Hexadecimal 0x2A: {entero_hexadecimal}")
    print(f"Negativo: {entero_negativo}")
    print(f"Grande: {entero_grande}")
    print(f"Tipo: {type(entero_decimal)}")
    print()
    
    # Conversiones de base
    print("--- CONVERSIONES DE BASE ---")
    numero = 255
    print(f"Número: {numero}")
    print(f"Binario: {bin(numero)}")
    print(f"Octal: {oct(numero)}")
    print(f"Hexadecimal: {hex(numero)}")
    print()
    
    # OPERADORES ARITMÉTICOS
    print("--- OPERADORES ARITMÉTICOS ---")
    a = 17
    b = 5
    
    print(f"a = {a}, b = {b}")
    print(f"Suma: a + b = {a + b}")
    print(f"Resta: a - b = {a - b}")
    print(f"Multiplicación: a * b = {a * b}")
    print(f"División flotante: a / b = {a / b}")
    print(f"División entera: a // b = {a // b}")
    print(f"Módulo (resto): a % b = {a % b}")
    print(f"Potencia: a ** b = {a ** b}")
    print(f"Valor absoluto: abs(-42) = {abs(-42)}")
    print()
    
    # Funciones matemáticas integradas
    print("--- FUNCIONES MATEMÁTICAS INTEGRADAS ---")
    numeros = [3, -7, 12, 0, -5, 8]
    print(f"Lista: {numeros}")
    print(f"Suma: sum() = {sum(numeros)}")
    print(f"Máximo: max() = {max(numeros)}")
    print(f"Mínimo: min() = {min(numeros)}")
    print(f"Valor absoluto de cada uno: {[abs(x) for x in numeros]}")
    
    # divmod()
    print(f"divmod(17, 5) = {divmod(17, 5)}")  # (cociente, resto)
    print(f"pow(2, 10) = {pow(2, 10)}")
    print(f"pow(2, 10, 1000) = {pow(2, 10, 1000)}")  # (2**10) % 1000
    print()


def operadores_comparacion_enteros():
    """Operadores de comparación con enteros"""
    print("--- OPERADORES DE COMPARACIÓN ---")
    
    x = 10
    y = 20
    z = 10
    
    print(f"x = {x}, y = {y}, z = {z}")
    print(f"x == y: {x == y}")
    print(f"x == z: {x == z}")
    print(f"x != y: {x != y}")
    print(f"x < y: {x < y}")
    print(f"x <= z: {x <= z}")
    print(f"x > y: {x > y}")
    print(f"x >= z: {x >= z}")
    
    # Comparaciones encadenadas
    print(f"0 < x < y: {0 < x < y}")
    print(f"x <= z <= y: {x <= z <= y}")
    print()


def operadores_bitwise():
    """Operadores bitwise con enteros"""
    print("--- OPERADORES BITWISE ---")
    
    a = 60  # 0011 1100 en binario
    b = 13  # 0000 1101 en binario
    
    print(f"a = {a} ({bin(a)})")
    print(f"b = {b} ({bin(b)})")
    print()
    
    print(f"AND bitwise: a & b = {a & b} ({bin(a & b)})")
    print(f"OR bitwise: a | b = {a | b} ({bin(a | b)})")
    print(f"XOR bitwise: a ^ b = {a ^ b} ({bin(a ^ b)})")
    print(f"NOT bitwise: ~a = {~a} ({bin(~a & 0xFF)})")  # Mostrar solo 8 bits
    print(f"Despl. izq.: a << 2 = {a << 2} ({bin(a << 2)})")
    print(f"Despl. der.: a >> 2 = {a >> 2} ({bin(a >> 2)})")
    print()


def ejemplos_flotantes():
    """Ejemplos con números de punto flotante (float)"""
    print("=" * 60)
    print("NÚMEROS DE PUNTO FLOTANTE (float)")
    print("=" * 60)
    
    # Creación de flotantes
    flotante_decimal = 3.14159
    flotante_exponencial = 1.23e-4  # 0.000123
    flotante_exponencial_pos = 6.02e23  # 6.02 * 10^23
    flotante_infinito = float('inf')
    flotante_menos_infinito = float('-inf')
    flotante_nan = float('nan')  # Not a Number
    
    print("--- CREACIÓN Y REPRESENTACIÓN ---")
    print(f"Decimal: {flotante_decimal}")
    print(f"Exponencial 1.23e-4: {flotante_exponencial}")
    print(f"Exponencial 6.02e23: {flotante_exponencial_pos}")
    print(f"Infinito: {flotante_infinito}")
    print(f"Menos infinito: {flotante_menos_infinito}")
    print(f"NaN: {flotante_nan}")
    print(f"Tipo: {type(flotante_decimal)}")
    print()
    
    # OPERACIONES ARITMÉTICAS
    print("--- OPERACIONES ARITMÉTICAS ---")
    x = 10.5
    y = 3.2
    
    print(f"x = {x}, y = {y}")
    print(f"Suma: x + y = {x + y}")
    print(f"Resta: x - y = {x - y}")
    print(f"Multiplicación: x * y = {x * y}")
    print(f"División: x / y = {x / y}")
    print(f"División entera: x // y = {x // y}")
    print(f"Módulo: x % y = {x % y}")
    print(f"Potencia: x ** y = {x ** y}")
    print()
    
    # Funciones matemáticas
    import math
    
    print("--- FUNCIONES MATEMÁTICAS (módulo math) ---")
    angulo = math.pi / 4  # 45 grados en radianes
    numero = 16.7
    
    print(f"pi = {math.pi}")
    print(f"e = {math.e}")
    print(f"sqrt(16) = {math.sqrt(16)}")
    print(f"sin(π/4) = {math.sin(angulo)}")
    print(f"cos(π/4) = {math.cos(angulo)}")
    print(f"log(10) = {math.log(10)}")
    print(f"log10(100) = {math.log10(100)}")
    print(f"ceil(16.7) = {math.ceil(numero)}")
    print(f"floor(16.7) = {math.floor(numero)}")
    print(f"round(16.7) = {round(numero)}")
    print(f"round(16.7, 1) = {round(numero, 1)}")
    print()
    
    # Verificaciones especiales
    print("--- VERIFICACIONES ESPECIALES ---")
    print(f"math.isinf(float('inf')): {math.isinf(flotante_infinito)}")
    print(f"math.isnan(float('nan')): {math.isnan(flotante_nan)}")
    print(f"math.isfinite(3.14): {math.isfinite(3.14)}")
    print()
    
    # Problemas de precisión
    print("--- PRECISIÓN DE FLOTANTES ---")
    resultado = 0.1 + 0.1 + 0.1
    print(f"0.1 + 0.1 + 0.1 = {resultado}")
    print(f"¿Es igual a 0.3? {resultado == 0.3}")
    print(f"Diferencia: {abs(resultado - 0.3)}")
    
    # Solución con decimal para precisión
    from decimal import Decimal
    d1 = Decimal('0.1')
    d2 = d1 + d1 + d1
    print(f"Con Decimal: {d1} + {d1} + {d1} = {d2}")
    print()


def ejemplos_complejos():
    """Ejemplos con números complejos (complex)"""
    print("=" * 60)
    print("NÚMEROS COMPLEJOS (complex)")
    print("=" * 60)
    
    # Creación de números complejos
    complejo1 = 3 + 4j
    complejo2 = complex(2, -5)  # 2 - 5j
    complejo3 = complex('1+2j')
    complejo4 = 5j  # Parte imaginaria pura
    complejo5 = 7 + 0j  # Parte real pura
    
    print("--- CREACIÓN ---")
    print(f"3 + 4j: {complejo1}")
    print(f"complex(2, -5): {complejo2}")
    print(f"complex('1+2j'): {complejo3}")
    print(f"5j: {complejo4}")
    print(f"7 + 0j: {complejo5}")
    print(f"Tipo: {type(complejo1)}")
    print()
    
    # Acceso a partes real e imaginaria
    print("--- PARTES REAL E IMAGINARIA ---")
    z = 6 - 8j
    print(f"z = {z}")
    print(f"Parte real: z.real = {z.real}")
    print(f"Parte imaginaria: z.imag = {z.imag}")
    print(f"Conjugado: z.conjugate() = {z.conjugate()}")
    print()
    
    # OPERACIONES ARITMÉTICAS
    print("--- OPERACIONES ARITMÉTICAS ---")
    a = 3 + 4j
    b = 1 - 2j
    
    print(f"a = {a}, b = {b}")
    print(f"Suma: a + b = {a + b}")
    print(f"Resta: a - b = {a - b}")
    print(f"Multiplicación: a * b = {a * b}")
    print(f"División: a / b = {a / b}")
    print(f"Potencia: a ** 2 = {a ** 2}")
    print()
    
    # Funciones matemáticas con complejos
    import cmath
    
    print("--- FUNCIONES MATEMÁTICAS (módulo cmath) ---")
    z = 3 + 4j
    print(f"z = {z}")
    print(f"Módulo (valor absoluto): abs(z) = {abs(z)}")
    print(f"Fase (argumento): cmath.phase(z) = {cmath.phase(z)} radianes")
    print(f"Coordenadas polares: cmath.polar(z) = {cmath.polar(z)}")
    
    # Convertir de polar a rectangular
    r, theta = cmath.polar(z)
    z_rect = cmath.rect(r, theta)
    print(f"De polar a rectangular: cmath.rect({r}, {theta}) = {z_rect}")
    
    # Otras funciones
    print(f"Exponencial: cmath.exp(z) = {cmath.exp(z)}")
    print(f"Logaritmo: cmath.log(z) = {cmath.log(z)}")
    print(f"Raíz cuadrada: cmath.sqrt(z) = {cmath.sqrt(z)}")
    print(f"Seno: cmath.sin(z) = {cmath.sin(z)}")
    print()


def operaciones_mixtas():
    """Operaciones entre diferentes tipos numéricos"""
    print("=" * 60)
    print("OPERACIONES MIXTAS ENTRE TIPOS")
    print("=" * 60)
    
    entero = 10
    flotante = 3.5
    complejo = 2 + 3j
    
    print("--- PROMOCIÓN AUTOMÁTICA DE TIPOS ---")
    print(f"entero = {entero} (tipo: {type(entero).__name__})")
    print(f"flotante = {flotante} (tipo: {type(flotante).__name__})")
    print(f"complejo = {complejo} (tipo: {type(complejo).__name__})")
    print()
    
    # int + float = float
    resultado_int_float = entero + flotante
    print(f"int + float: {entero} + {flotante} = {resultado_int_float}")
    print(f"Tipo resultado: {type(resultado_int_float).__name__}")
    
    # int + complex = complex
    resultado_int_complex = entero + complejo
    print(f"int + complex: {entero} + {complejo} = {resultado_int_complex}")
    print(f"Tipo resultado: {type(resultado_int_complex).__name__}")
    
    # float + complex = complex
    resultado_float_complex = flotante + complejo
    print(f"float + complex: {flotante} + {complejo} = {resultado_float_complex}")
    print(f"Tipo resultado: {type(resultado_float_complex).__name__}")
    print()
    
    # CONVERSIONES EXPLÍCITAS
    print("--- CONVERSIONES EXPLÍCITAS ---")
    
    # Convertir a entero
    print(f"int(3.7) = {int(3.7)}")  # Trunca, no redondea
    print(f"int(-3.7) = {int(-3.7)}")
    print(f"int('123') = {int('123')}")
    print(f"int('1010', 2) = {int('1010', 2)}")  # Binario a decimal
    print(f"int('FF', 16) = {int('FF', 16)}")     # Hexadecimal a decimal
    
    # Convertir a flotante
    print(f"float(42) = {float(42)}")
    print(f"float('3.14') = {float('3.14')}")
    print(f"float('inf') = {float('inf')}")
    
    # Convertir a complejo
    print(f"complex(3) = {complex(3)}")
    print(f"complex(3.5) = {complex(3.5)}")
    print(f"complex(1, 2) = {complex(1, 2)}")
    print()


def ejemplos_operadores_asignacion():
    """Operadores de asignación compuesta"""
    print("=" * 60)
    print("OPERADORES DE ASIGNACIÓN COMPUESTA")
    print("=" * 60)
    
    # Con enteros
    x = 10
    print(f"Valor inicial: x = {x}")
    
    x += 5    # x = x + 5
    print(f"x += 5: x = {x}")
    
    x -= 3    # x = x - 3
    print(f"x -= 3: x = {x}")
    
    x *= 2    # x = x * 2
    print(f"x *= 2: x = {x}")
    
    x /= 4    # x = x / 4 (resultado es float)
    print(f"x /= 4: x = {x} (tipo: {type(x).__name__})")
    
    x = int(x)  # Convertir de vuelta a entero
    x //= 3   # x = x // 3
    print(f"x //= 3: x = {x}")
    
    x %= 4    # x = x % 4
    print(f"x %= 4: x = {x}")
    
    x **= 3   # x = x ** 3
    print(f"x **= 3: x = {x}")
    print()
    
    # Operadores bitwise de asignación
    print("--- OPERADORES BITWISE DE ASIGNACIÓN ---")
    y = 12  # 1100 en binario
    print(f"Valor inicial: y = {y} ({bin(y)})")
    
    y &= 10   # y = y & 10
    print(f"y &= 10: y = {y} ({bin(y)})")
    
    y |= 5    # y = y | 5
    print(f"y |= 5: y = {y} ({bin(y)})")
    
    y ^= 3    # y = y ^ 3
    print(f"y ^= 3: y = {y} ({bin(y)})")
    
    y <<= 1   # y = y << 1
    print(f"y <<= 1: y = {y} ({bin(y)})")
    
    y >>= 2   # y = y >> 2
    print(f"y >>= 2: y = {y} ({bin(y)})")
    print()


def funciones_utiles_numericas():
    """Funciones útiles para trabajar con números"""
    print("=" * 60)
    print("FUNCIONES ÚTILES PARA NÚMEROS")
    print("=" * 60)
    
    # isinstance() para verificar tipos
    valores = [42, 3.14, 2+3j, True, "123"]
    
    print("--- VERIFICACIÓN DE TIPOS ---")
    for valor in valores:
        print(f"Valor: {valor}")
        print(f"  Es int: {isinstance(valor, int)}")
        print(f"  Es float: {isinstance(valor, float)}")
        print(f"  Es complex: {isinstance(valor, complex)}")
        print(f"  Es número: {isinstance(valor, (int, float, complex))}")
        print()
    
    # Funciones de conversión con validación
    def convertir_a_numero(valor):
        """Intenta convertir un valor a número"""
        try:
            # Intentar int primero
            if '.' not in str(valor) and 'j' not in str(valor):
                return int(valor)
            elif 'j' in str(valor):
                return complex(valor)
            else:
                return float(valor)
        except ValueError:
            return None
    
    print("--- CONVERSIÓN INTELIGENTE ---")
    test_valores = ["42", "3.14", "2+3j", "abc", "-17", "1e6"]
    
    for valor in test_valores:
        resultado = convertir_a_numero(valor)
        print(f"'{valor}' -> {resultado} (tipo: {type(resultado).__name__})")
    print()


if __name__ == "__main__":
    ejemplos_enteros()
    operadores_comparacion_enteros()
    operadores_bitwise()
    ejemplos_flotantes()
    ejemplos_complejos()
    operaciones_mixtas()
    ejemplos_operadores_asignacion()
    funciones_utiles_numericas()