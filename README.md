# Flask API Core Backend 🚀

Una arquitectura base modular construida con **Flask**, implementando el patrón de diseño **Repository-Service**, validación de datos estricta con **Pydantic** y almacenamiento de archivos en la nube utilizando **AWS S3**.

Ideal para proyectos que requieren una separación de responsabilidades clara, manejo global de errores y tipado seguro.

## ✨ Características Principales

* 🏗️ **Arquitectura en Capas:** Separación limpia mediante Controladores (Blueprints), Servicios, Repositorios y Modelos.
* 🛡️ **Validación de Datos Sólida:** Integración de **Pydantic v2** para la sanitización, tipado y validación estricta de payloads (evitando campos basura en mutaciones).
* ☁️ **Gestión de Archivos en la Nube:** Repositorio optimizado para interactuar con **AWS S3** usando `boto3` (Subida, listado y control de extensiones).
* 🛢️ **ORM y Migraciones:** Configurado con **Flask-SQLAlchemy** y **Flask-Migrate** mediante el patrón de *Application Factory*.

## 📁 Estructura del Proyecto

```text
app/
├── core/                  # Configuraciones centrales (Excepciones, Handlers)
│   ├── error_handler.py
│   └── exceptions.py
├── models/                # Modelos de la Base de Datos (SQLAlchemy)
│   └── user_model.py
├── schemas/               # Esquemática y validación de datos (Pydantic)
│   └── user_schema.py
├── repositories/          # Abstracción de acceso a datos (DB, S3, APIs externas)
│   ├── user_repository.py
│   └── s3_repository.py
├── services/              # Lógica de negocio core de la aplicación
│   ├── user_service.py
│   └── file_service.py
├── routes/                # Controladores / Endpoints (Blueprints)
│   ├── user_routes.py
│   └── file_routes.py
├── config.py              # Variables de entorno y configuraciones de Flask
├── extensions.py          # Inicialización de extensiones (DB, Migrate, S3 Client)
└── __init__.py            # Application Factory (create_app)
```

## 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

## 2. Crear y activar el entorno virtual

```bash
python -m venv venv

# En Windows:
.\venv\Scripts\activate

# En Linux/macOS:
source venv/bin/activate
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```
## 4. Ejecutar Migraciones

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## 5. Iniciar el servidor de desarrollo

```bash
flask run --reload
```


