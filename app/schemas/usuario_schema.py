from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioCreate(BaseModel):
    id_rol: int
    nombre: str
    apellidos: str
    correo: EmailStr
    password: str
    matricula: Optional[str] = None
    activo: bool = True

class UsuarioUpdate(BaseModel):
    id_rol: Optional[int] = None
    nombre: Optional[str] = None
    apellidos: Optional[str] = None
    correo: Optional[EmailStr] = None
    password: Optional[str] = None
    matricula: Optional[str] = None
    activo: Optional[bool] = None

class UsuarioResponse(BaseModel):
    id_usuario: int
    id_rol: int
    nombre: str
    apellidos: str
    correo: EmailStr
    matricula: Optional[str] = None
    activo: bool
    rol: Optional[str] = None

    class Config:
        from_attributes = True