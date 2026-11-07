from pydantic import BaseModel, Field
from typing import Optional
from app.schemas.usuario_schema import UsuarioResponse # <-- Importante

class DocenteBase(BaseModel):
    id_usuario: int = Field(..., description="ID del usuario asociado")
    numero_empleado: str = Field(..., description="Número de empleado único")
    especialidad: Optional[str] = Field(None, description="Especialidad del docente")

class DocenteCreate(DocenteBase):
    pass

class DocenteResponse(DocenteBase):
    id_docente: int
    usuario: Optional[UsuarioResponse] = None # <-- ESTA ES LA LÍNEA QUE FALTA

    class Config:
        from_attributes = True