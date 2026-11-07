from app.routes.auth_router import router as auth_router
from app.routes.usuario_router import router as usuario_router     # <-- NUEVO
from app.routes.docente_router import router as docente_router     # <-- NUEVO
from app.routes.rol_router import router as rol_router
from app.routes.carrera_router import router as carrera_router
from app.routes.grupo_router import router as grupo_router
from app.routes.estudiante_router import router as estudiante_router
from app.routes.materia_router import router as materia_router
from app.routes.grupo_materia_router import router as grupo_materia_router
from app.routes.sesion_router import router as sesion_router
from app.routes.asistencia_router import router as asistencia_router
from app.routes.periodo_router import router as periodo_router

__all__ = [
    "auth_router",
    "usuario_router",  # <-- NUEVO
    "docente_router",  # <-- NUEVO
    "rol_router",
    "carrera_router",
    "grupo_router",
    "estudiante_router",
    "materia_router",
    "grupo_materia_router",
    "sesion_router",
    "asistencia_router",
    "periodo_router",
]