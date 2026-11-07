from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas import PeriodoCreate, PeriodoResponse
from app.controllers.periodo_controller import PeriodoController

router = APIRouter(prefix="/periodos", tags=["Periodos"])

@router.get("/", response_model=List[PeriodoResponse], summary="Listar periodos")
def listar(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    return PeriodoController.listar(db, buscar)

@router.get("/{id_periodo}", response_model=PeriodoResponse, summary="Obtener periodo")
def obtener(id_periodo: int, db: Session = Depends(get_db)):
    return PeriodoController.obtener(id_periodo, db)

@router.post("/", response_model=PeriodoResponse, status_code=status.HTTP_201_CREATED, summary="Crear periodo")
def crear(datos: PeriodoCreate, db: Session = Depends(get_db)):
    return PeriodoController.crear(datos, db)

@router.put("/{id_periodo}", response_model=PeriodoResponse, summary="Actualizar periodo")
def actualizar(id_periodo: int, datos: PeriodoCreate, db: Session = Depends(get_db)):
    return PeriodoController.actualizar(id_periodo, datos, db)

@router.delete("/{id_periodo}", summary="Eliminar periodo")
def eliminar(id_periodo: int, db: Session = Depends(get_db)):
    return PeriodoController.eliminar(id_periodo, db)