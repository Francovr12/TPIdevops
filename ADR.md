
---
````
#  Documento de Decisiones Técnicas (ADR)

##  Elección de tecnologías

###  FastAPI
Elegimos FastAPI por ser liviano, rápido y permitir definir rutas con tipado fuerte. Su documentación integrada (`/docs`) facilita el testing manual. Ideal para APIs REST.

###  Docker
Usamos Docker para contenerizar el proyecto, facilitando la portabilidad. Una vez dockerizado, la app puede correr igual en cualquier máquina o servicio cloud.

###  GitHub Actions
Configuramos un workflow CI con GitHub Actions. Automatiza los tests en cada push a `main`, asegurando que el código se mantenga estable sin intervención manual.

###  Render
Elegimos Render por su simplicidad para desplegar servicios web a partir de imágenes Docker. Permite un flujo moderno y directo desde Docker Hub. Alternativas como Heroku o Railway quedaron descartadas por menor soporte directo a imágenes externas o menor estabilidad.

###  Almacenamiento en memoria
La API guarda tareas en una lista en memoria para simplificar el desarrollo inicial. Para producción, se puede reemplazar por una base de datos como SQLite o PostgreSQL. Justificamos esta decisión para enfocarnos en los flujos de despliegue y CI/CD.

---

##  Alternativas consideradas

- Base de datos: se dejó como mejora futura para mantener simple el MVP del TPI.
## Monitoreo

- Render tiene logs integrados.
- Se puede agregar [UptimeRobot](https://uptimerobot.com) o [BetterStack](https://betterstack.com) para uptime y alertas.

---
