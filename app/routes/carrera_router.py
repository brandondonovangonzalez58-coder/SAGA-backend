from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas import CarreraCreate, CarreraResponse
from app.controllers.carrera_controller import CarreraController

router = APIRouter(prefix="/carreras", tags=["Carreras"])

@router.get("/", response_model=List[CarreraResponse], summary="Listar carreras")
def listar(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    return CarreraController.listar(db, buscar)

@router.get("/{id_carrera}", response_model=CarreraResponse, summary="Obtener carrera")
def obtener(id_carrera: int, db: Session = Depends(get_db)):
    return CarreraController.obtener(id_carrera, db)

@router.post("/", response_model=CarreraResponse, status_code=status.HTTP_201_CREATED, summary="Crear carrera")
def crear(datos: CarreraCreate, db: Session = Depends(get_db)):
    return CarreraController.crear(datos, db)

@router.put("/{id_carrera}", response_model=CarreraResponse, summary="Actualizar carrera")
def actualizar(id_carrera: int, datos: CarreraCreate, db: Session = Depends(get_db)):
    return CarreraController.actualizar(id_carrera, datos, db)

@router.delete("/{id_carrera}", summary="Eliminar carrera")
def eliminar(id_carrera: int, db: Session = Depends(get_db)):
    return CarreraController.eliminar(id_carrera, db)