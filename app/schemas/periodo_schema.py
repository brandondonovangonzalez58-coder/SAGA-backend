from pydantic import BaseModel, Field
from datetime import date


class PeriodoBase(BaseModel):
    nombre: str = Field(..., examples=["2026-2027"], description="Nombre del periodo")
    fecha_inicio: date = Field(..., description="Fecha de inicio")
    fecha_fin: date = Field(..., description="Fecha de fin")
    activo: bool = Field(False, description="Si está activo")


class PeriodoCreate(PeriodoBase):
    pass


class PeriodoResponse(PeriodoBase):
    id_periodo: int

    class Config:
        from_attributes = True