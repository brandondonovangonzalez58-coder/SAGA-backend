from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.controllers.usuario_controller import UsuarioController

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/", response_model=List[UsuarioResponse], summary="Listar usuarios")
def listar(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    return UsuarioController.listar(db, buscar)

@router.get("/{id_usuario}", response_model=UsuarioResponse, summary="Obtener usuario")
def obtener(id_usuario: int, db: Session = Depends(get_db)):
    return UsuarioController.obtener(id_usuario, db)

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED, summary="Crear usuario")
def crear(datos: UsuarioCreate, db: Session = Depends(get_db)):
    return UsuarioController.crear(datos, db)

@router.put("/{id_usuario}", response_model=UsuarioResponse, summary="Actualizar usuario")
def actualizar(id_usuario: int, datos: UsuarioUpdate, db: Session = Depends(get_db)):
    return UsuarioController.actualizar(id_usuario, datos, db)

@router.delete("/{id_usuario}", summary="Eliminar usuario")
def eliminar(id_usuario: int, db: Session = Depends(get_db)):
    return UsuarioController.eliminar(id_usuario, db)