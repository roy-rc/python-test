# Imagen base de Python
FROM python:3.12

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copia dependencias e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos
COPY . .

# Comando por defecto al iniciar el contenedor
CMD ["python", "app.py"]

