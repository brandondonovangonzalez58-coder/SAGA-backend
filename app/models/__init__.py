from app.models.rol import Rol
from app.models.usuario import Usuario
from app.models.carrera import Carrera
from app.models.grupo import Grupo
from app.models.estudiante import Estudiante
from app.models.materia import Materia
from app.models.grupo_materia import GrupoMateria
from app.models.sesion import Sesion
from app.models.asistencia import Asistencia
from app.models.periodo import Periodo
from app.models.docente import Docente  # <-- ESTA ES LA LÍNEA QUE FALTA

__all__ = [
    "Rol",
    "Usuario",
    "Carrera",
    "Grupo",
    "Estudiante",
    "Materia",
    "GrupoMateria",
    "Sesion",
    "Asistencia",
    "Periodo",
    "Docente", # <-- AGREGARLO AQUÍ TAMBIÉN
]