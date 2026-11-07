from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import Optional
from app.models import GrupoMateria

class GrupoMateriaController:

    @staticmethod
    def listar(db: Session, buscar: Optional[str] = None):
        # Traemos las relaciones para que el celular muestre los nombres
        query = db.query(GrupoMateria).options(
            joinedload(GrupoMateria.grupo),
            joinedload(GrupoMateria.materia)
        )
        
        if buscar:
            try:
                id_buscar = int(buscar)
                query = query.filter(
                    (GrupoMateria.id_grupo == id_buscar) | 
                    (GrupoMateria.id_materia == id_buscar) |
                    (GrupoMateria.id_docente == id_buscar)
                )
            except ValueError:
                query = query.filter(GrupoMateria.periodo.like(f"%{buscar}%"))
        return query.all()

    @staticmethod
    def obtener(id_gm: int, db: Session):
        gm = db.query(GrupoMateria).filter(GrupoMateria.id_grupo_materia == id_gm).first()
        if not gm:
            raise HTTPException(status_code=404, detail="GrupoMateria no encontrada")
        return gm

    @staticmethod
    def crear(datos, db: Session):
        try:
            nuevo = GrupoMateria(**datos.model_dump())
            db.add(nuevo)
            db.commit()
            db.refresh(nuevo)
            return nuevo
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=400, 
                detail="Error: El grupo, la materia o el docente no existen, o ya están asignados en este periodo."
            )

    @staticmethod
    def actualizar(id_gm: int, datos, db: Session):
        gm = GrupoMateriaController.obtener(id_gm, db)
        try:
            for campo, valor in datos.model_dump(exclude_unset=True).items():
                setattr(gm, campo, valor)
            db.commit()
            db.refresh(gm)
            return gm
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="No se pudo actualizar: Verifica que los IDs existan.")

    @staticmethod
    def eliminar(id_gm: int, db: Session):
        gm = GrupoMateriaController.obtener(id_gm, db)
        try:
            db.delete(gm)
            db.commit()
            return {"mensaje": "GrupoMateria eliminada correctamente"}
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=400, 
                detail="No se puede eliminar: Esta asignación ya tiene sesiones o asistencias registradas."
            )