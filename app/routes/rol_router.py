from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas import RolCreate, RolResponse
from app.controllers.rol_controller import RolController

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/", response_model=List[RolResponse], summary="Listar roles")
def listar(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    return RolController.listar(db, buscar)

@router.get("/{id_rol}", response_model=RolResponse, summary="Obtener rol")
def obtener(id_rol: int, db: Session = Depends(get_db)):
    return RolController.obtener(id_rol, db)

@router.post("/", response_model=RolResponse, status_code=status.HTTP_201_CREATED, summary="Crear rol")
def crear(datos: RolCreate, db: Session = Depends(get_db)):
    return RolController.crear(datos, db)

@router.put("/{id_rol}", response_model=RolResponse, summary="Actualizar rol")
def actualizar(id_rol: int, datos: RolCreate, db: Session = Depends(get_db)):
    return RolController.actualizar(id_rol, datos, db)

@router.delete("/{id_rol}", summary="Eliminar rol")
def eliminar(id_rol: int, db: Session = Depends(get_db)):
    return RolController.eliminar(id_rol, db)