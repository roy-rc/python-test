# Ejemplos Completos de Python - Listas, Arrays y Tipos de Datos

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-enabled-blue.svg)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/flask-web_example-green.svg)](https://flask.palletsprojects.com/)
[![NumPy](https://img.shields.io/badge/numpy-optional-orange.svg)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este repositorio contiene una colección completa de ejemplos educativos de Python, cubriendo tanto el manejo de listas/arrays como los tipos de datos básicos del lenguaje. Está organizado en múltiples archivos especializados para facilitar el seguimiento y aprendizaje progresivo.

> 🎯 **Ideal para**: Estudiantes de Python, instructores, desarrolladores que buscan referencia rápida, y cualquiera que quiera dominar los fundamentos del lenguaje.

## 📋 Contenido

## 🎯 **PARTE 1: Tipos de Datos Básicos**

### 🔢 Tipos Numéricos
- **`code/tipos_numericos.py`** - Enteros, flotantes y complejos
  - Operadores aritméticos (+, -, *, /, //, %, **)
  - Operadores bitwise (&, |, ^, <<, >>, ~)
  - Funciones matemáticas (abs, round, divmod)
  - Números complejos y operaciones
  - Conversiones entre tipos

### 📝 Strings (Cadenas)
- **`code/tipos_strings.py`** - Manipulación completa de strings
  - Operadores de cadenas (+, *, in, comparación)
  - Métodos de strings (upper, lower, split, join, etc.)
  - Formateo (f-strings, format(), % formatting)
  - Encoding y Unicode
  - Expresiones regulares básicas

### ✅ Tipos Booleanos
- **`code/tipos_booleanos.py`** - Operadores lógicos y evaluación
  - Valores booleanos (True, False, truthiness)
  - Operadores lógicos (and, or, not)
  - Evaluación de cortocircuito
  - Precedencia de operadores
  - Casos de uso prácticos

### 📚 Tipos Secuencias
- **`code/tipos_secuencias.py`** - Listas, tuplas y ranges
  - Listas (mutables) vs tuplas (inmutables)
  - Ranges para iteración eficiente
  - Operadores comunes (len, in, +, *, slicing)
  - Comparaciones entre tipos de secuencia
  - Unpacking y empaquetado

### 🔗 Conjuntos (Sets)
- **`code/tipos_conjuntos.py`** - Sets y operaciones matemáticas
  - Sets mutables vs frozensets inmutables
  - Operadores de conjuntos (|, &, -, ^)
  - Métodos de conjuntos (union, intersection, difference)
  - Relaciones entre conjuntos
  - Casos de uso para eliminación de duplicados

### 🗂️ Diccionarios
- **`code/tipos_diccionarios.py`** - Mapeo clave-valor
  - Creación y acceso a diccionarios
  - Métodos principales (keys, values, items, get)
  - Operadores y comprensiones de diccionarios
  - Casos de uso avanzados (defaultdict, Counter)
  - Análisis de rendimiento

### 🔧 Tipos Especiales
- **`code/tipos_especiales.py`** - None, bytes y memoria
  - NoneType y el singleton None
  - Bytes inmutables vs bytearray mutables
  - Memoryview para eficiencia de memoria
  - Conversiones entre tipos binarios
  - Casos prácticos con archivos y protocolos

### 🚀 Archivos Principales
- **`main.py`** - Ejecutor para ejemplos de listas y arrays
  - Verificación automática de dependencias NumPy
  - Menú de selección de ejemplos
  - Ejecución individual o de todos los ejemplos
  - Resumen completo de conceptos

- **`main_tipos_datos.py`** - Ejecutor para ejemplos de tipos de datos
  - Menú interactivo completo
  - Ejecución secuencial o selectiva
  - Información del sistema Python
  - Navegación por funciones específicas

- **`app.py`** - Ejemplo web con Flask
  - Servidor web simple con Flask
  - Endpoint básico de demostración
  - Configurado para desarrollo con recarga automática
  - Accesible en puerto 5000

## 🎯 **PARTE 2: Listas y Arrays**

### 🐍 Listas Python Nativas
- **`code/listas_basicas.py`** - Ejemplos fundamentales de listas Python
  - Búsqueda de elementos (`in`, `index()`, `count()`)
  - Agregado de elementos (`append()`, `insert()`, `extend()`, `+`)
  - Eliminación de elementos (`remove()`, `pop()`, `del`, `clear()`)
  - Listas bidimensionales (listas de listas)
  - Comprensiones de lista y filtrado avanzado

### 🔢 Arrays NumPy
- **`code/numpy_arrays_1d.py`** - Arrays unidimensionales
  - Creación (`array()`, `arange()`, `linspace()`, `zeros()`, `ones()`)
  - Búsqueda (`where()`, `argmax()`, `argmin()`, condiciones booleanas)
  - Agregado (`append()`, `insert()`, `concatenate()`)
  - Eliminación (`delete()`, filtrado con máscaras)
  - Operaciones estadísticas y matemáticas

- **`code/numpy_arrays_2d.py`** - Arrays bidimensionales (matrices)
  - Creación de matrices
  - Acceso y modificación por índices
  - Agregado/eliminación de filas y columnas
  - Operaciones matriciales (`dot()`, `transpose()`)
  - Estadísticas por ejes

### 🔗 Unión de Estructuras
- **`code/union_listas.py`** - Unión de múltiples listas Python
  - Concatenación básica (`+`, `extend()`, `+=`)
  - Funciones avanzadas (`itertools.chain()`, `reduce()`)
  - Intercalado de elementos
  - Eliminación de duplicados
  - Preservación del orden

- **`code/union_arrays_numpy.py`** - Unión de arrays NumPy
  - Concatenación (`concatenate()`, `r_`, `c_`)
  - Apilamiento (`vstack()`, `hstack()`, `dstack()`, `stack()`)
  - Manejo de diferentes dimensiones
  - Broadcasting y repetición (`tile()`, `repeat()`)

## 🛠️ Instalación y Uso

### Prerrequisitos
```bash
# Python 3.6+
python --version

# Instalar NumPy (opcional, pero recomendado)
pip install numpy
```

### Instalación Local
```bash
# Instalar dependencias
pip install -r requirements.txt
```

### 🐳 Instalación con Docker

#### Opción 1: Docker Compose (Recomendado)
```bash
# Construir e iniciar el servidor Flask
docker-compose up --build
# Acceder a http://localhost:5000

# Ejecutar ejemplos interactivos
docker-compose run --rm web python main.py

# Ejecutar ejemplos de tipos de datos
docker-compose run --rm web python main_tipos_datos.py

# Ejecutar archivos individuales
docker-compose run --rm web python code/tipos_numericos.py
```

#### Opción 2: Docker tradicional
```bash
# Construir la imagen
docker build -t python-ejemplos .

# Ejecutar servidor Flask
docker run -p 5000:5000 python-ejemplos
# Acceder a http://localhost:5000

# Ejecutar ejemplos interactivos
docker run -it --rm -v $(pwd):/app python-ejemplos python main.py

# Ejecutar ejemplos específicos
docker run -it --rm -v $(pwd):/app python-ejemplos python main_tipos_datos.py
```

### Ejecución

#### Menús Interactivos (Recomendado)
```bash
# Para ejemplos de listas y arrays
python main.py

# Para ejemplos de tipos de datos básicos
python main_tipos_datos.py
```

#### Ejecución Individual - Listas y Arrays
```bash
# Ejemplos de listas básicas (sin dependencias)
python code/listas_basicas.py

# Ejemplos de arrays NumPy (requiere numpy)
python code/numpy_arrays_1d.py
python code/numpy_arrays_2d.py

# Ejemplos de unión
python code/union_listas.py
python code/union_arrays_numpy.py
```

#### Ejecución Individual - Tipos de Datos
```bash
# Tipos básicos (sin dependencias externas)
python code/tipos_numericos.py
python code/tipos_strings.py
python code/tipos_booleanos.py
python code/tipos_secuencias.py
python code/tipos_conjuntos.py
python code/tipos_diccionarios.py
python code/tipos_especiales.py

# Ejecutar servidor Flask
python app.py
# Acceder a http://localhost:5000
```

## 📚 Conceptos Cubiertos

### 🔹 **Listas y Arrays**

#### Listas Python
- ✅ Búsqueda: `in`, `index()`, `count()`, comprensiones
- ✅ Agregado: `append()`, `insert()`, `extend()`, concatenación
- ✅ Eliminación: `remove()`, `pop()`, `del`, `clear()`
- ✅ Listas 2D: acceso, modificación, navegación
- ✅ Filtrado y transformación avanzada

#### Arrays NumPy
- ✅ Creación eficiente de arrays
- ✅ Indexación y slicing avanzado
- ✅ Máscaras booleanas para filtrado
- ✅ Operaciones vectorizadas
- ✅ Manipulación de forma (`reshape()`, `flatten()`)
- ✅ Estadísticas y matemáticas optimizadas

#### Unión de Estructuras
- ✅ Múltiples métodos de concatenación
- ✅ Preservación vs alteración del orden
- ✅ Eliminación de duplicados
- ✅ Intercalado de elementos
- ✅ Manejo de diferentes tipos de datos
- ✅ Optimización para grandes volúmenes

### 🔹 **Tipos de Datos Básicos**

#### Tipos Numéricos
- ✅ Enteros: operaciones, conversiones, límites
- ✅ Flotantes: precisión, notación científica, especiales (inf, nan)
- ✅ Complejos: parte real/imaginaria, operaciones matemáticas
- ✅ Operadores: aritméticos, bitwise, comparación
- ✅ Funciones: math, cmath, conversiones

#### Strings y Texto
- ✅ Creación y literales de cadenas
- ✅ Operadores: concatenación, repetición, pertenencia
- ✅ Métodos: transformación, búsqueda, validación
- ✅ Formateo: f-strings, format(), % formatting
- ✅ Encoding: UTF-8, ASCII, Unicode

#### Tipos Lógicos y Colecciones
- ✅ Booleanos: valores, operadores lógicos, truthiness
- ✅ Listas y tuplas: mutabilidad, operaciones, unpacking
- ✅ Ranges: creación eficiente, iteración
- ✅ Sets: operaciones matemáticas, eliminación duplicados
- ✅ Diccionarios: mapeo, métodos, comprensiones

#### Tipos Especiales y Memoria
- ✅ None: singleton, usos, comparaciones
- ✅ Bytes: datos binarios inmutables
- ✅ Bytearray: datos binarios mutables
- ✅ Memoryview: acceso eficiente a memoria
- ✅ Conversiones entre tipos binarios

## 🎯 Características de los Ejemplos

- **📂 Organización Modular**: Cada concepto en su propio archivo
- **💬 Comentarios Detallados**: Explicaciones línea por línea
- **🔍 Casos Prácticos**: Ejemplos del mundo real
- **⚡ Progresión Gradual**: De básico a avanzado
- **🛡️ Manejo de Errores**: Casos edge y validaciones
- **📊 Output Formateado**: Salida clara y legible
- **🔄 Ejemplos Interactivos**: Ejecución paso a paso

## 📖 Guía de Uso

### Para Principiantes
1. **Tipos de datos básicos**: Comience con `main_tipos_datos.py`
   - Explore `tipos_numericos.py` y `tipos_strings.py` primero
   - Practique cada concepto en el intérprete interactivo
   - Avance gradualmente a tipos más complejos

2. **Listas y arrays**: Continue con `main.py`
   - Comience con `listas_basicas.py`
   - Experimente con los ejemplos paso a paso
   - Avance a NumPy cuando se sienta cómodo

### Para Usuarios Intermedios
1. Use ambos menús principales (`main.py` y `main_tipos_datos.py`)
2. Compare las diferencias entre tipos similares (list vs tuple, set vs frozenset)
3. Analice las diferencias de rendimiento entre listas nativas y arrays NumPy
4. Experimente modificando los ejemplos para casos específicos

### Para Usuarios Avanzados
1. Analice las optimizaciones y casos de uso de cada tipo
2. Estudie los casos prácticos y implementaciones eficientes
3. Use como referencia para decisiones de arquitectura
4. Contribuya con ejemplos adicionales o mejoras

## 🔧 Estructura del Proyecto

```
python-ejemplos/
├── main.py                      # Ejecutor para listas y arrays
├── main_tipos_datos.py          # Ejecutor para tipos de datos
├── app.py                       # Ejemplo web Flask
├── requirements.txt             # Dependencias del proyecto
├── README.md                   # Este archivo
├── app.code-workspace          # Configuración VS Code workspace
│
# === CONFIGURACIÓN DOCKER ===
├── Dockerfile                  # Imagen Python 3.12 con dependencias
├── docker-compose.yml         # Orquestación y configuración de servicios
│
└── code/                      # Directorio de ejemplos
    ├── constant.py            # Constantes del proyecto
    │
    # === LISTAS Y ARRAYS ===
    ├── listas_basicas.py      # Listas Python nativas
    ├── numpy_arrays_1d.py     # Arrays NumPy 1D
    ├── numpy_arrays_2d.py     # Arrays NumPy 2D
    ├── union_listas.py        # Unión de listas Python
    ├── union_arrays_numpy.py  # Unión de arrays NumPy
    │
    # === TIPOS DE DATOS BÁSICOS ===
    ├── tipos_numericos.py     # int, float, complex
    ├── tipos_strings.py       # str, formateo, encoding
    ├── tipos_booleanos.py     # bool, operadores lógicos
    ├── tipos_secuencias.py    # list, tuple, range
    ├── tipos_conjuntos.py     # set, frozenset
    ├── tipos_diccionarios.py  # dict, métodos, casos avanzados
    └── tipos_especiales.py    # None, bytes, bytearray, memoryview
```

## 🚨 Notas Importantes

### Dependencias
- **NumPy**: Requerido solo para ejemplos de arrays (`numpy_arrays_*.py`, `union_arrays_numpy.py`)
- **Tipos básicos**: Todos los ejemplos de tipos de datos usan solo la biblioteca estándar
- Instalación automática disponible via `requirements.txt`

### Características
- 📊 **Output educativo**: Algunos ejemplos generan salida extensa para facilitar el aprendizaje
- 🔍 **Detección automática**: Los runners principales detectan dependencias disponibles
- 🧩 **Modularidad**: Todos los archivos son independientes y ejecutables por separado
- 📱 **Menús interactivos**: Navegación fácil entre diferentes conceptos
- 🎯 **Progresión gradual**: Desde conceptos básicos hasta casos avanzados

### Compatibilidad
- **Python 3.6+**: Todos los ejemplos son compatibles
- **Multiplataforma**: Linux, Windows, macOS
- **Docker**: Configuración incluida para entornos aislados y reproducibles

### Entornos de Desarrollo
- **Local**: Instalación directa con pip
- **Docker**: Entorno containerizado con Python 3.12
- **VS Code**: Configuración de workspace incluida
- **GitHub Codespaces**: Compatible para desarrollo en la nube

## 🤝 Contribuciones

### Cómo Contribuir

#### 🚀 Setup rápido con Docker
```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/python-ejemplos.git
cd python-ejemplos

# 2. Ejecutar con Docker
docker-compose up --build

# 3. Probar cambios
docker-compose run --rm web python main.py
```

#### 🛠️ Setup local
```bash
# 1. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate     # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar ejemplos
python main.py
```

#### ✨ Tipos de contribuciones bienvenidas
- **Nuevos ejemplos**: Agregar casos de uso adicionales
- **Mejoras de documentación**: Clarificar explicaciones
- **Optimizaciones**: Mejorar rendimiento del código
- **Correcciones**: Reportar y corregir errores
- **Nuevos tipos**: Extender a tipos avanzados (collections, etc.)
- **Traduciones**: Documentación en otros idiomas

#### 📋 Proceso de contribución
1. **Fork** del repositorio
2. **Crear rama** para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. **Commit** tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. **Push** a la rama (`git push origin feature/nueva-funcionalidad`)
5. **Crear Pull Request** con descripción detallada

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 📊 Estadísticas del Proyecto

- 📁 **16 archivos totales**: 8 tipos de datos + 5 listas/arrays + 2 ejecutores + 1 web Flask
- 🔧 **100+ funciones de ejemplo**: Cubriendo cada aspecto de los tipos básicos
- 📚 **7 tipos principales**: Numéricos, strings, booleanos, secuencias, conjuntos, diccionarios, especiales  
- � **Componente web**: Ejemplo Flask con Docker configurado
- �🎯 **2 niveles de complejidad**: Básico a intermedio, perfecto para aprendizaje
- 🚀 **Ejecución múltiple**: CLI interactivo + servidor web + Docker

## 🎓 Casos de Uso Educativos

### Para Estudiantes
- Referencia completa de tipos de datos Python
- Ejemplos prácticos para cada concepto
- Progresión estructurada de dificultad
- Output detallado para comprensión visual

### Para Instructores
- Material de clase organizado por temas
- Ejemplos listos para demostración
- Casos de uso del mundo real
- Base para ejercicios y tareas

### Para Desarrolladores
- Referencia rápida de sintaxis y métodos
- Comparaciones de rendimiento entre tipos
- Mejores prácticas y casos edge
- Patrones de uso comunes

## 🐳 Configuración Docker

Este proyecto incluye una configuración completa de Docker para facilitar la ejecución en entornos aislados y garantizar la reproducibilidad.

### 📦 Contenido Docker

#### Dockerfile
- **Imagen base**: Python 3.12 oficial
- **Dependencias**: Instalación automática via requirements.txt
- **Optimización**: Cache de pip deshabilitado para imágenes más ligeras
- **Directorio de trabajo**: `/app`

#### docker-compose.yml
- **Servicio web**: Contenedor principal de la aplicación
- **Volúmenes**: Mapeo del código fuente para desarrollo
- **Variables de entorno**: Configuración para desarrollo
- **Puertos**: Puerto 5000 expuesto (para futuras extensiones web)
- **Modo interactivo**: TTY y STDIN habilitados

### 🚀 Comandos Docker Útiles

#### Gestión de contenedores
```bash
# Ver contenedores activos
docker-compose ps

# Ver logs del contenedor
docker-compose logs

# Parar servicios
docker-compose down

# Reconstruir sin cache
docker-compose build --no-cache

# Limpiar volúmenes
docker-compose down -v
```

#### Desarrollo interactivo
```bash
# Abrir shell en el contenedor
docker-compose run --rm web /bin/bash

# Ejecutar Python interactivo
docker-compose run --rm web python

# Instalar dependencias adicionales
docker-compose run --rm web pip install nueva-dependencia

# Ejecutar servidor Flask en modo desarrollo
docker-compose run --rm -p 5000:5000 web python app.py
```

#### Ejecución de ejemplos específicos
```bash
# Listas básicas
docker-compose run --rm web python code/listas_basicas.py

# Tipos numéricos
docker-compose run --rm web python code/tipos_numericos.py

# Todos los tipos de datos
docker-compose run --rm web python main_tipos_datos.py

# Menú principal de listas/arrays
docker-compose run --rm web python main.py
```

### 🔧 Ventajas del uso de Docker

#### Para Desarrollo
- **Entorno consistente**: Misma versión de Python en todos los sistemas
- **Dependencias aisladas**: No interfiere con otras instalaciones
- **Fácil distribución**: Compartir entorno completo con otros desarrolladores

#### Para Educación
- **Configuración rápida**: Un solo comando para comenzar
- **Sin conflictos**: Ideal para laboratorios y aulas
- **Portabilidad**: Funciona igual en cualquier sistema con Docker

#### Para Producción
- **Reproducibilidad**: Mismo entorno en desarrollo y producción
- **Escalabilidad**: Base para orquestación con Kubernetes
- **Seguridad**: Aislamiento de procesos y recursos

### 🛠️ Personalización Docker

#### Variables de entorno disponibles
```bash
# En docker-compose.yml o al ejecutar
PYTHONUNBUFFERED=1          # Output inmediato
FLASK_ENV=development       # Modo desarrollo (para extensiones futuras)
PYTHONPATH=/app            # Path de Python personalizado
```

#### Modificar configuración
```yaml
# Ejemplo: Cambiar puerto en docker-compose.yml
ports:
  - "8080:5000"  # Puerto host:puerto contenedor

# Ejemplo: Agregar variables de entorno
environment:
  - DEBUG=True
  - LOG_LEVEL=INFO
```

## 🌐 **Componente Web (Flask)**

El proyecto incluye un ejemplo básico de aplicación web con Flask para demostrar la integración de Python en contextos web.

### 🎯 **Características del ejemplo Flask**
- **Servidor web simple** con endpoint de demostración
- **Configuración Docker** optimizada para desarrollo web  
- **Recarga automática** habilitada (`debug=True`)
- **Puerto 5000** expuesto y mapeado en Docker
- **Host 0.0.0.0** para acceso desde fuera del contenedor

### 🚀 **Uso del componente web**

#### Ejecución local
```bash
# El servidor Flask se inicia automáticamente
python app.py

# Acceder en el navegador
# http://localhost:5000
# Verás: "¡Hola desde Flask con recarga automática!"
```

#### Ejecución con Docker
```bash
# Método 1: Docker Compose (recomendado)
docker-compose up
# Servidor automáticamente disponible en http://localhost:5000

# Método 2: Docker tradicional  
docker run -p 5000:5000 python-ejemplos
# Acceder a http://localhost:5000
```

### 💡 **Casos de uso y extensiones posibles**
- **API REST**: Crear endpoints para ejecutar ejemplos específicos
- **Interface web**: Dashboard para explorar ejemplos interactivamente  
- **Servicios web**: Convertir funciones de tipos de datos en servicios
- **Comparación de rendimiento**: Visualización web de benchmarks
- **Educación interactiva**: Formularios web para probar conceptos

### 🔧 **Estructura Flask actual**
```python
# app.py - Servidor básico Flask
@app.route("/")
def home():
    return "¡Hola desde Flask con recarga automática!"
    
# Configuración para desarrollo
app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
```

---

*Creado como material educativo completo para dominar listas, arrays y tipos de datos en Python* 🐍✨