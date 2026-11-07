from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import Optional
from app.models import Materia

class MateriaController:
    @staticmethod
    def listar(db: Session, buscar: Optional[str] = None):
        query = db.query(Materia)
        if buscar:
            query = query.filter((Materia.nombre.like(f"%{buscar}%")) | (Materia.clave.like(f"%{buscar}%")))
        return query.all()

    @staticmethod
    def obtener(id_materia: int, db: Session):
        mat = db.query(Materia).filter(Materia.id_materia == id_materia).first()
        if not mat: raise HTTPException(status_code=404, detail="Materia no encontrada")
        return mat

    @staticmethod
    def crear(datos, db: Session):
        try:
            nueva = Materia(**datos.model_dump())
            db.add(nueva); db.commit(); db.refresh(nueva)
            return nueva
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="La clave de la materia ya existe.")

    @staticmethod
    def actualizar(id_materia: int, datos, db: Session):
        mat = MateriaController.obtener(id_materia, db)
        try:
            for campo, valor in datos.model_dump(exclude_unset=True).items(): setattr(mat, campo, valor)
            db.commit(); db.refresh(mat)
            return mat
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="La clave ya está registrada.")

    @staticmethod
    def eliminar(id_materia: int, db: Session):
        mat = MateriaController.obtener(id_materia, db)
        try:
            db.delete(mat); db.commit()
            return {"mensaje": "Materia eliminada"}
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="No se puede eliminar: tiene grupos asignados.")