from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.routes import (
    auth_router,
    rol_router,
    carrera_router,
    grupo_router,
    estudiante_router,
    materia_router,
    grupo_materia_router,
    sesion_router,
    asistencia_router,
    periodo_router,
    usuario_router,  # <-- NUEVO
    docente_router,  # <-- NUEVO
)



#nuevas modificaciones en la ruta libre de acceso para la api
description = """
SAGA API es el backend del **Sistema de Administración y Gestión Académica**.

## Módulos
* **Autenticación** — login y tokens JWT.
* **Usuarios** — gestión de cuentas de acceso.
* **Docentes** — gestión del personal docente.
* **Roles** — catálogo de roles.
* **Carreras** — catálogo de carreras.
* **Grupos** — grupos por carrera.
* **Estudiantes** — alumnos inscritos.
* **Materias** — catálogo de materias.
* **GrupoMaterias** — asignación de materias a grupos.
* **Sesiones** — clases impartidas.
* **Asistencias** — registro de asistencia.
* **Periodos** — periodos académicos.
"""

tags_metadata = [
    {"name": "Autenticación", "description": "Login y tokens JWT."},
    {"name": "Usuarios", "description": "Gestión de cuentas de acceso."}, # <-- NUEVO
    {"name": "Docentes", "description": "Gestión del personal docente."}, # <-- NUEVO
    {"name": "Roles", "description": "Catálogo de roles."},
    {"name": "Carreras", "description": "Catálogo de carreras."},
    {"name": "Grupos", "description": "Grupos por carrera."},
    {"name": "Estudiantes", "description": "Alumnos inscritos."},
    {"name": "Materias", "description": "Catálogo de materias."},
    {"name": "GrupoMaterias", "description": "Asignación de materias a grupos."},
    {"name": "Sesiones", "description": "Clases impartidas."},
    {"name": "Asistencias", "description": "Registro de asistencia."},
    {"name": "Periodos", "description": "Periodos académicos."},
    {"name": "Root", "description": "Endpoint raíz."},
]

app = FastAPI(
    title="SAGA API",
    description=description,
    summary="API para el Sistema de Administración y Gestión Académica.",
    version="1.0.0",
    contact={
        "name": "Brandon Donovan González Florencio",
        "email": "brandon@saga.com",
    },
    license_info={"name": "Uso académico"},
    openapi_tags=tags_metadata,
)

# ============================================================
# CORS — Configuración abierta para DESARROLLO LOCAL
# ============================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(auth_router)
app.include_router(usuario_router)  # <-- NUEVO
app.include_router(docente_router)  # <-- NUEVO
app.include_router(rol_router)
app.include_router(carrera_router)
app.include_router(grupo_router)
app.include_router(estudiante_router)
app.include_router(materia_router)
app.include_router(grupo_materia_router)
app.include_router(sesion_router)
app.include_router(asistencia_router)
app.include_router(periodo_router)


@app.get("/", tags=["Root"], summary="Verificar estado de la API")
def raiz():
    return {"mensaje": "SAGA API funcionando correctamente"}


if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)