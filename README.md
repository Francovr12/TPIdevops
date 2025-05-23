# API - FastAPI + Docker + CI/CD

Una API REST simple para gestionar tareas, desarrollada como parte de un Trabajo Práctico Integrador (TPI) usando FastAPI. El proyecto está dockerizado, testeado y desplegado en la nube.

---

##  Demo online

🔗 https://todo-api-latest.onrender.com  
📄 Swagger: https://todo-api-latest.onrender.com/docs

---

## Tecnologías usadas

- **Python 3.11**
- **FastAPI** como framework web
- **Docker** para contenerización
- **Docker Hub** como registry
- **GitHub Actions** para CI/CD
- **Render** para el deploy
- **Pytest** para testing

---

## Cómo correr el proyecto localmente

### Opción 1: Manual (sin Docker)

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows

# Instalar dependencias
pip install -r requirements.txt

# Correr la app
uvicorn app.main:app --reload
 
