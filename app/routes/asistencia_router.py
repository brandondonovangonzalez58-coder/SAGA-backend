from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas import AsistenciaCreate, AsistenciaResponse
from app.controllers.asistencia_controller import AsistenciaController

router = APIRouter(prefix="/asistencias", tags=["Asistencias"])

@router.get("/", response_model=List[AsistenciaResponse], summary="Listar asistencias")
def listar(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    return AsistenciaController.listar(db, buscar)

@router.get("/{id_asistencia}", response_model=AsistenciaResponse, summary="Obtener asistencia")
def obtener(id_asistencia: int, db: Session = Depends(get_db)):
    return AsistenciaController.obtener(id_asistencia, db)

@router.post("/", response_model=AsistenciaResponse, status_code=status.HTTP_201_CREATED, summary="Registrar asistencia")
def crear(datos: AsistenciaCreate, db: Session = Depends(get_db)):
    return AsistenciaController.crear(datos, db)

@router.put("/{id_asistencia}", response_model=AsistenciaResponse, summary="Actualizar asistencia")
def actualizar(id_asistencia: int, datos: AsistenciaCreate, db: Session = Depends(get_db)):
    return AsistenciaController.actualizar(id_asistencia, datos, db)

@router.delete("/{id_asistencia}", summary="Eliminar asistencia")
def eliminar(id_asistencia: int, db: Session = Depends(get_db)):
    return AsistenciaController.eliminar(id_asistencia, db)