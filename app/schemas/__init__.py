from app.schemas.auth_schema import LoginRequest, TokenResponse
# Agregamos UsuarioCreate y UsuarioUpdate aquí:
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.schemas.rol_schema import RolCreate, RolResponse
from app.schemas.carrera_schema import CarreraCreate, CarreraResponse
from app.schemas.grupo_schema import GrupoCreate, GrupoResponse
from app.schemas.estudiante_schema import EstudianteCreate, EstudianteResponse
from app.schemas.materia_schema import MateriaCreate, MateriaResponse
from app.schemas.grupo_materia_schema import GrupoMateriaCreate, GrupoMateriaResponse
from app.schemas.sesion_schema import SesionCreate, SesionResponse
from app.schemas.asistencia_schema import AsistenciaCreate, AsistenciaResponse
from app.schemas.periodo_schema import PeriodoCreate, PeriodoResponse

__all__ = [
    "LoginRequest", "TokenResponse", 
    "UsuarioCreate", "UsuarioUpdate", "UsuarioResponse", # <-- Los agregamos a la lista
    "RolCreate", "RolResponse",
    "CarreraCreate", "CarreraResponse",
    "GrupoCreate", "GrupoResponse",
    "EstudianteCreate", "EstudianteResponse",
    "MateriaCreate", "MateriaResponse",
    "GrupoMateriaCreate", "GrupoMateriaResponse",
    "SesionCreate", "SesionResponse",
    "AsistenciaCreate", "AsistenciaResponse",
    "PeriodoCreate", "PeriodoResponse",
]