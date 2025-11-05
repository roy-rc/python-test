#!/usr/bin/env python3
"""
Ejemplos completos de tipos especiales en Python
- NoneType (None)
- bytes (secuencias inmutables de bytes)
- bytearray (secuencias mutables de bytes)
- memoryview (vistas de memoria)
- Operadores y métodos específicos
"""

def ejemplos_none():
    """Ejemplos del tipo None"""
    print("=" * 60)
    print("NONETYPE - TIPO None")
    print("=" * 60)
    
    # None es un singleton
    print("--- CARACTERÍSTICAS DE None ---")
    
    valor_none = None
    otro_none = None
    
    print(f"valor_none: {valor_none}")
    print(f"type(None): {type(None)}")
    print(f"None is None: {None is None}")
    print(f"valor_none is otro_none: {valor_none is otro_none}")
    print(f"valor_none == otro_none: {valor_none == otro_none}")
    print(f"id(None): {id(None)}")
    print(f"id(valor_none): {id(valor_none)}")
    print("None es un singleton - solo existe una instancia")
    print()
    
    # Casos de uso comunes
    print("--- CASOS DE USO DE None ---")
    
    # Valor por defecto de función
    def saludar(nombre=None):
        if nombre is None:
            return "Hola, desconocido!"
        return f"Hola, {nombre}!"
    
    print(f"saludar(): '{saludar()}'")
    print(f"saludar('Ana'): '{saludar('Ana')}'")
    
    # Variable no inicializada
    resultado = None
    if True:  # alguna condición
        resultado = "valor calculado"
    
    if resultado is not None:
        print(f"Resultado: {resultado}")
    
    # Retorno implícito de función
    def funcion_sin_return():
        x = 1 + 1  # No hay return explícito
    
    retorno = funcion_sin_return()
    print(f"Función sin return retorna: {retorno}")
    print()
    
    # Comparaciones con None
    print("--- COMPARACIONES CON None ---")
    
    valores = [None, 0, False, "", [], {}, set()]
    
    print("Comparación con None:")
    for valor in valores:
        es_none_is = valor is None
        es_none_eq = valor == None  # No recomendado
        es_truthiness = bool(valor)
        
        print(f"  {repr(valor):10} is None: {es_none_is:5} == None: {es_none_eq:5} bool(): {es_truthiness}")
    
    print("\nRecomendación: Usar 'is None' en lugar de '== None'")
    print()
    
    # None en estructuras de datos
    print("--- None EN ESTRUCTURAS DE DATOS ---")
    
    # Lista con None
    lista_con_none = [1, None, 3, None, 5]
    print(f"Lista: {lista_con_none}")
    print(f"Filtrar None: {[x for x in lista_con_none if x is not None]}")
    
    # Diccionario con None
    config = {
        "host": "localhost",
        "port": 8080,
        "password": None,  # Aún no configurado
        "debug": True
    }
    
    print(f"Config: {config}")
    # Filtrar claves con valor None
    config_valido = {k: v for k, v in config.items() if v is not None}
    print(f"Config sin None: {config_valido}")
    print()


def ejemplos_bytes():
    """Ejemplos del tipo bytes"""
    print("=" * 60)
    print("BYTES - SECUENCIAS INMUTABLES DE BYTES")
    print("=" * 60)
    
    # Creación de bytes
    print("--- CREACIÓN DE BYTES ---")
    
    # Bytes literal
    bytes_literal = b"Hola mundo"
    bytes_vacio = b""
    
    # Constructor bytes()
    bytes_desde_lista = bytes([72, 111, 108, 97])  # "Hola" en ASCII
    bytes_desde_string = "Hola".encode('utf-8')
    bytes_ceros = bytes(10)  # 10 bytes en cero
    
    # Bytes con escape
    bytes_escape = b"L\xednea 1\nL\xednea 2"
    
    print(f"Literal: {bytes_literal}")
    print(f"Vacío: {bytes_vacio}")
    print(f"Desde lista: {bytes_desde_lista}")
    print(f"Desde string: {bytes_desde_string}")
    print(f"Ceros (10): {bytes_ceros}")
    print(f"Con escape: {bytes_escape}")
    print(f"Tipo: {type(bytes_literal)}")
    print()
    
    # Propiedades de bytes
    print("--- PROPIEDADES ---")
    
    datos = b"Python"
    print(f"Datos: {datos}")
    print(f"Longitud: {len(datos)}")
    print(f"Primer byte: {datos[0]} (carácter: {chr(datos[0])})")
    print(f"Último byte: {datos[-1]} (carácter: {chr(datos[-1])})")
    print(f"Slice [1:4]: {datos[1:4]}")
    
    # Bytes son inmutables
    print("\nBytes son inmutables:")
    try:
        datos[0] = 65  # Error
    except TypeError as e:
        print(f"Error al modificar: {e}")
    print()
    
    # Operadores con bytes
    print("--- OPERADORES CON BYTES ---")
    
    parte1 = b"Hola"
    parte2 = b" mundo"
    
    # Concatenación
    completo = parte1 + parte2
    print(f"Concatenación: {parte1} + {parte2} = {completo}")
    
    # Repetición
    repetido = parte1 * 3
    print(f"Repetición: {parte1} * 3 = {repetido}")
    
    # Pertenencia (busca bytes individuales)
    print(f"65 in b'ABC': {65 in b'ABC'}")  # 65 = 'A'
    print(f"b'ol' in b'Hola': {b'ol' in b'Hola'}")
    
    # Comparación
    print(f"b'abc' == b'abc': {b'abc' == b'abc'}")
    print(f"b'abc' < b'abd': {b'abc' < b'abd'}")
    print()
    
    # Métodos de bytes
    print("--- MÉTODOS DE BYTES ---")
    
    texto_bytes = b"Python Programming"
    print(f"Texto: {texto_bytes}")
    
    # Métodos similares a strings
    print(f"upper(): {texto_bytes.upper()}")
    print(f"lower(): {texto_bytes.lower()}")
    print(f"split(): {texto_bytes.split()}")
    print(f"replace(b'Python', b'Java'): {texto_bytes.replace(b'Python', b'Java')}")
    print(f"startswith(b'Py'): {texto_bytes.startswith(b'Py')}")
    print(f"find(b'Pro'): {texto_bytes.find(b'Pro')}")
    
    # Decodificación
    print(f"decode('utf-8'): '{texto_bytes.decode('utf-8')}'")
    print()


def ejemplos_bytearray():
    """Ejemplos del tipo bytearray (bytes mutables)"""
    print("=" * 60)
    print("BYTEARRAY - SECUENCIAS MUTABLES DE BYTES")
    print("=" * 60)
    
    # Creación de bytearray
    print("--- CREACIÓN DE BYTEARRAY ---")
    
    # Desde bytes
    ba_desde_bytes = bytearray(b"Hola")
    
    # Desde string
    ba_desde_string = bytearray("Hola", 'utf-8')
    
    # Desde lista de enteros
    ba_desde_lista = bytearray([72, 111, 108, 97])  # "Hola"
    
    # Bytearray vacío
    ba_vacio = bytearray()
    
    # Bytearray con tamaño
    ba_ceros = bytearray(5)  # 5 bytes en cero
    
    print(f"Desde bytes: {ba_desde_bytes}")
    print(f"Desde string: {ba_desde_string}")
    print(f"Desde lista: {ba_desde_lista}")
    print(f"Vacío: {ba_vacio}")
    print(f"Ceros (5): {ba_ceros}")
    print(f"Tipo: {type(ba_desde_bytes)}")
    print()
    
    # Mutabilidad
    print("--- MUTABILIDAD ---")
    
    datos = bytearray(b"Python")
    print(f"Original: {datos}")
    
    # Modificar elementos individuales
    datos[0] = 74  # 'J'
    print(f"Después de datos[0] = 74: {datos}")
    
    # Modificar slice
    datos[1:3] = b"av"
    print(f"Después de datos[1:3] = b'av': {datos}")
    
    # Métodos de modificación
    print(f"Antes de append(33): {datos}")  # 33 = '!'
    datos.append(33)
    print(f"Después de append(33): {datos}")
    
    datos.extend(b" rocks")
    print(f"Después de extend(b' rocks'): {datos}")
    
    # Insertar
    datos.insert(0, 42)  # '*'
    print(f"Después de insert(0, 42): {datos}")
    
    # Eliminar
    eliminado = datos.pop()
    print(f"pop() eliminó: {eliminado} ({chr(eliminado)}), resultado: {datos}")
    
    datos.remove(42)  # Eliminar primer '*'
    print(f"Después de remove(42): {datos}")
    print()
    
    # Métodos adicionales de bytearray
    print("--- MÉTODOS ADICIONALES ---")
    
    buffer = bytearray(b"abcdefghijk")
    print(f"Buffer original: {buffer}")
    
    # reverse()
    buffer.reverse()
    print(f"Después de reverse(): {buffer}")
    
    # clear()
    buffer_copia = buffer.copy()
    buffer.clear()
    print(f"Después de clear(): {buffer}")
    print(f"Copia guardada: {buffer_copia}")
    print()


def ejemplos_memoryview():
    """Ejemplos del tipo memoryview"""
    print("=" * 60)
    print("MEMORYVIEW - VISTAS DE MEMORIA")
    print("=" * 60)
    
    print("--- QUÉ ES MEMORYVIEW ---")
    print("memoryview permite acceder a la memoria interna de objetos")
    print("sin copiar los datos - útil para eficiencia de memoria")
    print()
    
    # Crear memoryview desde bytearray
    print("--- MEMORYVIEW DESDE BYTEARRAY ---")
    
    datos_originales = bytearray(b"Python Programming")
    vista = memoryview(datos_originales)
    
    print(f"Datos originales: {datos_originales}")
    print(f"Vista completa: {vista.tobytes()}")
    print(f"Tipo vista: {type(vista)}")
    
    # Propiedades de memoryview
    print(f"Longitud: {len(vista)}")
    print(f"Formato: {vista.format}")
    print(f"Item size: {vista.itemsize}")
    print(f"Readonly: {vista.readonly}")
    print()
    
    # Slicing de memoryview
    print("--- SLICING DE MEMORYVIEW ---")
    
    # Vista parcial
    vista_parcial = vista[7:18]  # "Programming"
    print(f"Vista parcial [7:18]: {vista_parcial.tobytes()}")
    
    # Modificar a través de la vista
    print(f"Antes de modificar: {datos_originales}")
    vista_parcial[0] = 112  # 'p' minúscula
    print(f"Después de modificar vista: {datos_originales}")
    print("Los cambios en la vista afectan los datos originales")
    print()
    
    # Memoryview desde bytes (readonly)
    print("--- MEMORYVIEW DESDE BYTES (READONLY) ---")
    
    bytes_datos = b"Inmutable"
    vista_readonly = memoryview(bytes_datos)
    
    print(f"Bytes datos: {bytes_datos}")
    print(f"Vista readonly: {vista_readonly.tobytes()}")
    print(f"Es readonly: {vista_readonly.readonly}")
    
    try:
        vista_readonly[0] = 65  # Error - es readonly
    except TypeError as e:
        print(f"Error al modificar vista readonly: {e}")
    print()
    
    # Casos de uso prácticos
    print("--- CASOS DE USO PRÁCTICOS ---")
    
    # Procesar datos grandes sin copiar
    def procesar_chunk(vista_memoria):
        """Procesa un chunk de datos sin copiarlo"""
        suma = sum(vista_memoria)
        return suma
    
    datos_grandes = bytearray(range(256))  # 0-255
    
    # Procesar en chunks
    chunk_size = 64
    resultados = []
    
    for i in range(0, len(datos_grandes), chunk_size):
        chunk_vista = memoryview(datos_grandes[i:i+chunk_size])
        resultado = procesar_chunk(chunk_vista)
        resultados.append(resultado)
    
    print(f"Datos grandes: {len(datos_grandes)} bytes")
    print(f"Procesado en chunks de {chunk_size}: {resultados}")
    print(f"Suma total: {sum(resultados)}")
    print()


def conversion_entre_tipos():
    """Conversiones entre tipos de bytes"""
    print("=" * 60)
    print("CONVERSIONES ENTRE TIPOS")
    print("=" * 60)
    
    # Datos de ejemplo
    texto_original = "Hola mundo! 🌍"
    
    print("--- CADENA DE CONVERSIONES ---")
    print(f"Texto original: '{texto_original}'")
    
    # str -> bytes
    bytes_utf8 = texto_original.encode('utf-8')
    print(f"1. str -> bytes (UTF-8): {bytes_utf8}")
    
    # bytes -> bytearray
    bytearray_datos = bytearray(bytes_utf8)
    print(f"2. bytes -> bytearray: {bytearray_datos}")
    
    # bytearray -> memoryview
    vista_memoria = memoryview(bytearray_datos)
    print(f"3. bytearray -> memoryview: {vista_memoria.tobytes()}")
    
    # Modificar bytearray a través de memoryview
    vista_memoria[0] = 104  # 'H' -> 'h'
    print(f"4. Modificar via memoryview: {bytearray_datos}")
    
    # bytearray -> bytes
    bytes_final = bytes(bytearray_datos)
    print(f"5. bytearray -> bytes: {bytes_final}")
    
    # bytes -> str
    texto_final = bytes_final.decode('utf-8')
    print(f"6. bytes -> str: '{texto_final}'")
    print()
    
    # Diferentes encodings
    print("--- DIFERENTES ENCODINGS ---")
    
    texto = "Café résumé naïve"
    encodings = ['utf-8', 'latin-1', 'ascii']
    
    for encoding in encodings:
        try:
            encoded = texto.encode(encoding)
            decoded = encoded.decode(encoding)
            print(f"{encoding:10}: {encoded} -> '{decoded}'")
        except UnicodeEncodeError as e:
            print(f"{encoding:10}: Error de codificación: {e}")
        except UnicodeDecodeError as e:
            print(f"{encoding:10}: Error de decodificación: {e}")
    print()
    
    # Hexadecimal representation
    print("--- REPRESENTACIÓN HEXADECIMAL ---")
    
    datos = b"Python"
    print(f"Datos: {datos}")
    
    # Convertir a hex
    hex_string = datos.hex()
    print(f"Hexadecimal: {hex_string}")
    
    # Hex con separador
    hex_separado = datos.hex(' ')
    print(f"Hex separado: {hex_separado}")
    
    # Desde hex de vuelta a bytes
    desde_hex = bytes.fromhex(hex_string)
    print(f"Desde hex: {desde_hex}")
    
    # Representación individual
    print("Bytes individuales:")
    for i, byte_val in enumerate(datos):
        print(f"  [{i}]: {byte_val:3d} = 0x{byte_val:02x} = '{chr(byte_val)}'")
    print()


def casos_uso_practicos_bytes():
    """Casos de uso prácticos con tipos de bytes"""
    print("=" * 60)
    print("CASOS DE USO PRÁCTICOS")
    print("=" * 60)
    
    # Lectura/escritura de archivos binarios
    print("--- SIMULACIÓN DE ARCHIVO BINARIO ---")
    
    # Simular contenido de archivo binario
    datos_archivo = bytearray()
    
    # Header (4 bytes)
    datos_archivo.extend(b"PYTH")
    
    # Versión (2 bytes)
    version = 1
    datos_archivo.extend(version.to_bytes(2, 'little'))
    
    # Cantidad de strings (4 bytes)
    cantidad = 3
    datos_archivo.extend(cantidad.to_bytes(4, 'little'))
    
    # Strings con longitud
    strings = ["Hola", "Mundo", "Python"]
    for s in strings:
        s_bytes = s.encode('utf-8')
        # Longitud del string (1 byte)
        datos_archivo.append(len(s_bytes))
        # Contenido del string
        datos_archivo.extend(s_bytes)
    
    print(f"Datos del archivo: {datos_archivo}")
    print(f"Tamaño total: {len(datos_archivo)} bytes")
    
    # Leer el archivo simulado
    print("\nLeyendo archivo:")
    vista = memoryview(datos_archivo)
    offset = 0
    
    # Leer header
    header = vista[offset:offset+4].tobytes()
    offset += 4
    print(f"Header: {header}")
    
    # Leer versión
    version_bytes = vista[offset:offset+2].tobytes()
    version = int.from_bytes(version_bytes, 'little')
    offset += 2
    print(f"Versión: {version}")
    
    # Leer cantidad
    cantidad_bytes = vista[offset:offset+4].tobytes()
    cantidad = int.from_bytes(cantidad_bytes, 'little')
    offset += 4
    print(f"Cantidad de strings: {cantidad}")
    
    # Leer strings
    for i in range(cantidad):
        # Leer longitud
        longitud = vista[offset]
        offset += 1
        
        # Leer contenido
        contenido = vista[offset:offset+longitud].tobytes().decode('utf-8')
        offset += longitud
        
        print(f"String {i+1}: '{contenido}' ({longitud} bytes)")
    print()
    
    # Protocolo de comunicación simple
    print("--- PROTOCOLO DE COMUNICACIÓN ---")
    
    def crear_mensaje(tipo_msg, datos):
        """Crear mensaje con formato: [tipo][longitud][datos]"""
        mensaje = bytearray()
        
        # Tipo de mensaje (1 byte)
        mensaje.append(tipo_msg)
        
        # Datos como bytes
        if isinstance(datos, str):
            datos_bytes = datos.encode('utf-8')
        else:
            datos_bytes = datos
        
        # Longitud de datos (2 bytes, little endian)
        mensaje.extend(len(datos_bytes).to_bytes(2, 'little'))
        
        # Datos
        mensaje.extend(datos_bytes)
        
        return bytes(mensaje)
    
    def parsear_mensaje(mensaje):
        """Parsear mensaje recibido"""
        if len(mensaje) < 3:
            return None
        
        tipo = mensaje[0]
        longitud = int.from_bytes(mensaje[1:3], 'little')
        
        if len(mensaje) < 3 + longitud:
            return None  # Mensaje incompleto
        
        datos = mensaje[3:3+longitud]
        
        return {
            'tipo': tipo,
            'longitud': longitud,
            'datos': datos
        }
    
    # Tipos de mensaje
    MSG_TEXTO = 1
    MSG_NUMERO = 2
    MSG_BINARIO = 3
    
    # Crear mensajes
    msg1 = crear_mensaje(MSG_TEXTO, "Hola servidor")
    msg2 = crear_mensaje(MSG_NUMERO, str(42))
    msg3 = crear_mensaje(MSG_BINARIO, bytes([0xFF, 0x00, 0xAA]))
    
    mensajes = [msg1, msg2, msg3]
    nombres = ["Texto", "Número", "Binario"]
    
    for msg, nombre in zip(mensajes, nombres):
        print(f"Mensaje {nombre}: {msg}")
        parsed = parsear_mensaje(msg)
        print(f"  Parseado: {parsed}")
        
        if parsed['tipo'] == MSG_TEXTO:
            print(f"  Contenido: '{parsed['datos'].decode('utf-8')}'")
        elif parsed['tipo'] == MSG_NUMERO:
            print(f"  Número: {int(parsed['datos'].decode('utf-8'))}")
        elif parsed['tipo'] == MSG_BINARIO:
            print(f"  Binario: {list(parsed['datos'])}")
        print()


if __name__ == "__main__":
    ejemplos_none()
    ejemplos_bytes()
    ejemplos_bytearray()
    ejemplos_memoryview()
    conversion_entre_tipos()
    casos_uso_practicos_bytes()