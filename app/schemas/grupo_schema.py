from pydantic import BaseModel, Field
from typing import Optional


class GrupoBase(BaseModel):
    id_carrera: int = Field(..., description="ID de la carrera")
    nombre: str = Field(..., examples=["1A"], description="Nombre del grupo")
    cuatrimestre: Optional[int] = Field(None, ge=1, le=12, description="Cuatrimestre (1-12)")
    turno: Optional[str] = Field(None, description="Matutino, Vespertino o Mixto")
    activo: bool = Field(True, description="Si el grupo está activo")


class GrupoCreate(GrupoBase):
    pass


class GrupoResponse(GrupoBase):
    id_grupo: int

    class Config:
        from_attributes = True