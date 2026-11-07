from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import LoginRequest, TokenResponse
from app.controllers.auth_controller import AuthController

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"],
    responses={
        401: {"description": "Credenciales incorrectas"},
        403: {"description": "Usuario inactivo"},
    },
)


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="Iniciar sesión",
    description=(
        "Recibe correo y contraseña del usuario. "
        "Si las credenciales son válidas, devuelve un token JWT "
        "y los datos básicos del usuario para que el frontend "
        "pueda redirigir según su rol."
    ),
)
def login(datos: LoginRequest, db: Session = Depends(get_db)):
    return AuthController.login(datos, db)