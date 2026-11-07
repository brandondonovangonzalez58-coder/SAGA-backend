from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, time

class SesionBase(BaseModel):
    id_grupo_materia: int
    fecha: date
    hora_inicio: Optional[time] = None
    hora_fin: Optional[time] = None
    tema: Optional[str] = None
    estado: str = "Abierta"

class SesionCreate(SesionBase):
    pass

class SesionResponse(SesionBase):
    id_sesion: int

    class Config:
        from_attributes = True