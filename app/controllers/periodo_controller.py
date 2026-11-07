from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import Optional
from app.models import Periodo

class PeriodoController:
    @staticmethod
    def listar(db: Session, buscar: Optional[str] = None):
        query = db.query(Periodo)
        if buscar:
            query = query.filter(Periodo.nombre.like(f"%{buscar}%"))
        return query.all()

    @staticmethod
    def obtener(id_periodo: int, db: Session):
        per = db.query(Periodo).filter(Periodo.id_periodo == id_periodo).first()
        if not per: raise HTTPException(status_code=404, detail="Periodo no encontrado")
        return per

    @staticmethod
    def crear(datos, db: Session):
        try:
            nuevo = Periodo(**datos.model_dump())
            db.add(nuevo); db.commit(); db.refresh(nuevo)
            return nuevo
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="El nombre del periodo ya existe.")

    @staticmethod
    def actualizar(id_periodo: int, datos, db: Session):
        per = PeriodoController.obtener(id_periodo, db)
        try:
            for campo, valor in datos.model_dump(exclude_unset=True).items(): setattr(per, campo, valor)
            db.commit(); db.refresh(per)
            return per
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="Error al actualizar.")

    @staticmethod
    def eliminar(id_periodo: int, db: Session):
        per = PeriodoController.obtener(id_periodo, db)
        try:
            db.delete(per); db.commit()
            return {"mensaje": "Periodo eliminado"}
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="No se puede eliminar.")