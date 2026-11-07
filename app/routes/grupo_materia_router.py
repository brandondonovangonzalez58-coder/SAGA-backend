from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas import GrupoMateriaCreate, GrupoMateriaResponse
from app.controllers.grupo_materia_controller import GrupoMateriaController

router = APIRouter(prefix="/grupo-materias", tags=["GrupoMaterias"])

@router.get("/", response_model=List[GrupoMateriaResponse], summary="Listar asignaciones")
def listar(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    return GrupoMateriaController.listar(db, buscar)

@router.get("/{id_gm}", response_model=GrupoMateriaResponse, summary="Obtener asignación")
def obtener(id_gm: int, db: Session = Depends(get_db)):
    return GrupoMateriaController.obtener(id_gm, db)

@router.post("/", response_model=GrupoMateriaResponse, status_code=status.HTTP_201_CREATED, summary="Crear asignación")
def crear(datos: GrupoMateriaCreate, db: Session = Depends(get_db)):
    return GrupoMateriaController.crear(datos, db)

@router.put("/{id_gm}", response_model=GrupoMateriaResponse, summary="Actualizar asignación")
def actualizar(id_gm: int, datos: GrupoMateriaCreate, db: Session = Depends(get_db)):
    return GrupoMateriaController.actualizar(id_gm, datos, db)

@router.delete("/{id_gm}", summary="Eliminar asignación")
def eliminar(id_gm: int, db: Session = Depends(get_db)):
    return GrupoMateriaController.eliminar(id_gm, db)