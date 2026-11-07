from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas import MateriaCreate, MateriaResponse
from app.controllers.materia_controller import MateriaController

router = APIRouter(prefix="/materias", tags=["Materias"])

@router.get("/", response_model=List[MateriaResponse], summary="Listar materias")
def listar(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    return MateriaController.listar(db, buscar)

@router.get("/{id_materia}", response_model=MateriaResponse, summary="Obtener materia")
def obtener(id_materia: int, db: Session = Depends(get_db)):
    return MateriaController.obtener(id_materia, db)

@router.post("/", response_model=MateriaResponse, status_code=status.HTTP_201_CREATED, summary="Crear materia")
def crear(datos: MateriaCreate, db: Session = Depends(get_db)):
    return MateriaController.crear(datos, db)

@router.put("/{id_materia}", response_model=MateriaResponse, summary="Actualizar materia")
def actualizar(id_materia: int, datos: MateriaCreate, db: Session = Depends(get_db)):
    return MateriaController.actualizar(id_materia, datos, db)

@router.delete("/{id_materia}", summary="Eliminar materia")
def eliminar(id_materia: int, db: Session = Depends(get_db)):
    return MateriaController.eliminar(id_materia, db)