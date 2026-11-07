from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas.docente_schema import DocenteCreate, DocenteResponse
from app.controllers.docente_controller import DocenteController

router = APIRouter(prefix="/docentes", tags=["Docentes"])

@router.get("/", response_model=List[DocenteResponse], summary="Listar docentes")
def listar(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    return DocenteController.listar(db, buscar)

@router.get("/{id_docente}", response_model=DocenteResponse, summary="Obtener docente")
def obtener(id_docente: int, db: Session = Depends(get_db)):
    return DocenteController.obtener(id_docente, db)

@router.post("/", response_model=DocenteResponse, status_code=status.HTTP_201_CREATED, summary="Crear docente")
def crear(datos: DocenteCreate, db: Session = Depends(get_db)):
    return DocenteController.crear(datos, db)

@router.put("/{id_docente}", response_model=DocenteResponse, summary="Actualizar docente")
def actualizar(id_docente: int, datos: DocenteCreate, db: Session = Depends(get_db)):
    return DocenteController.actualizar(id_docente, datos, db)

@router.delete("/{id_docente}", summary="Eliminar docente")
def eliminar(id_docente: int, db: Session = Depends(get_db)):
    return DocenteController.eliminar(id_docente, db)