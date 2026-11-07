from pydantic import BaseModel, Field
from typing import Optional


class MateriaBase(BaseModel):
    nombre: str = Field(..., examples=["Matemáticas"], description="Nombre de la materia")
    clave: Optional[str] = Field(None, examples=["MAT-101"], description="Clave única")
    activa: bool = Field(True, description="Si la materia está activa")


class MateriaCreate(MateriaBase):
    pass


class MateriaResponse(MateriaBase):
    id_materia: int

    class Config:
        from_attributes = True