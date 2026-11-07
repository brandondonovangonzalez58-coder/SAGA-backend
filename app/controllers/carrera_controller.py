from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import Optional
from app.models import Carrera

class CarreraController:
    @staticmethod
    def listar(db: Session, buscar: Optional[str] = None):
        query = db.query(Carrera)
        if buscar:
            query = query.filter((Carrera.nombre.like(f"%{buscar}%")) | (Carrera.siglas.like(f"%{buscar}%")))
        return query.all()

    @staticmethod
    def obtener(id_carrera: int, db: Session):
        carrera = db.query(Carrera).filter(Carrera.id_carrera == id_carrera).first()
        if not carrera: raise HTTPException(status_code=404, detail="Carrera no encontrada")
        return carrera

    @staticmethod
    def crear(datos, db: Session):
        try:
            nueva = Carrera(**datos.model_dump())
            db.add(nueva); db.commit(); db.refresh(nueva)
            return nueva
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="El nombre de la carrera ya existe.")

    @staticmethod
    def actualizar(id_carrera: int, datos, db: Session):
        carrera = CarreraController.obtener(id_carrera, db)
        try:
            for campo, valor in datos.model_dump(exclude_unset=True).items(): setattr(carrera, campo, valor)
            db.commit(); db.refresh(carrera)
            return carrera
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="El nombre ya está en uso.")

    @staticmethod
    def eliminar(id_carrera: int, db: Session):
        carrera = CarreraController.obtener(id_carrera, db)
        try:
            db.delete(carrera); db.commit()
            return {"mensaje": "Carrera eliminada"}
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="No se puede eliminar: tiene grupos asignados.")