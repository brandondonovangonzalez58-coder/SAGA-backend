from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# 1. Esquema para crear un usuario
class UsuarioCreate(BaseModel):
    id_rol: int = Field(..., description="ID del rol (1=Admin, 2=Docente, 3=Estudiante)")
    nombre: str = Field(..., description="Nombre(s) del usuario")
    apellidos: str = Field(..., description="Apellidos del usuario")
    correo: EmailStr = Field(..., description="Correo electrónico único")
    password: str = Field(..., description="Contraseña en texto plano (el backend la encripta)")
    matricula: Optional[str] = Field(None, description="Matrícula (solo alumnos)")
    activo: bool = Field(True, description="Estado de la cuenta")

# 2. Esquema para actualizar (todos los campos son opcionales)
class UsuarioUpdate(BaseModel):
    id_rol: Optional[int] = None
    nombre: Optional[str] = None
    apellidos: Optional[str] = None
    correo: Optional[EmailStr] = None
    password: Optional[str] = None
    matricula: Optional[str] = None
    activo: Optional[bool] = None

# 3. Esquema de respuesta (NUNCA devuelve el hash de la contraseña)
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