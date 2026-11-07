from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import Optional
from app.models import Grupo

class GrupoController:
    @staticmethod
    def listar(db: Session, buscar: Optional[str] = None):
        query = db.query(Grupo)
        if buscar:
            query = query.filter(Grupo.nombre.like(f"%{buscar}%"))
        return query.all()

    @staticmethod
    def obtener(id_grupo: int, db: Session):
        grupo = db.query(Grupo).filter(Grupo.id_grupo == id_grupo).first()
        if not grupo: raise HTTPException(status_code=404, detail="Grupo no encontrado")
        return grupo

    @staticmethod
    def crear(datos, db: Session):
        try:
            nuevo = Grupo(**datos.model_dump())
            db.add(nuevo); db.commit(); db.refresh(nuevo)
            return nuevo
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="Error al crear: verifica los datos.")

    @staticmethod
    def actualizar(id_grupo: int, datos, db: Session):
        grupo = GrupoController.obtener(id_grupo, db)
        try:
            for campo, valor in datos.model_dump(exclude_unset=True).items(): setattr(grupo, campo, valor)
            db.commit(); db.refresh(grupo)
            return grupo
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="Error al actualizar.")

    @staticmethod
    def eliminar(id_grupo: int, db: Session):
        grupo = GrupoController.obtener(id_grupo, db)
        try:
            db.delete(grupo); db.commit()
            return {"mensaje": "Grupo eliminado"}
        except IntegrityError:
            db.rollback(); raise HTTPException(status_code=400, detail="No se puede eliminar: tiene estudiantes o materias ligadas.")