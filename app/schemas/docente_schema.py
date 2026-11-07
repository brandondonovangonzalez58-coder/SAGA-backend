from pydantic import BaseModel, Field
from typing import Optional

class DocenteBase(BaseModel):
    id_usuario: int = Field(..., description="ID del usuario asociado")
    numero_empleado: str = Field(..., description="Número de empleado único")
    especialidad: Optional[str] = Field(None, description="Especialidad del docente")

class DocenteCreate(DocenteBase):
    pass

class DocenteResponse(DocenteBase):
    id_docente: int

    class Config:
        from_attributes = True