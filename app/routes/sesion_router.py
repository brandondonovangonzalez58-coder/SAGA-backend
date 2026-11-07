from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas import SesionCreate, SesionResponse
from app.controllers.sesion_controller import SesionController

router = APIRouter(prefix="/sesiones", tags=["Sesiones"])

@router.get("/", response_model=List[SesionResponse], summary="Listar sesiones")
def listar(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    return SesionController.listar(db, buscar)

@router.get("/{id_sesion}", response_model=SesionResponse, summary="Obtener sesión")
def obtener(id_sesion: int, db: Session = Depends(get_db)):
    return SesionController.obtener(id_sesion, db)

@router.post("/", response_model=SesionResponse, status_code=status.HTTP_201_CREATED, summary="Crear sesión")
def crear(datos: SesionCreate, db: Session = Depends(get_db)):
    return SesionController.crear(datos, db)

@router.put("/{id_sesion}", response_model=SesionResponse, summary="Actualizar sesión")
def actualizar(id_sesion: int, datos: SesionCreate, db: Session = Depends(get_db)):
    return SesionController.actualizar(id_sesion, datos, db)

@router.delete("/{id_sesion}", summary="Eliminar sesión")
def eliminar(id_sesion: int, db: Session = Depends(get_db)):
    return SesionController.eliminar(id_sesion, db)