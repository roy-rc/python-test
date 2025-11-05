#!/usr/bin/env python3
"""
Main runner para todos los ejemplos de tipos de datos básicos de Python
Ejecuta todos los archivos de ejemplos con menú interactivo
"""

import os
import sys
import importlib.util
from pathlib import Path

# Obtener el directorio del script actual
SCRIPT_DIR = Path(__file__).parent
CODE_DIR = SCRIPT_DIR / "code"

# Información de los módulos de tipos de datos
MODULOS_TIPOS = [
    {
        'archivo': 'tipos_numericos.py',
        'nombre': 'Tipos Numéricos',
        'descripcion': 'int, float, complex y operadores aritméticos',
        'funciones_principales': [
            'ejemplos_enteros',
            'ejemplos_flotantes', 
            'ejemplos_complejos',
            'operadores_aritmeticos',
            'operadores_bitwise',
            'funciones_matematicas'
        ]
    },
    {
        'archivo': 'tipos_strings.py',
        'nombre': 'Strings',
        'descripcion': 'Manipulación de cadenas, métodos y formateo',
        'funciones_principales': [
            'creacion_strings',
            'operadores_strings',
            'metodos_strings',
            'formateo_strings',
            'encoding_unicode'
        ]
    },
    {
        'archivo': 'tipos_booleanos.py',
        'nombre': 'Tipos Booleanos',
        'descripcion': 'Operadores lógicos y evaluación booleana',
        'funciones_principales': [
            'valores_booleanos',
            'operadores_logicos',
            'cortocircuito_evaluacion',
            'precedencia_operadores',
            'casos_uso_practicos'
        ]
    },
    {
        'archivo': 'tipos_secuencias.py',
        'nombre': 'Tipos Secuencias',
        'descripcion': 'list, tuple, range y operaciones comunes',
        'funciones_principales': [
            'ejemplos_listas',
            'ejemplos_tuplas',
            'ejemplos_ranges',
            'operadores_secuencias',
            'comparacion_secuencias'
        ]
    },
    {
        'archivo': 'tipos_conjuntos.py',
        'nombre': 'Conjuntos (Sets)',
        'descripcion': 'set, frozenset y operaciones matemáticas',
        'funciones_principales': [
            'creacion_conjuntos',
            'operadores_conjuntos',
            'metodos_conjuntos',
            'relaciones_conjuntos',
            'casos_uso_practicos'
        ]
    },
    {
        'archivo': 'tipos_diccionarios.py',
        'nombre': 'Diccionarios',
        'descripcion': 'dict, métodos y casos de uso avanzados',
        'funciones_principales': [
            'creacion_diccionarios',
            'acceso_modificacion',
            'metodos_diccionarios',
            'operadores_diccionarios',
            'comprension_diccionarios',
            'casos_uso_avanzados'
        ]
    },
    {
        'archivo': 'tipos_especiales.py',
        'nombre': 'Tipos Especiales',
        'descripcion': 'None, bytes, bytearray, memoryview',
        'funciones_principales': [
            'ejemplos_none',
            'ejemplos_bytes',
            'ejemplos_bytearray',
            'ejemplos_memoryview',
            'conversion_entre_tipos',
            'casos_uso_practicos_bytes'
        ]
    }
]


def verificar_archivos():
    """Verifica que todos los archivos de tipos de datos existan"""
    archivos_faltantes = []
    archivos_disponibles = []
    
    for modulo in MODULOS_TIPOS:
        archivo_path = CODE_DIR / modulo['archivo']
        if archivo_path.exists():
            archivos_disponibles.append(modulo)
        else:
            archivos_faltantes.append(modulo['archivo'])
    
    return archivos_disponibles, archivos_faltantes


def cargar_modulo(archivo_path):
    """Carga dinámicamente un módulo desde su path"""
    try:
        spec = importlib.util.spec_from_file_location("modulo_temp", archivo_path)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        return modulo, None
    except Exception as e:
        return None, str(e)


def ejecutar_funcion(modulo, nombre_funcion):
    """Ejecuta una función específica del módulo"""
    try:
        if hasattr(modulo, nombre_funcion):
            funcion = getattr(modulo, nombre_funcion)
            funcion()
            return True
        else:
            print(f"Función '{nombre_funcion}' no encontrada en el módulo")
            return False
    except Exception as e:
        print(f"Error ejecutando '{nombre_funcion}': {e}")
        return False


def ejecutar_archivo_completo(modulo_info):
    """Ejecuta todas las funciones principales de un archivo"""
    archivo_path = CODE_DIR / modulo_info['archivo']
    
    print("=" * 80)
    print(f"EJECUTANDO: {modulo_info['nombre'].upper()}")
    print("=" * 80)
    print(f"Archivo: {modulo_info['archivo']}")
    print(f"Descripción: {modulo_info['descripcion']}")
    print()
    
    # Cargar el módulo
    modulo, error = cargar_modulo(archivo_path)
    if not modulo:
        print(f"Error cargando el módulo: {error}")
        return False
    
    # Ejecutar cada función principal
    funciones_exitosas = 0
    for nombre_funcion in modulo_info['funciones_principales']:
        print(f"\n--- Ejecutando {nombre_funcion}() ---")
        if ejecutar_funcion(modulo, nombre_funcion):
            funciones_exitosas += 1
        print()  # Espacio entre funciones
    
    total_funciones = len(modulo_info['funciones_principales'])
    print(f"Funciones ejecutadas exitosamente: {funciones_exitosas}/{total_funciones}")
    
    return funciones_exitosas == total_funciones


def ejecutar_funcion_especifica():
    """Permite al usuario ejecutar una función específica"""
    print("\nMÓDULOS DISPONIBLES:")
    archivos_disponibles, _ = verificar_archivos()
    
    for i, modulo in enumerate(archivos_disponibles, 1):
        print(f"{i:2d}. {modulo['nombre']} - {modulo['descripcion']}")
    
    try:
        seleccion = int(input(f"\nSeleccione módulo (1-{len(archivos_disponibles)}): "))
        if 1 <= seleccion <= len(archivos_disponibles):
            modulo_seleccionado = archivos_disponibles[seleccion - 1]
            
            print(f"\nFUNCIONES DISPONIBLES en {modulo_seleccionado['nombre']}:")
            funciones = modulo_seleccionado['funciones_principales']
            
            for i, funcion in enumerate(funciones, 1):
                print(f"{i:2d}. {funcion}()")
            
            sel_func = int(input(f"\nSeleccione función (1-{len(funciones)}): "))
            if 1 <= sel_func <= len(funciones):
                funcion_seleccionada = funciones[sel_func - 1]
                
                # Cargar y ejecutar
                archivo_path = CODE_DIR / modulo_seleccionado['archivo']
                modulo, error = cargar_modulo(archivo_path)
                
                if modulo:
                    print(f"\n{'='*60}")
                    print(f"EJECUTANDO: {funcion_seleccionada}()")
                    print(f"{'='*60}")
                    ejecutar_funcion(modulo, funcion_seleccionada)
                else:
                    print(f"Error cargando módulo: {error}")
            else:
                print("Selección de función inválida")
        else:
            print("Selección de módulo inválida")
    except ValueError:
        print("Entrada inválida")
    except KeyboardInterrupt:
        print("\nOperación cancelada")


def mostrar_resumen():
    """Muestra un resumen de todos los tipos de datos disponibles"""
    print("=" * 80)
    print("RESUMEN DE TIPOS DE DATOS BÁSICOS EN PYTHON")
    print("=" * 80)
    
    archivos_disponibles, archivos_faltantes = verificar_archivos()
    
    print(f"Archivos disponibles: {len(archivos_disponibles)}")
    print(f"Archivos faltantes: {len(archivos_faltantes)}")
    print()
    
    if archivos_disponibles:
        print("TIPOS DE DATOS CUBIERTOS:")
        print("-" * 40)
        
        for i, modulo in enumerate(archivos_disponibles, 1):
            print(f"{i:2d}. {modulo['nombre']}")
            print(f"    Archivo: {modulo['archivo']}")
            print(f"    Descripción: {modulo['descripcion']}")
            print(f"    Funciones: {len(modulo['funciones_principales'])}")
            
            # Mostrar funciones principales
            for func in modulo['funciones_principales']:
                print(f"      - {func}()")
            print()
    
    if archivos_faltantes:
        print("ARCHIVOS FALTANTES:")
        print("-" * 20)
        for archivo in archivos_faltantes:
            print(f"  - {archivo}")
        print()
    
    # Estadísticas
    total_funciones = sum(len(m['funciones_principales']) for m in archivos_disponibles)
    print("ESTADÍSTICAS:")
    print(f"  - Total de módulos: {len(archivos_disponibles)}")
    print(f"  - Total de funciones de ejemplo: {total_funciones}")
    print(f"  - Tipos principales cubiertos: int, float, complex, str, bool, list, tuple, range, set, frozenset, dict, None, bytes, bytearray, memoryview")
    print()


def menu_principal():
    """Menú principal interactivo"""
    archivos_disponibles, archivos_faltantes = verificar_archivos()
    
    if archivos_faltantes:
        print("⚠️  ADVERTENCIA: Algunos archivos no están disponibles:")
        for archivo in archivos_faltantes:
            print(f"   - {archivo}")
        print()
    
    while True:
        print("=" * 80)
        print("MENÚ PRINCIPAL - EJEMPLOS DE TIPOS DE DATOS PYTHON")
        print("=" * 80)
        print("1. Mostrar resumen de todos los tipos")
        print("2. Ejecutar todos los ejemplos (secuencial)")
        print("3. Ejecutar archivo específico")
        print("4. Ejecutar función específica")
        print("5. Información del sistema Python")
        print("0. Salir")
        print("-" * 80)
        
        try:
            opcion = input("Seleccione una opción (0-5): ").strip()
            
            if opcion == '0':
                print("¡Hasta luego!")
                break
            elif opcion == '1':
                mostrar_resumen()
                input("\nPresione Enter para continuar...")
            elif opcion == '2':
                ejecutar_todos_secuencial(archivos_disponibles)
                input("\nPresione Enter para continuar...")
            elif opcion == '3':
                ejecutar_archivo_especifico(archivos_disponibles)
                input("\nPresione Enter para continuar...")
            elif opcion == '4':
                ejecutar_funcion_especifica()
                input("\nPresione Enter para continuar...")
            elif opcion == '5':
                mostrar_info_sistema()
                input("\nPresione Enter para continuar...")
            else:
                print("Opción inválida. Intente de nuevo.")
        
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break
        except EOFError:
            print("\n\n¡Hasta luego!")
            break


def ejecutar_todos_secuencial(archivos_disponibles):
    """Ejecuta todos los archivos de forma secuencial"""
    print("\n🚀 EJECUTANDO TODOS LOS EJEMPLOS SECUENCIALMENTE")
    print("=" * 80)
    
    resultados = []
    
    for i, modulo in enumerate(archivos_disponibles, 1):
        print(f"\n[{i}/{len(archivos_disponibles)}] Procesando: {modulo['nombre']}")
        
        # Preguntar si continuar (excepto el primero)
        if i > 1:
            continuar = input("Continuar con el siguiente módulo? (S/n): ").strip().lower()
            if continuar == 'n':
                print("Ejecución cancelada por el usuario")
                break
        
        resultado = ejecutar_archivo_completo(modulo)
        resultados.append((modulo['nombre'], resultado))
        
        if i < len(archivos_disponibles):
            print("\n" + "="*80)
    
    # Resumen de resultados
    print("\n" + "="*80)
    print("RESUMEN DE EJECUCIÓN")
    print("="*80)
    
    exitosos = 0
    for nombre, resultado in resultados:
        estado = "✅ EXITOSO" if resultado else "❌ ERROR"
        print(f"{estado:12} - {nombre}")
        if resultado:
            exitosos += 1
    
    print(f"\nResultado: {exitosos}/{len(resultados)} módulos ejecutados exitosamente")


def ejecutar_archivo_especifico(archivos_disponibles):
    """Permite al usuario seleccionar y ejecutar un archivo específico"""
    print("\nARCHIVOS DISPONIBLES:")
    
    for i, modulo in enumerate(archivos_disponibles, 1):
        print(f"{i:2d}. {modulo['nombre']}")
        print(f"    {modulo['descripcion']}")
    
    try:
        seleccion = int(input(f"\nSeleccione archivo (1-{len(archivos_disponibles)}): "))
        if 1 <= seleccion <= len(archivos_disponibles):
            modulo_seleccionado = archivos_disponibles[seleccion - 1]
            ejecutar_archivo_completo(modulo_seleccionado)
        else:
            print("Selección inválida")
    except ValueError:
        print("Entrada inválida")
    except KeyboardInterrupt:
        print("\nOperación cancelada")


def mostrar_info_sistema():
    """Muestra información del sistema Python"""
    print("=" * 60)
    print("INFORMACIÓN DEL SISTEMA PYTHON")
    print("=" * 60)
    
    print(f"Versión de Python: {sys.version}")
    print(f"Plataforma: {sys.platform}")
    print(f"Executable: {sys.executable}")
    print(f"Path del script: {__file__}")
    print(f"Directorio de código: {CODE_DIR}")
    print(f"Directorio actual: {os.getcwd()}")
    
    # Información de módulos
    print(f"\nMódulos integrados disponibles: {len(sys.builtin_module_names)}")
    print("Algunos módulos integrados importantes:")
    modulos_importantes = ['builtins', 'sys', 'os', 'math', 'itertools', 'collections']
    for mod in modulos_importantes:
        if mod in sys.builtin_module_names:
            print(f"  ✅ {mod}")
        else:
            print(f"  ❌ {mod}")
    
    # Información de encoding
    print(f"\nEncoding por defecto: {sys.getdefaultencoding()}")
    print(f"Encoding del sistema de archivos: {sys.getfilesystemencoding()}")
    
    # Límites del sistema
    print(f"\nRecursión máxima: {sys.getrecursionlimit()}")
    print(f"Tamaño máximo de int: Sin límite (Python 3)")


if __name__ == "__main__":
    print("🐍 EJEMPLOS DE TIPOS DE DATOS BÁSICOS EN PYTHON")
    print("Autor: Ejemplos educativos")
    print(f"Ubicación: {SCRIPT_DIR}")
    print()
    
    # Verificar estructura de directorios
    if not CODE_DIR.exists():
        print(f"❌ Error: Directorio '{CODE_DIR}' no encontrado")
        sys.exit(1)
    
    # Ejecutar menú principal
    try:
        menu_principal()
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        sys.exit(1)