from pydantic import BaseModel, Field


class GrupoMateriaBase(BaseModel):
    id_grupo: int = Field(..., description="ID del grupo")
    id_materia: int = Field(..., description="ID de la materia")
    id_docente: int = Field(..., description="ID del docente")
    periodo: str = Field(..., examples=["2026-2027"], description="Periodo escolar")
    activa: bool = Field(True, description="Si está activa")


class GrupoMateriaCreate(GrupoMateriaBase):
    pass


class GrupoMateriaResponse(GrupoMateriaBase):
    id_grupo_materia: int

    class Config:
        from_attributes = True