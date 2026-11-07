from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import Optional
from app.models import Docente, Usuario

class DocenteController:

    @staticmethod
    def _formatear_docente(doc: Docente):
        return {
            "id_docente": doc.id_docente,
            "id_usuario": doc.id_usuario,
            "numero_empleado": doc.numero_empleado,
            "especialidad": doc.especialidad,
            "usuario": {
                "id_usuario": doc.usuario.id_usuario,
                "nombre": doc.usuario.nombre,
                "apellidos": doc.usuario.apellidos,
                "correo": doc.usuario.correo,
                "matricula": doc.usuario.matricula,
                "id_rol": doc.usuario.id_rol,
                "rol": doc.usuario.rol.nombre if doc.usuario.rol else None,
                "activo": doc.usuario.activo
            } if doc.usuario else None
        }

    @staticmethod
    def listar(db: Session, buscar: Optional[str] = None):
        query = db.query(Docente).options(
            joinedload(Docente.usuario).joinedload(Usuario.rol)
        )
        if buscar:
            query = query.filter(
                (Docente.numero_empleado.like(f"%{buscar}%")) | 
                (Docente.especialidad.like(f"%{buscar}%"))
            )
        
        docentes = query.all()
        return [DocenteController._formatear_docente(doc) for doc in docentes]

    @staticmethod
    def obtener(id_docente: int, db: Session):
        doc = db.query(Docente).options(
            joinedload(Docente.usuario).joinedload(Usuario.rol)
        ).filter(Docente.id_docente == id_docente).first()
        
        if not doc:
            raise HTTPException(status_code=404, detail="Docente no encontrado")
        return DocenteController._formatear_docente(doc)

    @staticmethod
    def crear(datos, db: Session):
        try:
            nuevo = Docente(**datos.model_dump())
            db.add(nuevo)
            db.commit()
            db.refresh(nuevo)
            return nuevo
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="El ID de usuario o número de empleado ya existe.")

    @staticmethod
    def actualizar(id_docente: int, datos, db: Session):
        doc = db.query(Docente).filter(Docente.id_docente == id_docente).first()
        if not doc:
            raise HTTPException(status_code=404, detail="Docente no encontrado")
        try:
            for campo, valor in datos.model_dump(exclude_unset=True).items():
                setattr(doc, campo, valor)
            db.commit()
            db.refresh(doc)
            return doc
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Datos duplicados o inválidos.")

    @staticmethod
    def eliminar(id_docente: int, db: Session):
        doc = db.query(Docente).filter(Docente.id_docente == id_docente).first()
        if not doc:
            raise HTTPException(status_code=404, detail="Docente no encontrado")
        try:
            db.delete(doc)
            db.commit()
            return {"mensaje": "Docente eliminado correctamente"}
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="No se puede eliminar: El docente tiene materias asignadas.")