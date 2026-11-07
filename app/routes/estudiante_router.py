from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional  # Agregamos Optional para la búsqueda
from app.database import get_db
from app.schemas import EstudianteCreate, EstudianteResponse
from app.controllers.estudiante_controller import EstudianteController

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])


@router.get("/", response_model=List[EstudianteResponse], summary="Listar estudiantes")
def listar(buscar: Optional[str] = None, db: Session = Depends(get_db)):
    # Le pasamos el parámetro 'buscar' al controlador para que filtre
    return EstudianteController.listar(db, buscar)


@router.get("/{id_estudiante}", response_model=EstudianteResponse, summary="Obtener estudiante")
def obtener(id_estudiante: int, db: Session = Depends(get_db)):
    return EstudianteController.obtener(id_estudiante, db)


@router.post("/", response_model=EstudianteResponse, status_code=status.HTTP_201_CREATED, summary="Crear estudiante")
def crear(datos: EstudianteCreate, db: Session = Depends(get_db)):
    return EstudianteController.crear(datos, db)


@router.put("/{id_estudiante}", response_model=EstudianteResponse, summary="Actualizar estudiante")
def actualizar(id_estudiante: int, datos: EstudianteCreate, db: Session = Depends(get_db)):
    return EstudianteController.actualizar(id_estudiante, datos, db)


@router.delete("/{id_estudiante}", summary="Eliminar estudiante")
def eliminar(id_estudiante: int, db: Session = Depends(get_db)):
    return EstudianteController.eliminar(id_estudiante, db)



@router.get("/grupo/{id_grupo}", response_model=List[EstudianteResponse], summary="Listar estudiantes por grupo")
def listar_por_grupo(id_grupo: int, db: Session = Depends(get_db)):
    return EstudianteController.listar_por_grupo(id_grupo, db)
