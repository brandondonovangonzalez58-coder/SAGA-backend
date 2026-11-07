from pydantic import BaseModel
from typing import Optional
from datetime import date
from app.schemas.usuario_schema import UsuarioResponse

class GrupoSimple(BaseModel):
    id_grupo: int
    nombre: str
    turno: Optional[str] = None

    class Config:
        from_attributes = True

class EstudianteBase(BaseModel):
    id_usuario: int
    id_grupo: int
    fecha_ingreso: Optional[date] = None

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteResponse(EstudianteBase):
    id_estudiante: int
    usuario: Optional[UsuarioResponse] = None
    grupo: Optional[GrupoSimple] = None

    class Config:
        from_attributes = True