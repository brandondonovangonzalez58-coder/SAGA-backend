from pydantic import BaseModel, EmailStr, Field
from app.schemas.usuario_schema import UsuarioResponse


class LoginRequest(BaseModel):
    correo: EmailStr = Field(
        ...,
        examples=["admin@saga.com"],
        description="Correo registrado del usuario"
    )
    password: str = Field(
        ...,
        examples=["admin123"],
        description="Contraseña del usuario"
    )


class TokenResponse(BaseModel):
    access_token: str = Field(..., description="Token JWT")
    token_type: str = Field("bearer", description="Tipo de token")
    usuario: UsuarioResponse

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "access_token": "eyJhbGciOiJIUzI1...",
                    "token_type": "bearer",
                    "usuario": {
                        "id_usuario": 1,
                        "nombre": "Admin",
                        "apellidos": "SAGA",
                        "correo": "admin@saga.com",
                        "matricula": None,
                        "id_rol": 1,
                        "rol": "Administrador"
                    }
                }
            ]
        }
    }