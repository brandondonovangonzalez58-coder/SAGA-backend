from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas import GrupoCreate, GrupoResponse
from app.controllers.grupo_controller import GrupoController

router = APIRouter(prefix="/grupos", tags=["Grupos"])

@router.get("/", response_model=List[GrupoResponse], summary="Listar grupos")
def listar(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    return GrupoController.listar(db, buscar)

@router.get("/{id_grupo}", response_model=GrupoResponse, summary="Obtener grupo")
def obtener(id_grupo: int, db: Session = Depends(get_db)):
    return GrupoController.obtener(id_grupo, db)

@router.post("/", response_model=GrupoResponse, status_code=status.HTTP_201_CREATED, summary="Crear grupo")
def crear(datos: GrupoCreate, db: Session = Depends(get_db)):
    return GrupoController.crear(datos, db)

@router.put("/{id_grupo}", response_model=GrupoResponse, summary="Actualizar grupo")
def actualizar(id_grupo: int, datos: GrupoCreate, db: Session = Depends(get_db)):
    return GrupoController.actualizar(id_grupo, datos, db)

@router.delete("/{id_grupo}", summary="Eliminar grupo")
def eliminar(id_grupo: int, db: Session = Depends(get_db)):
    return GrupoController.eliminar(id_grupo, db)