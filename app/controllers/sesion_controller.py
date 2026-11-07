from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import Optional
from app.models import Sesion

class SesionController:
    @staticmethod
    def listar(db: Session, buscar: Optional[str] = None):
        query = db.query(Sesion)
        if buscar:
            query = query.filter(Sesion.tema.like(f"%{buscar}%"))
        return query.all()

    @staticmethod
    def obtener(id_sesion: int, db: Session):
        ses = db.query(Sesion).filter(Sesion.id_sesion == id_sesion).first()
        if not ses: raise HTTPException(status_code=404, detail="Sesión no encontrada")
        return ses

    @staticmethod
    def crear(datos, db: Session):
        try:
            nueva = Sesion(**datos.model_dump())
            db.add(nueva); db.commit(); db.refresh(nueva)
            return nueva
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="Error: El grupo-materia no existe.")

    @staticmethod
    def actualizar(id_sesion: int, datos, db: Session):
        ses = SesionController.obtener(id_sesion, db)
        try:
            for campo, valor in datos.model_dump(exclude_unset=True).items(): setattr(ses, campo, valor)
            db.commit(); db.refresh(ses)
            return ses
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="Error al actualizar la sesión.")

    @staticmethod
    def eliminar(id_sesion: int, db: Session):
        ses = SesionController.obtener(id_sesion, db)
        try:
            db.delete(ses); db.commit()
            return {"mensaje": "Sesión eliminada"}
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="No se puede eliminar: tiene asistencias ligadas.")