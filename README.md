#  API - FastAPI + Docker + CI/CD

Una API REST simple para gestionar tareas, desarrollada como parte de un Trabajo Práctico Integrador (TPI) usando FastAPI. El proyecto está dockerizado, testeado y desplegado en la nube.

---

## Demo online

🔗 https://todo-api-latest.onrender.com  
📄 Swagger: https://todo-api-latest.onrender.com/docs

---

##  Tecnologías usadas

- **Python 3.11**
- **FastAPI** como framework web
- **Docker** para contenerización
- **Docker Hub** como registry
- **GitHub Actions** para CI/CD
- **Render** para el deploy
- **Pytest** para testing

---
````
## Cómo correr el proyecto localmente

### Opción 1: Manual (sin Docker)


# Crear entorno virtual


python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows

# Instalar dependencias

pip install -r requirements.txt

# Correr la app

uvicorn app.main:app --reload

Opción 2: Usando Docker

docker build -t todo-api .
docker run -p 8000:8000 todo-api

   Cómo correr los tests
# Establecer PYTHONPATH (si hace falta)
export PYTHONPATH=.

# Ejecutar tests
pytest
   Para desarrollo
Código fuente: carpeta app/

Tests: carpeta tests/

Rutas disponibles: /tasks, /tasks/{id}, /docs

  CI/CD
Cada push/pull request a main ejecuta automáticamente:

Instalación de dependencias

Ejecución de tests con pytest

Verificación del build

   Deploy
Se usa Render para el despliegue.

El contenedor se crea a partir de una imagen Docker publicada en Docker Hub.

Comando de arranque: uvicorn app.main:app --host 0.0.0.0 --port 8000

    Monitoreo
Render tiene logs integrados.

Se puede agregar UptimeRobot o BetterStack para uptime y alertas.


 
