FROM python:3.13.7-alpine

# Instala dependencias del sistema necesarias para mysqlclient (MariaDB)
RUN apk add --no-cache mariadb-dev pkgconfig build-base

# Crea el directorio de trabajo
WORKDIR /app

# Copia e instala dependencias Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Cambia al directorio del proyecto Django
WORKDIR /app/alenkuraWeb

# Expone el puerto 8000 (opcional pero buena práctica)
EXPOSE 8000

# Ejecuta Django en modo accesible desde fuera del contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]