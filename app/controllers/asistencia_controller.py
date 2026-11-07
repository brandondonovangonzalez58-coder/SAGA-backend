from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import Optional
from app.models import Asistencia, Estudiante  # <-- Agregamos Estudiante

class AsistenciaController:
    @staticmethod
    def listar(db: Session, buscar: Optional[str] = None):
        # Hacemos el JOIN para traer al estudiante y a su vez al usuario (para el nombre)
        query = db.query(Asistencia).options(
            joinedload(Asistencia.estudiante).joinedload(Estudiante.usuario)
        )
        
        if buscar:
            try:
                id_b = int(buscar)
                query = query.filter((Asistencia.id_sesion == id_b) | (Asistencia.id_estudiante == id_b))
            except ValueError:
                query = query.filter(Asistencia.estado.like(f"%{buscar}%"))
        return query.all()

    @staticmethod
    def obtener(id_asistencia: int, db: Session):
        asis = db.query(Asistencia).filter(Asistencia.id_asistencia == id_asistencia).first()
        if not asis: raise HTTPException(status_code=404, detail="Asistencia no encontrada")
        return asis

    @staticmethod
    def crear(datos, db: Session):
        try:
            nueva = Asistencia(**datos.model_dump())
            db.add(nueva)
            db.commit()
            db.refresh(nueva)
            return nueva
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Ya existe asistencia para este alumno en esta sesión.")

    @staticmethod
    def actualizar(id_asistencia: int, datos, db: Session):
        asis = AsistenciaController.obtener(id_asistencia, db)
        try:
            for campo, valor in datos.model_dump(exclude_unset=True).items(): setattr(asis, campo, valor)
            db.commit(); db.refresh(asis)
            return asis
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="Error al actualizar la asistencia.")

    @staticmethod
    def eliminar(id_asistencia: int, db: Session):
        asis = AsistenciaController.obtener(id_asistencia, db)
        try:
            db.delete(asis); db.commit()
            return {"mensaje": "Asistencia eliminada"}
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="No se puede eliminar.")