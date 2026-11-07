from pydantic import BaseModel
from typing import Optional
from datetime import date
from app.schemas.usuario_schema import UsuarioResponse

class EstudianteBase(BaseModel):
    id_usuario: int
    id_grupo: int
    fecha_ingreso: Optional[date] = None

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteResponse(EstudianteBase):
    id_estudiante: int
    usuario: Optional[UsuarioResponse] = None

    class Config:
        from_attributes = True