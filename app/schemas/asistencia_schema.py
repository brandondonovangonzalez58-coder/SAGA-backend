from pydantic import BaseModel, Field
from typing import Optional


class AsistenciaBase(BaseModel):
    id_sesion: int = Field(..., description="ID de la sesión")
    id_estudiante: int = Field(..., description="ID del estudiante")
    estado: str = Field(..., description="Presente, Retardo, Falta o Justificada")
    observaciones: Optional[str] = Field(None, description="Comentarios")
    registrado_por: int = Field(..., description="ID del usuario que registra")


class AsistenciaCreate(AsistenciaBase):
    pass


class AsistenciaResponse(AsistenciaBase):
    id_asistencia: int

    class Config:
        from_attributes = True