#!/usr/bin/env python3
"""
Archivo principal para ejecutar todos los ejemplos de manejo de listas y arrays
Importa y ejecuta todas las demostraciones de forma organizada
"""

import sys
import os

def main():
    """Función principal que ejecuta todos los ejemplos"""
    print("=" * 80)
    print("EJEMPLOS COMPLETOS DE MANEJO DE LISTAS Y ARRAYS")
    print("Python nativo y NumPy")
    print("=" * 80)
    print()
    
    # Lista de módulos a ejecutar
    ejemplos = [
        {
            'nombre': 'Listas Básicas de Python',
            'archivo': 'listas_basicas.py',
            'descripcion': 'Búsqueda, agregado y eliminación en listas 1D y 2D'
        },
        {
            'nombre': 'Arrays NumPy 1D',
            'archivo': 'numpy_arrays_1d.py',
            'descripcion': 'Manejo completo de arrays unidimensionales'
        },
        {
            'nombre': 'Arrays NumPy 2D',
            'archivo': 'numpy_arrays_2d.py',
            'descripcion': 'Manejo completo de arrays bidimensionales (matrices)'
        },
        {
            'nombre': 'Unión de Listas Python',
            'archivo': 'union_listas.py',
            'descripcion': 'Diferentes métodos para unir múltiples listas'
        },
        {
            'nombre': 'Unión de Arrays NumPy',
            'archivo': 'union_arrays_numpy.py',
            'descripcion': 'Concatenación y apilamiento de arrays NumPy'
        }
    ]
    
    # Verificar que NumPy esté disponible
    numpy_disponible = verificar_numpy()
    
    # Mostrar menú de opciones
    mostrar_menu(ejemplos, numpy_disponible)
    
    while True:
        try:
            opcion = input("\nSeleccione una opción (0 para salir): ").strip()
            
            if opcion == '0':
                print("¡Gracias por usar los ejemplos!")
                break
            elif opcion == 'all':
                ejecutar_todos_ejemplos(ejemplos, numpy_disponible)
            elif opcion.isdigit():
                indice = int(opcion) - 1
                if 0 <= indice < len(ejemplos):
                    ejecutar_ejemplo_individual(ejemplos[indice], numpy_disponible)
                else:
                    print("Opción no válida. Intente de nuevo.")
            else:
                print("Opción no válida. Intente de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\nInterrumpido por el usuario. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"Error: {e}")


def verificar_numpy():
    """Verifica si NumPy está disponible"""
    try:
        import numpy as np
        print(f"✓ NumPy {np.__version__} está disponible")
        return True
    except ImportError:
        print("⚠ NumPy no está disponible. Los ejemplos de NumPy no se ejecutarán.")
        print("  Para instalar NumPy: pip install numpy")
        return False


def mostrar_menu(ejemplos, numpy_disponible):
    """Muestra el menú de opciones"""
    print("\nEJEMPLOS DISPONIBLES:")
    print("-" * 50)
    
    for i, ejemplo in enumerate(ejemplos, 1):
        disponible = "✓" if (numpy_disponible or "numpy" not in ejemplo['archivo'].lower()) else "⚠"
        print(f"{disponible} {i}. {ejemplo['nombre']}")
        print(f"     {ejemplo['descripcion']}")
        print(f"     Archivo: {ejemplo['archivo']}")
        print()
    
    print("OPCIONES ESPECIALES:")
    print("  all - Ejecutar todos los ejemplos disponibles")
    print("  0   - Salir")


def ejecutar_todos_ejemplos(ejemplos, numpy_disponible):
    """Ejecuta todos los ejemplos disponibles"""
    print("\n" + "=" * 80)
    print("EJECUTANDO TODOS LOS EJEMPLOS")
    print("=" * 80)
    
    for i, ejemplo in enumerate(ejemplos, 1):
        # Saltar ejemplos de NumPy si no está disponible
        if not numpy_disponible and "numpy" in ejemplo['archivo'].lower():
            print(f"\n⚠ Saltando {ejemplo['nombre']} (NumPy no disponible)")
            continue
            
        print(f"\n{'='*20} EJEMPLO {i}: {ejemplo['nombre']} {'='*20}")
        ejecutar_archivo(ejemplo['archivo'])
        
        # Pausa entre ejemplos
        input("\nPresione Enter para continuar al siguiente ejemplo...")


def ejecutar_ejemplo_individual(ejemplo, numpy_disponible):
    """Ejecuta un ejemplo individual"""
    # Verificar si es ejemplo de NumPy y si está disponible
    if not numpy_disponible and "numpy" in ejemplo['archivo'].lower():
        print(f"\n⚠ No se puede ejecutar {ejemplo['nombre']} porque NumPy no está disponible.")
        print("  Para instalar NumPy: pip install numpy")
        return
    
    print(f"\n{'='*60}")
    print(f"EJECUTANDO: {ejemplo['nombre']}")
    print(f"Descripción: {ejemplo['descripcion']}")
    print(f"Archivo: {ejemplo['archivo']}")
    print("="*60)
    
    ejecutar_archivo(ejemplo['archivo'])


def ejecutar_archivo(nombre_archivo):
    """Ejecuta un archivo Python específico"""
    try:
        # Construir la ruta completa del archivo
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
        
        if not os.path.exists(ruta_archivo):
            print(f"Error: No se encontró el archivo {nombre_archivo}")
            return
        
        # Ejecutar el archivo
        print(f"Ejecutando {nombre_archivo}...\n")
        
        # Usar exec para ejecutar el archivo
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            
        # Crear un namespace limpio para la ejecución
        namespace = {
            '__name__': '__main__',
            '__file__': ruta_archivo
        }
        
        exec(codigo, namespace)
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    except ImportError as e:
        print(f"Error de importación en {nombre_archivo}: {e}")
        if "numpy" in str(e).lower():
            print("Sugerencia: Instale NumPy con 'pip install numpy'")
    except Exception as e:
        print(f"Error al ejecutar {nombre_archivo}: {e}")


def mostrar_resumen():
    """Muestra un resumen de todos los conceptos cubiertos"""
    print("\n" + "=" * 80)
    print("RESUMEN DE CONCEPTOS CUBIERTOS")
    print("=" * 80)
    
    conceptos = {
        "LISTAS PYTHON": [
            "• Búsqueda: in, index(), count(), list comprehensions",
            "• Agregado: append(), insert(), extend(), concatenación (+)",
            "• Eliminación: remove(), pop(), del, clear(), filtrado",
            "• Listas 2D: acceso, modificación, búsqueda en matrices"
        ],
        "ARRAYS NUMPY 1D": [
            "• Creación: array(), arange(), linspace(), zeros(), ones()",
            "• Búsqueda: where(), argmax(), argmin(), condiciones booleanas",
            "• Agregado: append(), insert(), concatenate()",
            "• Eliminación: delete(), filtrado con máscaras booleanas"
        ],
        "ARRAYS NUMPY 2D": [
            "• Matrices: creación, reshape(), acceso por índices",
            "• Agregado: append filas/columnas, insert(), concatenate()",
            "• Eliminación: delete filas/columnas, filtrado avanzado",
            "• Operaciones: transpose(), dot(), estadísticas por ejes"
        ],
        "UNIÓN DE LISTAS": [
            "• Métodos básicos: +, extend(), +=, sum()",
            "• Funciones avanzadas: itertools.chain(), reduce()",
            "• Comprehensions, intercalado, eliminación de duplicados",
            "• Preservación de orden, filtrado durante unión"
        ],
        "UNIÓN DE ARRAYS": [
            "• Concatenación: concatenate(), r_, c_",
            "• Apilamiento: vstack(), hstack(), dstack(), stack()",
            "• Dimensiones: expand_dims(), reshape(), broadcasting",
            "• Avanzado: tile(), repeat(), arrays estructurados"
        ]
    }
    
    for categoria, items in conceptos.items():
        print(f"\n{categoria}:")
        for item in items:
            print(f"  {item}")
    
    print(f"\n{'='*80}")
    print("ARCHIVOS CREADOS:")
    print("  • listas_basicas.py - Ejemplos de listas Python")
    print("  • numpy_arrays_1d.py - Arrays NumPy unidimensionales")
    print("  • numpy_arrays_2d.py - Arrays NumPy bidimensionales")
    print("  • union_listas.py - Unión de listas Python")
    print("  • union_arrays_numpy.py - Unión de arrays NumPy")
    print("  • main.py - Este archivo principal")
    print("="*80)


if __name__ == "__main__":
    try:
        main()
        mostrar_resumen()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido. ¡Hasta luego!")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        sys.exit(1)