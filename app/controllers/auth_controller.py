from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import Usuario
from app.schemas import LoginRequest, TokenResponse, UsuarioResponse
from app.utils.security import verify_password, crear_token

class AuthController:

    @staticmethod
    def login(datos: LoginRequest, db: Session) -> TokenResponse:
        usuario = db.query(Usuario).filter(Usuario.correo == datos.correo).first()

        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Correo o contraseña incorrectos"
            )

        if not usuario.activo:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuario inactivo, contacta al administrador"
            )

        if not verify_password(datos.password, usuario.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Correo o contraseña incorrectos"
            )

        token = crear_token({
            "sub": str(usuario.id_usuario),
            "correo": usuario.correo,
            "rol": usuario.rol.nombre
        })

        return TokenResponse(
            access_token=token,
            usuario=UsuarioResponse(
                id_usuario=usuario.id_usuario,
                nombre=usuario.nombre,
                apellidos=usuario.apellidos,
                correo=usuario.correo,
                matricula=usuario.matricula,
                id_rol=usuario.id_rol,
                rol=usuario.rol.nombre,
                activo=usuario.activo  # <-- ESTA ES LA LÍNEA QUE FALTABA
            )
        )