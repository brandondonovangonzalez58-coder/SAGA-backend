from pydantic import BaseModel, Field
from typing import Optional


class CarreraBase(BaseModel):
    nombre: str = Field(..., examples=["Ingeniería en Sistemas"], description="Nombre de la carrera")
    siglas: Optional[str] = Field(None, examples=["IS"], description="Siglas de la carrera")
    activa: bool = Field(True, description="Si la carrera está activa")


class CarreraCreate(CarreraBase):
    pass


class CarreraResponse(CarreraBase):
    id_carrera: int

    class Config:
        from_attributes = True