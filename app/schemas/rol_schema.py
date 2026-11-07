from pydantic import BaseModel, Field


class RolBase(BaseModel):
    nombre: str = Field(..., examples=["Administrador"], description="Nombre del rol")


class RolCreate(RolBase):
    pass


class RolResponse(RolBase):
    id_rol: int

    class Config:
        from_attributes = True